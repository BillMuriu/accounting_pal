"use client";

import React, { useState } from "react";
import LedgerForm from "./components/LedgerForm";
import { rmiLedgerColumns } from "./components/ledger-columns";
import { LedgerDataTable } from "@/components/tables/ledge-table";
import { format } from "date-fns";
import { PDFDownloadLink } from "@react-pdf/renderer";
import { Download } from "lucide-react"; // Import the Download icon
import LedgerPDF from "./components/ledger-pdf";

const Ledger = () => {
  const [loading, setLoading] = useState(false);
  const [ledgerData, setLedgerData] = useState({});

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
            { cashbook: "", debits: 0, credits: 0, date: "-" },
          ];

          ledgerData.push({
            cashbook: "Totals",
            debits: ledger.total_debits || 0,
            credits: ledger.total_credits || 0,
            date: "-",
          });

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
    <div className="flex lg:w-screen sm:w-full items-center justify-center flex-col h-full p-4">
      <LedgerForm onSubmit={onSubmit} loading={loading} />

      {Object.keys(ledgerData).length > 0 && (
        <div className="w-full max-w-5xl mt-10 p-4 sm:p-6 bg-white shadow-lg rounded-lg">
          {/* Header */}
          <div className="relative mb-6">
            <h1 className="text-2xl font-bold text-center">Ledger Summaries</h1>
            <div className="absolute top-0 right-0">
              <PDFDownloadLink
                document={
                  <LedgerPDF
                    month={"01"} // Example month
                    year={"2025"} // Example year
                    ledgerData={ledgerData}
                  />
                }
                fileName={`combined_ledger_${format(
                  new Date(),
                  "MM_dd_yyyy"
                )}.pdf`}
              >
                {({ loading }) =>
                  loading ? (
                    <span className="text-gray-500">Preparing document...</span>
                  ) : (
                    <a
                      href="#"
                      className="flex items-center gap-2 text-blue-500 hover:text-blue-600 transition-all"
                    >
                      <Download className="w-5 h-5" />
                      Download
                    </a>
                  )
                }
              </PDFDownloadLink>
            </div>
          </div>

          {Object.keys(ledgerData).map((ledgerKey) => (
            <div key={ledgerKey} className="mb-8">
              <h2 className="text-lg sm:text-xl font-bold mb-4 border-b pb-2">
                {ledgerTitles[ledgerKey]}
              </h2>
              <LedgerDataTable
                columns={rmiLedgerColumns}
                data={ledgerData[ledgerKey].map((row) => ({
                  ...row,
                  className:
                    row.cashbook === "Totals" ? "totals-row bg-gray-100" : "",
                }))}
                onSelectionChange={(newSelection) =>
                  console.log(
                    `${ledgerTitles[ledgerKey]} selection`,
                    newSelection
                  )
                }
              />
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Ledger;
