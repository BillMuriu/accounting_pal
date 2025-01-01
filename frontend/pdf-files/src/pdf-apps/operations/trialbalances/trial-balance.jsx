import React, { useState, useEffect } from "react";
import TrialBalanceForm from "./components/trial-balance-form";
import { format } from "date-fns";
import { trialBalanceColumns } from "./components/trial-balance-columns";
import { TrialBalanceDataTable } from "@/components/tables/trial-balance-table";

const fetchTrialBalance = async (startDate, endDate) => {
  const response = await fetch(
    `http://127.0.0.1:8000/api/operations-trialbalances/trial-balance/?start_date=${startDate}&end_date=${endDate}`
  );
  if (!response.ok) {
    throw new Error("Error fetching trial balance data");
  }
  return await response.json();
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

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  // Transform data to match the table format
  const transformData = (data) => {
    const debitsData = Object.entries(data.debits).map(([key, value]) => ({
      description: key,
      debits: value,
      credits: data.credits[key]?.amount || 0,
    }));

    const creditsData = Object.entries(data.credits).map(([key, value]) => ({
      description: key,
      debits: data.debits[key]?.amount || 0,
      credits: value.amount,
    }));

    return [...debitsData, ...creditsData];
  };

  const transformedData = data ? transformData(data) : [];

  return (
    <div className="flex items-center justify-center min-h-screen py-10 bg-gray-50">
      <div className="w-full max-w-4xl bg-white p-6 rounded-lg shadow-lg">
        <TrialBalanceForm onSubmit={handleFormSubmit} loading={isLoading} />
        {data && (
          <div className="mt-8">
            <h2 className="text-2xl font-bold text-center mb-6">
              Trial Balance
            </h2>
            <div className="balance">
              <TrialBalanceDataTable
                data={transformedData}
                columns={trialBalanceColumns} // Use the columns defined elsewhere
              />
              <div className="mt-6 text-center">
                <h3 className="text-lg font-semibold">
                  Total Debits: {data.total_debits.toLocaleString()}
                </h3>
                <h3 className="text-lg font-semibold">
                  Total Credits: {data.total_credits.toLocaleString()}
                </h3>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default TrialBalance;
