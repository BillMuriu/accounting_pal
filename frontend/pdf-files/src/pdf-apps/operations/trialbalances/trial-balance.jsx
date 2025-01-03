import React, { useState, useEffect } from "react";
import { Download } from "lucide-react";
import TrialBalanceForm from "./components/trial-balance-form";
import { format } from "date-fns";
import { trialBalanceColumns } from "./components/trial-balance-columns";
import { TrialBalanceDataTable } from "@/components/tables/trial-balance-table";
import { PDFDownloadLink } from "@react-pdf/renderer";
import TrialBalancePDF from "./components/trial-balance-pdf";
import clsx from "clsx";

// Fetch function to get trial balance data from the backend
const fetchTrialBalance = async (startDate, endDate) => {
  const response = await fetch(
    `http://127.0.0.1:8000/api/operations-trialbalances/trial-balance/?start_date=${startDate}&end_date=${endDate}`
  );
  if (!response.ok) {
    throw new Error("Error fetching trial balance data");
  }
  const data = await response.json();
  return data;
};

const TrialBalance = () => {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFormSubmit = (formData) => {
    setStartDate(format(formData.start_date, "yyyy-MM-dd"));
    setEndDate(format(formData.end_date, "yyyy-MM-dd"));
  };

  useEffect(() => {
    if (startDate && endDate) {
      const fetchData = async () => {
        setIsLoading(true);
        setError(null);
        try {
          const result = await fetchTrialBalance(startDate, endDate);
          setData(result);
        } catch (err) {
          setError(err.message);
        } finally {
          setIsLoading(false);
        }
      };

      fetchData();
    }
  }, [startDate, endDate]);

  const transformData = (data) => {
    const openingBalances = [];
    const closingBalances = [];
    const others = [];
    let totalDebits = 0;
    let totalCredits = 0;

    // Get all unique accounts from both debits and credits
    const allAccounts = new Set([
      ...Object.keys(data.debits),
      ...Object.keys(data.credits),
    ]);

    console.log("Data received:", data); // Log the entire data to check its structure

    // Iterate through each account
    allAccounts.forEach((account) => {
      // Get the debits and credits safely
      const debits =
        typeof data.debits[account] === "object"
          ? data.debits[account]?.amount || 0
          : data.debits[account] || 0;
      const credits =
        typeof data.credits[account] === "object"
          ? data.credits[account]?.amount || 0
          : data.credits[account] || 0;

      // Update total debits and credits
      totalDebits += debits;
      totalCredits += credits;

      // Create a row for the account
      const row = {
        description: account.trim(), // Ensure no extra spaces in account name
        debits,
        credits,
      };

      // Determine where to categorize this account (opening, closing, others)
      if (account.toLowerCase().includes("opening")) {
        console.log("Opening balance found for:", account, row); // Log when an opening balance is found
        openingBalances.push(row);
      } else if (account.toLowerCase().includes("closing")) {
        closingBalances.push(row);
      } else {
        others.push(row);
      }
    });

    console.log("Opening balances:", openingBalances); // Log the openingBalances array

    // Return the transformed data
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

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="flex items-center justify-center flex-col h-full w-full sm:w-[800px] lg:w-[900px] xl:w-[1000px] mb-10 overflow-x-hidden">
      {" "}
      {/* Ensure no horizontal overflow */}
      <TrialBalanceForm onSubmit={handleFormSubmit} loading={isLoading} />
      {data && (
        <div className="w-full sm:w-[800px] mt-8 bg-white shadow-lg rounded-lg p-6 relative max-w-full">
          {" "}
          {/* Prevent horizontal overflow */}
          {/* Header with title and PDF download link */}
          <div className="relative mb-6">
            <h2 className="text-2xl font-bold text-center">Trial Balance</h2>
            {transformedData &&
            transformedData.openingBalances.length > 0 &&
            transformedData.closingBalances.length > 0 &&
            transformedData.others.length > 0 ? (
              <PDFDownloadLink
                document={
                  <TrialBalancePDF
                    startDate={startDate}
                    endDate={endDate}
                    transformedData={transformedData}
                  />
                }
                fileName={`Operations_Trial_Balance_${startDate}_${endDate}.pdf`}
                className="absolute top-0 right-0 flex items-center gap-1 text-sm font-medium text-blue-500 hover:underline"
              >
                {({ loading }) =>
                  loading ? (
                    "Preparing..."
                  ) : (
                    <>
                      <Download className="w-4 h-4" />
                      Download
                    </>
                  )
                }
              </PDFDownloadLink>
            ) : (
              <p className="absolute top-0 right-0">Loading...</p>
            )}
          </div>
          <div className="space-y-8">
            <section>
              <h3 className="text-md font-semibold mt-4 mb-1 bg-white p-2 rounded-md">
                Opening Balances
              </h3>
              <TrialBalanceDataTable
                data={transformedData.openingBalances}
                columns={trialBalanceColumns}
              />
            </section>
            <section>
              <h3 className="text-md font-semibold mt-4 mb-1 bg-white p-2 rounded-md">
                Main Accounts
              </h3>
              <TrialBalanceDataTable
                data={transformedData.others}
                columns={trialBalanceColumns}
              />
            </section>
            <section>
              <h3 className="text-md font-semibold mt-4 mb-1 bg-white p-2 rounded-md">
                Closing Balances
              </h3>
              <TrialBalanceDataTable
                data={transformedData.closingBalances}
                columns={trialBalanceColumns}
              />
            </section>
          </div>
          {/* Totals Table */}
          <section>
            <h3 className="text-md font-semibold mt-4 mb-1 bg-gray-50 p-2 rounded-md">
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
