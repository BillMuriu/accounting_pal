import { format } from "date-fns";
import clsx from "clsx";

export const rmiLedgerColumns = [
  {
    accessorKey: "cashbook",
    header: "Ref-cashbook",
    cell: ({ getValue, row }) => {
      return (
        <span
          className={clsx(
            "text-sm",
            row.original.cashbook === "Totals" && "font-bold" // Apply bold for Totals row
          )}
        >
          {getValue()}
        </span>
      );
    },
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
            row.original.cashbook === "Totals" && "font-bold", // Apply bold for Totals row
            row.original.cashbook === "Totals" && value > 0 && "text-red-600" // Apply red for positive debits in Totals row
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
            row.original.cashbook === "Totals" && "font-bold", // Apply bold for Totals row
            row.original.cashbook === "Totals" && value > 0 && "text-green-600" // Apply green for positive credits in Totals row
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
      const formattedDate =
        date && !isNaN(new Date(date))
          ? format(new Date(date), "MM/dd/yyyy")
          : "-"; // Handle invalid or missing dates
      return (
        <span
          className={clsx(
            "text-sm",
            row.original.cashbook === "Totals" && "text-gray-500" // Style the date for Totals row
          )}
        >
          {formattedDate}
        </span>
      );
    },
  },
];
