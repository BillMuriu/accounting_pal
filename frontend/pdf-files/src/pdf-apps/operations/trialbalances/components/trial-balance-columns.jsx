"use client";

import clsx from "clsx";

export const trialBalanceColumns = [
  {
    accessorKey: "description",
    header: "Account",
    cell: ({ getValue }) => {
      const accountName = getValue();
      return <span className="text-sm">{accountName}</span>;
    },
    width: "30%", // Make the account column wide enough for names
  },
  {
    accessorKey: "debits",
    header: "Debits",
    cell: ({ getValue }) => {
      const value = parseFloat(getValue() || 0);
      const isPositive = value > 0;
      return (
        <span
          className={clsx(
            "text-sm",
            isPositive ? "text-green-600" : "text-red-600"
          )}
        >
          {value !== 0 ? value.toLocaleString("en-KE") : "-"}
        </span>
      );
    },
    width: "25%", // Fixed width for Debits column
  },
  {
    accessorKey: "credits",
    header: "Credits",
    cell: ({ getValue }) => {
      const value = parseFloat(getValue() || 0);
      const isPositive = value > 0;
      return (
        <span
          className={clsx(
            "text-sm",
            isPositive ? "text-blue-600" : "text-gray-600"
          )}
        >
          {value !== 0 ? value.toLocaleString("en-KE") : "-"}
        </span>
      );
    },
    width: "25%", // Fixed width for Credits column
  },
];
