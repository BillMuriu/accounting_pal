import React, { useState } from "react";
import { PDFDownloadLink } from "@react-pdf/renderer";
import CashBookFormComponent from "./components/cash-book-form";
import CashbookPDF from "./components/CashbookPDF";
import { ReceiptsDataTable } from "@/components/tables/receipts-table";
import { receiptsColumns } from "./components/cashbook-columns/receipt-columns";
import { paymentsColumns } from "./components/cashbook-columns/payment-columns";
import { Button } from "@/components/ui/button";

const CashBook = () => {
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState(null);
  const [cashbookData, setCashbookData] = useState({
    receipts: [],
    payments: [],
  });

  const currentMonth = new Date().getMonth() + 1;
  const currentYear = new Date().getFullYear();

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

  const onSubmit = (values) => {
    const parsedData = {
      month: Number(values.month),
      year: Number(values.year),
    };

    setFormData(parsedData);
    fetchCashbooks(parsedData.year, parsedData.month);
  };

  return (
    <div className="flex items-center justify-center flex-col h-full w-screen">
      <CashBookFormComponent
        onSubmit={onSubmit}
        defaultValues={{
          month: currentMonth.toString(),
          year: currentYear.toString(),
        }}
      />

      {loading && <p>Loading cashbooks...</p>}

      {!loading &&
        formData &&
        (cashbookData.receipts.length > 0 ||
          cashbookData.payments.length > 0) && (
          <div className="relative mt-6 w-full max-w-4xl border border-gray-200 rounded-lg shadow-lg p-6 bg-white">
            {/* Title */}
            <div className="flex justify-between items-center mb-6">
              <h1 className="text-xl font-bold">Cashbook Details</h1>
              <Button>
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
            </div>

            {/* Receipts and Payments */}
            {cashbookData.receipts.length > 0 && (
              <div className="mb-8">
                <h2 className="text-lg font-bold mb-4">Receipts</h2>
                <ReceiptsDataTable
                  columns={receiptsColumns}
                  data={cashbookData.receipts}
                />
              </div>
            )}

            {cashbookData.payments.length > 0 && (
              <div>
                <h2 className="text-lg font-bold mb-4">Payments</h2>
                <ReceiptsDataTable
                  columns={paymentsColumns}
                  data={cashbookData.payments}
                />
              </div>
            )}
          </div>
        )}
    </div>
  );
};

export default CashBook;
