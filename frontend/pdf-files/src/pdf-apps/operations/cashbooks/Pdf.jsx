import React, { useState } from "react";
import * as z from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "@/components/ui/input";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
} from "@/components/ui/form";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Button } from "@/components/ui/button";
import { PDFDownloadLink } from "@react-pdf/renderer";
import CashbookPDF from "./components/CashbookPDF";
import { ReceiptsDataTable } from "@/components/tables/receipts-table";
import { receiptsColumns } from "@/components/columns/cashbook-columns/receipt-columns";
import { paymentsColumns } from "@/components/columns/cashbook-columns/payment-columns";

// Schema for validation
const formSchema = z.object({
  month: z
    .string()
    .min(1, "Month must be between 1 and 12")
    .max(2, "Month must be between 1 and 12")
    .regex(
      /^(0?[1-9]|1[0-2])$/,
      "Month must be a valid number between 1 and 12"
    ),
  year: z
    .string()
    .min(4, "Year must be at least 4 digits")
    .max(4, "Year must be exactly 4 digits")
    .regex(/^\d{4}$/, "Year must be a valid 4-digit number"),
});

const CashBookForm = () => {
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState(null);
  const [cashbookData, setCashbookData] = useState({
    receipts: [],
    payments: [],
  });

  const currentMonth = new Date().getMonth() + 1;
  const currentYear = new Date().getFullYear();

  const form = useForm({
    resolver: zodResolver(formSchema),
    defaultValues: {
      month: currentMonth.toString(),
      year: currentYear.toString(),
    },
  });

  const {
    handleSubmit,
    control,
    formState: { errors },
    setValue,
    trigger,
  } = form;

  const onSubmit = (values) => {
    const parsedData = {
      month: Number(values.month),
      year: Number(values.year),
    };

    setFormData(parsedData);
    fetchCashbooks(parsedData.year, parsedData.month);
  };

  const fetchCashbooks = async (year, month) => {
    setLoading(true);
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/operations-cashbooks/cashbook/?year=${year}&month=${month}`
      );
      const data = await response.json();
      setCashbookData(data);
    } catch (error) {
      console.error("Error fetching cashbooks:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center flex-col h-full w-screen">
      <Form {...form}>
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="max-w-md w-full flex flex-col gap-4"
        >
          {/* Month Select */}
          <FormField
            control={control}
            name="month"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Month</FormLabel>
                <FormControl>
                  <Select {...field} onValueChange={field.onChange}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select month" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="1">January</SelectItem>
                      <SelectItem value="2">February</SelectItem>
                      <SelectItem value="3">March</SelectItem>
                      <SelectItem value="4">April</SelectItem>
                      <SelectItem value="5">May</SelectItem>
                      <SelectItem value="6">June</SelectItem>
                      <SelectItem value="7">July</SelectItem>
                      <SelectItem value="8">August</SelectItem>
                      <SelectItem value="9">September</SelectItem>
                      <SelectItem value="10">October</SelectItem>
                      <SelectItem value="11">November</SelectItem>
                      <SelectItem value="12">December</SelectItem>
                    </SelectContent>
                  </Select>
                </FormControl>
                {errors.month && (
                  <p className="text-red-500 text-sm">{errors.month.message}</p>
                )}
              </FormItem>
            )}
          />
          {/* Year Field */}
          <FormField
            control={control}
            name="year"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Year</FormLabel>
                <FormControl>
                  <Input
                    {...field}
                    className="w-full"
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                </FormControl>
                {errors.year && (
                  <p className="text-red-500 text-sm">{errors.year.message}</p>
                )}
              </FormItem>
            )}
          />
          <Button type="submit" className="w-full">
            Submit
          </Button>
        </form>
      </Form>

      {loading && <p>Loading cashbooks...</p>}

      {formData &&
        (cashbookData.receipts.length > 0 ||
          cashbookData.payments.length > 0) && (
          <Button className="mt-4">
            <PDFDownloadLink
              document={
                <CashbookPDF
                  month={formData.month}
                  year={formData.year}
                  cashbookData={cashbookData}
                />
              }
              fileName={`cashbook_${formData.month}_${formData.year}.pdf`}
            >
              {({ loading }) =>
                loading ? "Preparing document..." : "Download Cashbook PDF"
              }
            </PDFDownloadLink>
          </Button>
        )}

      {!loading &&
        (cashbookData.receipts.length > 0 ||
          cashbookData.payments.length > 0) && (
          <div className="mt-6 w-full max-w-4xl">
            {cashbookData.receipts.length > 0 && (
              <>
                <h2 className="text-lg font-bold mb-4">Receipts</h2>
                <ReceiptsDataTable
                  columns={receiptsColumns}
                  data={cashbookData.receipts}
                />
              </>
            )}

            {cashbookData.payments.length > 0 && (
              <>
                <h2 className="text-lg font-bold mt-8 mb-4">Payments</h2>
                <ReceiptsDataTable
                  columns={paymentsColumns}
                  data={cashbookData.payments}
                />
              </>
            )}
          </div>
        )}
    </div>
  );
};

export default CashBookForm;
