import React, { useState, useEffect } from "react";
import TrialBalanceForm from "./components/trial-balance-form";
import { format } from "date-fns";

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

  return (
    <div className="container">
      <TrialBalanceForm onSubmit={handleFormSubmit} loading={isLoading} />
      {data && (
        <div className="trial-balance">
          <h2>Trial Balance</h2>
          <div className="balance">
            <div>
              <h3>Debits</h3>
              <pre>{JSON.stringify(data.debits, null, 2)}</pre>
            </div>
            <div>
              <h3>Credits</h3>
              <pre>{JSON.stringify(data.credits, null, 2)}</pre>
            </div>
            <div>
              <h3>Total Debits: {data.total_debits.toLocaleString()}</h3>
              <h3>Total Credits: {data.total_credits.toLocaleString()}</h3>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default TrialBalance;
