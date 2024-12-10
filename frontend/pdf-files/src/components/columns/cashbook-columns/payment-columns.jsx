export const paymentsColumns = [
  {
    accessorKey: "type",
    header: "Type",
    cell: ({ row }) => {
      const type = row.original.type;
      return type.charAt(0).toUpperCase() + type.slice(1);
    },
  },
  {
    accessorKey: "voucher_no",
    header: "Voucher No.",
    cell: ({ row }) => row.original.voucher_no || "-",
  },
  {
    accessorKey: "cheque_no",
    header: "Cheque No.",
    cell: ({ row }) => row.original.cheque_no || "-",
  },
  {
    accessorKey: "cash",
    header: "Cash (KSh)",
    cell: ({ row }) =>
      row.original.cash ? row.original.cash.toLocaleString() : "-",
  },
  {
    accessorKey: "bank",
    header: "Bank (KSh)",
    cell: ({ row }) =>
      row.original.bank ? row.original.bank.toLocaleString() : "-",
  },
  {
    accessorKey: "bank_charge",
    header: "Bank Charge (KSh)",
    cell: ({ row }) =>
      row.original.bank_charge
        ? row.original.bank_charge.toLocaleString()
        : "-",
  },
  {
    accessorKey: "description",
    header: "Description",
    cell: ({ row }) => row.original.description || "-",
  },
  {
    accessorKey: "date",
    header: "Date",
    cell: ({ row }) => {
      const date = new Date(row.original.date);
      return date.toLocaleDateString("en-US", {
        year: "2-digit",
        month: "2-digit",
        day: "2-digit",
      }); // Formats as mm/dd/yy
    },
  },
];
