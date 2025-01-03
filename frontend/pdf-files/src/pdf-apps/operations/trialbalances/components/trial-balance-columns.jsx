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
  },
  {
    accessorKey: "debits",
    header: "Debits",
    cell: ({ getValue }) => {
      const value = parseFloat(getValue() || 0);
      return (
        <span className="text-sm">
          {value !== 0 ? value.toLocaleString("en-KE") : "-"}
        </span>
      );
    },
  },
  {
    accessorKey: "credits",
    header: "Credits",
    cell: ({ getValue }) => {
      const value = parseFloat(getValue() || 0);
      return (
        <span className="text-sm">
          {value !== 0 ? value.toLocaleString("en-KE") : "-"}
        </span>
      );
    },
  },
];
