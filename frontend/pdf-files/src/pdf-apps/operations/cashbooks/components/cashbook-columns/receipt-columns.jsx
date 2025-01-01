"use client";

import { Badge } from "@/components/ui/badge";
import { format } from "date-fns";

export const receiptsColumns = [
  {
    accessorKey: "from_whom",
    header: ({ column }) => <div className="text-left">From Whom</div>,
    cell: ({ getValue }) => {
      const rawValue = getValue();
      const formattedValue = rawValue
        .replace(/_/g, " ") // Replace underscores with spaces
        .replace(/\b\w/g, (char) => char.toUpperCase()); // Capitalize each word

      // Check for Inter Account Borrowing
      const iabValues = ["rmi", "school_fund", "tuition", "pettycash"];
      const isIAB = iabValues.includes(rawValue);

      // Check for Petty Cash
      const isPettyCash = rawValue === "Petty Cash";

      // Check for Balance Carried Forward
      const isBalanceCarriedForward = rawValue === "Balance Carried Forward";

      return (
        <div className="flex items-center space-x-2">
          {isIAB && (
            <Badge
              variant="outline"
              className="border-blue-500 bg-blue-100 text-blue-500 flex items-center justify-center"
            >
              IAB- {formattedValue} {/* Add "IAB-" prefix to the value */}
            </Badge>
          )}
          {isPettyCash && !isIAB && (
            <Badge
              variant="outline"
              className="border-purple-500 bg-purple-100 text-purple-500 flex items-center justify-center"
            >
              {formattedValue} {/* For pettycash, just show the value */}
            </Badge>
          )}
          {isBalanceCarriedForward && (
            <Badge
              variant="outline"
              className="border-gray-500 bg-gray-100 text-gray-500 flex items-center justify-center"
            >
              {formattedValue}{" "}
              {/* Wrap the value in the badge for Balance Carried Forward */}
            </Badge>
          )}
          {/* Default badge for other values (if applicable) */}
          {!isIAB && !isPettyCash && !isBalanceCarriedForward && (
            <span className="text-sm">{formattedValue}</span>
          )}
        </div>
      );
    },
  },

  {
    accessorKey: "receipt_no",
    header: "Receipt No",
  },
  {
    accessorKey: "cash",
    header: "Cash (KES)",
    cell: ({ getValue }) =>
      parseFloat(getValue().replace(/,/g, "")).toLocaleString("en-KE"),
  },
  {
    accessorKey: "bank",
    header: "Bank (KES)",
    cell: ({ getValue }) =>
      parseFloat(getValue().replace(/,/g, "")).toLocaleString("en-KE"),
  },
  {
    accessorKey: "rmi",
    header: "RMI",
    cell: ({ getValue }) => {
      const value = getValue();
      return (
        <span className="text-sm">
          {value === "-" ? "-" : parseFloat(value).toLocaleString("en-KE")}
        </span>
      );
    },
  },

  {
    accessorKey: "other_voteheads",
    header: "Other Voteheads",
    cell: ({ getValue }) => {
      const value = getValue();
      return <span className="text-sm">{value}</span>;
    },
  },
  {
    accessorKey: "date",
    header: "Date",
    cell: ({ getValue }) => {
      const dateValue = getValue();
      const parsedDate = new Date(dateValue);

      // Check if the date is valid
      if (isNaN(parsedDate)) {
        return <span className="text-sm">Invalid Date</span>;
      }

      return format(parsedDate, "MM/dd/yyyy");
    },
  },
];
