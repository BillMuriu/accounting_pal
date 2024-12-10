"use client";

import { Button } from "@/components/ui/button";
import { ArrowUpDown } from "lucide-react";

export const receiptsColumns = [
  {
    accessorKey: "from_whom",
    header: "From Whom",
  },
  {
    accessorKey: "receipt_no",
    header: ({ column }) => (
      <Button
        variant="ghost"
        onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
      >
        Receipt No
        <ArrowUpDown className="ml-2 h-4 w-4" />
      </Button>
    ),
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
  },
  {
    accessorKey: "other_voteheads",
    header: "Other Voteheads",
  },
];
