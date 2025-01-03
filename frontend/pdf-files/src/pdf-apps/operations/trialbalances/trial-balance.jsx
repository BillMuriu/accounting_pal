import React, { useState, useEffect } from "react";
import TrialBalanceForm from "./components/trial-balance-form";
import { format } from "date-fns";
import { trialBalanceColumns } from "./components/trial-balance-columns";
import { TrialBalanceDataTable } from "@/components/tables/trial-balance-table";

// Fetch function to get trial balance data from the backend
const fetchTrialBalance = async (startDate, endDate) => {
  console.log("Fetching trial balance data for:", { startDate, endDate });
  const response = await fetch(
    `http://127.0.0.1:8000/api/operations-trialbalances/trial-balance/?start_date=${startDate}&end_date=${endDate}`
  );
  if (!response.ok) {
    throw new Error("Error fetching trial balance data");
  }
  const data = await response.json();
  console.log("Fetched trial balance data:", data);
  return data;
};

const TrialBalance = () => {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Handle form submission
  const handleFormSubmit = (formData) => {
    setStartDate(format(formData.start_date, "yyyy-MM-dd"));
    setEndDate(format(formData.end_date, "yyyy-MM-dd"));
  };

  // Fetch data when startDate or endDate changes
  useEffect(() => {
    if (startDate && endDate) {
      const fetchData = async () => {
        setIsLoading(true);
        setError(null);
        try {
          const result = await fetchTrialBalance(startDate, endDate);
          console.log("Received trial balance result:", result);
          setData(result);
        } catch (err) {
          console.error("Error fetching trial balance:", err.message);
          setError(err.message);
        } finally {
          setIsLoading(false);
        }
      };

      fetchData();
    }
  }, [startDate, endDate]);

  // Transform data to match the table format
  const transformData = (data) => {
    const openingBalances = [];
    const closingBalances = [];
    const others = [];
    let totalDebits = 0;
    let totalCredits = 0;

    console.log("Transforming data:", data);

    // Combine all accounts from both debits and credits
    const allAccounts = new Set([
      ...Object.keys(data.debits),
      ...Object.keys(data.credits),
    ]);

    allAccounts.forEach((account) => {
      const debits =
        typeof data.debits[account] === "object"
          ? data.debits[account]?.amount || 0
          : data.debits[account] || 0;
      const credits =
        typeof data.credits[account] === "object"
          ? data.credits[account]?.amount || 0
          : data.credits[account] || 0;

      console.log(`Processing account: ${account}`, { debits, credits });

      totalDebits += debits;
      totalCredits += credits;

      const row = {
        description: account,
        debits,
        credits,
      };

      if (account.toLowerCase().includes("opening")) {
        console.log("Adding to opening balances:", row);
        openingBalances.push(row);
      } else if (account.toLowerCase().includes("closing")) {
        console.log("Adding to closing balances:", row);
        closingBalances.push(row);
      } else {
        others.push(row);
      }
    });

    console.log("Transformed data:", {
      openingBalances,
      closingBalances,
      others,
    });

    return {
      openingBalances,
      closingBalances,
      others,
      totalDebits,
      totalCredits,
    };
  };

  const transformedData = data
    ? transformData(data)
    : {
        openingBalances: [],
        closingBalances: [],
        others: [],
        totalDebits: 0,
        totalCredits: 0,
      };

  // Show loading or error state
  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="w-screen max-w-4xl bg-white p-6 rounded-lg shadow-lg">
      <TrialBalanceForm onSubmit={handleFormSubmit} loading={isLoading} />
      {data && (
        <div className="w-full mt-8">
          <h2 className="text-2xl font-bold text-center mb-6">Trial Balance</h2>
          <div className="space-y-8">
            <section>
              <h3 className="text-xl font-semibold mb-4 bg-blue-50 p-2 rounded-md">
                Opening Balances
              </h3>
              <TrialBalanceDataTable
                data={transformedData.openingBalances}
                columns={trialBalanceColumns}
              />
            </section>
            <section>
              <h3 className="text-xl font-semibold mb-4 bg-gray-50 p-2 rounded-md">
                Closing Balances
              </h3>
              <TrialBalanceDataTable
                data={transformedData.closingBalances}
                columns={trialBalanceColumns}
              />
            </section>
            <section>
              <h3 className="text-xl font-semibold mb-4 bg-white p-2 rounded-md">
                Other Accounts
              </h3>
              <TrialBalanceDataTable
                data={transformedData.others}
                columns={trialBalanceColumns}
              />
            </section>
          </div>

          {/* Totals Table */}
          <section>
            <h3 className="text-xl font-semibold mb-4 bg-green-50 p-2 rounded-md">
              Totals
            </h3>
            <TrialBalanceDataTable
              data={[
                {
                  description: "Total",
                  debits: transformedData.totalDebits,
                  credits: transformedData.totalCredits,
                },
              ]}
              columns={trialBalanceColumns}
            />
          </section>
        </div>
      )}
    </div>
  );
};

export default TrialBalance;
