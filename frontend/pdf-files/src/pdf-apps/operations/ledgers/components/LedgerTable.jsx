// components/LedgerTable.js
import React from "react";
import { format } from "date-fns";

const LedgerTable = ({ title, data, totalCredits, totalDebits }) => {
  const credits = data?.credits || [];
  const debits = data?.debits || [];
  let balance = 0;

  const rows = [...credits, ...debits].sort(
    (a, b) => new Date(a.date) - new Date(b.date)
  );

  return (
    <div className="mb-6">
      <h3 className="text-lg font-semibold mb-4">{title}</h3>

      <table className="min-w-full table-auto border-collapse mb-4">
        <thead>
          <tr>
            <th className="px-4 py-2 text-left border-b">Date</th>
            <th className="px-4 py-2 text-left border-b">Description</th>
            <th className="px-4 py-2 text-left border-b">Debit</th>
            <th className="px-4 py-2 text-left border-b">Credit</th>
            <th className="px-4 py-2 text-left border-b">Balance</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((entry, index) => {
            const debit = entry.type === "debit" ? entry.amount : 0;
            const credit = entry.type === "credit" ? entry.amount : 0;
            balance += credit - debit;

            return (
              <tr key={index}>
                <td className="px-4 py-2">
                  {format(new Date(entry.date), "MM/dd/yyyy")}
                </td>
                <td className="px-4 py-2">{entry.description}</td>
                <td className="px-4 py-2">
                  {debit > 0 ? debit.toLocaleString() : "-"}
                </td>
                <td className="px-4 py-2">
                  {credit > 0 ? credit.toLocaleString() : "-"}
                </td>
                <td className="px-4 py-2">{balance.toLocaleString()}</td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <div className="flex justify-between">
        <span className="font-medium">Total Debits:</span>
        <span>{totalDebits.toLocaleString()}</span>
      </div>
      <div className="flex justify-between mt-2">
        <span className="font-medium">Total Credits:</span>
        <span>{totalCredits.toLocaleString()}</span>
      </div>
      <div className="flex justify-between mt-2">
        <span className="font-medium">Ending Balance:</span>
        <span>{balance.toLocaleString()}</span>
      </div>
    </div>
  );
};

export default LedgerTable;
