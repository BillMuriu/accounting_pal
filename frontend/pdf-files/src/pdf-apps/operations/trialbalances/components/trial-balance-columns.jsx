"use client";

import clsx from "clsx";

export const trialBalanceColumns = [
  {
    accessorKey: "debits",
    header: "Debits",
    cell: ({ getValue, row }) => {
      const value = parseFloat(getValue() || 0);

      // Check if the row corresponds to "Total Debits"
      const isTotalDebits =
        row.original.debits &&
        row.original.debits.hasOwnProperty("Total Debits");

      return (
        <span
          className={clsx(
            "text-sm",
            isTotalDebits && "font-bold text-red-600" // Apply style if it's "Total Debits"
          )}
        >
          {value > 0 ? value.toLocaleString("en-KE") : "-"}
        </span>
      );
    },
  },
  {
    accessorKey: "credits",
    header: "Credits",
    cell: ({ getValue, row }) => {
      const value = parseFloat(getValue() || 0);

      // Check if the row corresponds to "Total Credits"
      const isTotalCredits =
        row.original.credits &&
        row.original.credits.hasOwnProperty("Total Credits");

      return (
        <span
          className={clsx(
            "text-sm",
            isTotalCredits && "font-bold text-green-600" // Apply style if it's "Total Credits"
          )}
        >
          {value > 0 ? value.toLocaleString("en-KE") : "-"}
        </span>
      );
    },
  },
];
