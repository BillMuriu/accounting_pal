"use client";

import { format } from "date-fns";
import clsx from "clsx";

export const rmiLedgerColumns = [
  {
    accessorKey: "cashbook",
    header: "Cashbook",
    cell: ({ getValue, row }) => (
      <span
        className={clsx(
          "text-sm",
          row.original.cashbook?.includes("Total Debits") &&
            "font-bold text-red-600",
          row.original.cashbook?.includes("Total Credits") &&
            "font-bold text-green-600"
        )}
      >
        {getValue() || "-"}
      </span>
    ),
  },
  {
    accessorKey: "debits",
    header: "Debit (KES)",
    cell: ({ getValue, row }) => {
      const value = parseFloat(getValue() || 0);
      return (
        <span
          className={clsx(
            "text-sm",
            row.original.cashbook?.includes("Total Debits") &&
              "font-bold text-red-600",
            row.original.cashbook?.includes("Total Credits") &&
              "font-bold text-green-600"
          )}
        >
          {value > 0 ? value.toLocaleString("en-KE") : "-"}
        </span>
      );
    },
  },
  {
    accessorKey: "credits",
    header: "Credit (KES)",
    cell: ({ getValue, row }) => {
      const value = parseFloat(getValue() || 0);
      return (
        <span
          className={clsx(
            "text-sm",
            row.original.cashbook?.includes("Total Debits") &&
              "font-bold text-red-600",
            row.original.cashbook?.includes("Total Credits") &&
              "font-bold text-green-600"
          )}
        >
          {value > 0 ? value.toLocaleString("en-KE") : "-"}
        </span>
      );
    },
  },
  {
    accessorKey: "date",
    header: "Date",
    cell: ({ getValue, row }) => {
      const date = getValue();
      return (
        <span
          className={clsx(
            "text-sm",
            row.original.cashbook?.includes("Total Debits") && "text-gray-500",
            row.original.cashbook?.includes("Total Credits") && "text-gray-500"
          )}
        >
          {date ? format(new Date(date), "MM/dd/yyyy") : "-"}
        </span>
      );
    },
  },
];
