import React, { useState } from "react";
import LedgerForm from "./components/LedgerForm";
import { rmiLedgerColumns } from "./components/ledger-columns";
import { LedgerDataTable } from "@/components/tables/ledge-table";
import { format } from "date-fns";
import { PDFDownloadLink } from "@react-pdf/renderer";
import LedgerPDF from "./components/ledger-pdf";

const Ledger = () => {
  const [loading, setLoading] = useState(false);
  const [ledgerData, setLedgerData] = useState({}); // Object to store all ledger data

  const onSubmit = async (values) => {
    setLoading(true);
    try {
      const formattedStartDate = format(values.start_date, "yyyy-MM-dd");
      const formattedEndDate = format(values.end_date, "yyyy-MM-dd");

      const response = await fetch(
        `http://127.0.0.1:8000/api/operations-ledgers/combined-ledger/?start_date=${formattedStartDate}&end_date=${formattedEndDate}`
      );
      const data = await response.json();

      const ledgers = Object.entries(data.combined_ledger).reduce(
        (acc, [key, ledger]) => {
          const ledgerData = [
            ...(ledger.debits?.map((entry) => ({
              cashbook: entry.cashbook,
              debits: entry.amount,
              credits: 0,
              date: format(new Date(entry.date), "MM/dd/yyyy"),
            })) || []),
            ...(ledger.credits?.map((entry) => ({
              cashbook: entry.cashbook,
              debits: 0,
              credits: entry.amount,
              date: format(new Date(entry.date), "MM/dd/yyyy"),
            })) || []),
            {
              cashbook: "Total Debits",
              debits: ledger.total_debits || 0,
              credits: 0,
              date: null,
            },
            {
              cashbook: "Total Credits",
              debits: 0,
              credits: ledger.total_credits || 0,
              date: null,
            },
          ];

          acc[key] = ledgerData;
          return acc;
        },
        {}
      );

      setLedgerData(ledgers);
    } catch (error) {
      console.error("Error fetching ledgers:", error);
    } finally {
      setLoading(false);
    }
  };

  const ledgerTitles = {
    rmi_ledger: "RMI Ledger Summary",
    bankcharge_ledger: "Bank Charges Ledger Summary",
    school_fund_ledger: "School Fund Ledger Summary",
    tuition_ledger: "Tuition Ledger Summary",
    other_voteheads_ledger: "Other Voteheads Ledger Summary",
  };

  return (
    <div className="flex items-center justify-center flex-col h-full w-screen">
      <LedgerForm onSubmit={onSubmit} loading={loading} />

      {Object.keys(ledgerData).map((ledgerKey) => (
        <div key={ledgerKey} className="mt-6 w-full max-w-4xl">
          <h2 className="text-xl font-bold mb-4">{ledgerTitles[ledgerKey]}</h2>
          <LedgerDataTable
            columns={rmiLedgerColumns}
            data={ledgerData[ledgerKey]}
            onSelectionChange={(newSelection) =>
              console.log(`${ledgerTitles[ledgerKey]} selection`, newSelection)
            }
          />

          {/* Add Download PDF Button */}
          <div className="mt-4">
            <PDFDownloadLink
              document={
                <LedgerPDF
                  month={"01"} // Example month
                  year={"2025"} // Example year
                  ledgerData={ledgerData} // Pass the ledger data
                />
              }
              fileName={`${ledgerKey}_ledger_${format(
                new Date(),
                "MM_dd_yyyy"
              )}.pdf`}
            >
              {({ loading }) =>
                loading ? "Preparing document..." : "Download PDF"
              }
            </PDFDownloadLink>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Ledger;
