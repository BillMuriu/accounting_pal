import { Badge } from "@/components/ui/badge";

export const paymentsColumns = [
  {
    accessorKey: "type",
    header: "Type",
    cell: ({ row }) => {
      const type = row.original.type;

      // Function to format type (e.g., "bankcharge" → "Bank Charge")
      const formatType = (str) =>
        str
          .replace(/([a-z])([A-Z])/g, "$1 $2") // Add space between camelCase
          .replace(/_/g, " ") // Replace underscores with spaces
          .replace(/\b\w/g, (char) => char.toUpperCase()); // Capitalize each word

      const formattedType = formatType(type);

      // Badge colors
      const badgeColors = {
        pettycash: "border-purple-500 bg-purple-100 text-purple-500",
        paymentvoucher: "border-blue-500 bg-blue-100 text-blue-500",
        cheque: "border-green-500 bg-green-100 text-green-500",
        bankcharge: "border-orange-500 bg-orange-100 text-orange-500",
      };

      const badgeClass =
        badgeColors[type.toLowerCase()] ||
        "border-gray-500 bg-gray-100 text-gray-500";

      return (
        <div className="flex items-center space-x-2">
          <Badge
            variant="outline"
            className={`flex items-center justify-center ${badgeClass}`}
          >
            {formattedType}
          </Badge>
        </div>
      );
    },
  },
  {
    accessorKey: "voucher_no",
    header: "Voucher No.",
    cell: ({ row }) => (
      <span className="text-sm">{row.original.voucher_no || "-"}</span>
    ),
  },
  {
    accessorKey: "cheque_no",
    header: "Cheque No.",
    cell: ({ row }) => (
      <span className="text-sm">{row.original.cheque_no || "-"}</span>
    ),
  },
  {
    accessorKey: "cash",
    header: "Cash (KSh)",
    cell: ({ row }) => {
      const cash = row.original.cash;
      return cash ? (
        <div className="flex items-center space-x-2">
          <Badge
            variant="outline"
            className="border-yellow-500 bg-yellow-100 text-yellow-500 flex items-center justify-center"
          >
            {cash.toLocaleString()}
          </Badge>
        </div>
      ) : (
        "-"
      );
    },
  },
  {
    accessorKey: "bank",
    header: "Bank (KSh)",
    cell: ({ row }) => {
      const bank = row.original.bank;
      return bank ? (
        <div className="flex items-center space-x-2">
          <Badge
            variant="outline"
            className="border-green-500 bg-green-100 text-green-500 flex items-center justify-center"
          >
            {bank.toLocaleString()}
          </Badge>
        </div>
      ) : (
        "-"
      );
    },
  },
  {
    accessorKey: "bank_charge",
    header: "Bank Charge (KSh)",
    cell: ({ row }) => (
      <span className="text-sm">
        {row.original.bank_charge
          ? row.original.bank_charge.toLocaleString()
          : "-"}
      </span>
    ),
  },
  {
    accessorKey: "date",
    header: "Date",
    cell: ({ row }) => {
      const date = new Date(row.original.date);
      return (
        <span className="text-sm">
          {date.toLocaleDateString("en-US", {
            year: "2-digit",
            month: "2-digit",
            day: "2-digit",
          })}
        </span>
      );
    },
  },
  {
    accessorKey: "description",
    header: "Description",
    cell: ({ row }) => {
      const description = row.original.description || "-";
      const truncatedDescription = description
        .split(" ")
        .slice(0, 2)
        .join(" ")
        .concat(description.split(" ").length > 2 ? "..." : "");

      return <span className="text-sm">{truncatedDescription}</span>;
    },
  },
];
