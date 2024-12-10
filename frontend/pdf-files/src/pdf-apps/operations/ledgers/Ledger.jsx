"use client";

import React, { useState } from "react";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { format } from "date-fns";
import { CalendarIcon } from "lucide-react";
import { useForm } from "react-hook-form";

import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

const formSchema = z.object({
  start_date: z.date({
    required_error: "Start date is required.",
  }),
  end_date: z.date({
    required_error: "End date is required.",
  }),
});

const Ledger = () => {
  const [loading, setLoading] = useState(false);
  const [ledgerData, setLedgerData] = useState(null);

  const form = useForm({
    resolver: zodResolver(formSchema),
    defaultValues: {
      start_date: undefined,
      end_date: undefined,
    },
  });

  const onSubmit = async (values) => {
    setLoading(true);
    try {
      const formattedStartDate = format(values.start_date, "yyyy-MM-dd");
      const formattedEndDate = format(values.end_date, "yyyy-MM-dd");

      const response = await fetch(
        `http://127.0.0.1:8000/api/operations-ledgers/rmi-ledger/?start_date=${formattedStartDate}&end_date=${formattedEndDate}`
      );
      const data = await response.json();
      setLedgerData(data.ledger);
    } catch (error) {
      console.error("Error fetching ledger:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center flex-col h-full w-screen">
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="max-w-md w-full flex flex-col lg:flex-row lg:gap-6 gap-4"
        >
          {/* Start Date */}
          <FormField
            control={form.control}
            name="start_date"
            render={({ field }) => (
              <FormItem className="flex-1">
                <FormLabel>Start Date</FormLabel>
                <Popover>
                  <PopoverTrigger asChild>
                    <FormControl>
                      <Button
                        variant="outline"
                        className="w-full pl-3 text-left font-normal"
                      >
                        {field.value ? (
                          format(field.value, "PPP")
                        ) : (
                          <span>Pick a start date</span>
                        )}
                        <CalendarIcon className="ml-auto h-4 w-4 opacity-50" />
                      </Button>
                    </FormControl>
                  </PopoverTrigger>
                  <PopoverContent align="start">
                    <Calendar
                      mode="single"
                      selected={field.value}
                      onSelect={field.onChange}
                      disabled={(date) => date > new Date()}
                      initialFocus
                    />
                  </PopoverContent>
                </Popover>
                <FormMessage />
              </FormItem>
            )}
          />
          {/* End Date */}
          <FormField
            control={form.control}
            name="end_date"
            render={({ field }) => (
              <FormItem className="flex-1">
                <FormLabel>End Date</FormLabel>
                <Popover>
                  <PopoverTrigger asChild>
                    <FormControl>
                      <Button
                        variant="outline"
                        className="w-full pl-3 text-left font-normal"
                      >
                        {field.value ? (
                          format(field.value, "PPP")
                        ) : (
                          <span>Pick an end date</span>
                        )}
                        <CalendarIcon className="ml-auto h-4 w-4 opacity-50" />
                      </Button>
                    </FormControl>
                  </PopoverTrigger>
                  <PopoverContent align="start">
                    <Calendar
                      mode="single"
                      selected={field.value}
                      onSelect={field.onChange}
                      disabled={(date) => date > new Date()}
                      initialFocus
                    />
                  </PopoverContent>
                </Popover>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit" className="w-full lg:w-auto" disabled={loading}>
            {loading ? "Loading..." : "Submit"}
          </Button>
        </form>
      </Form>

      {ledgerData && (
        <div className="mt-6 w-full max-w-4xl">
          <h2 className="text-xl font-bold mb-4">Ledger Summary</h2>

          {/* Credits Section */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold mb-2">Credits</h3>
            <table className="min-w-full table-auto border-collapse">
              <thead>
                <tr>
                  <th className="px-4 py-2 text-left border-b">Date</th>
                  <th className="px-4 py-2 text-left border-b">Amount</th>
                  <th className="px-4 py-2 text-left border-b">Cashbook</th>
                </tr>
              </thead>
              <tbody>
                {ledgerData.credits.map((credit, index) => (
                  <tr key={index}>
                    <td className="px-4 py-2">
                      {format(new Date(credit.date), "MM/dd/yyyy")}
                    </td>
                    <td className="px-4 py-2">
                      {credit.amount.toLocaleString()}
                    </td>
                    <td className="px-4 py-2">{credit.cashbook}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Debits Section */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold mb-2">Debits</h3>
            <table className="min-w-full table-auto border-collapse">
              <thead>
                <tr>
                  <th className="px-4 py-2 text-left border-b">Date</th>
                  <th className="px-4 py-2 text-left border-b">Amount</th>
                  <th className="px-4 py-2 text-left border-b">Cashbook</th>
                </tr>
              </thead>
              <tbody>
                {ledgerData.debits.map((debit, index) => (
                  <tr key={index}>
                    <td className="px-4 py-2">
                      {format(new Date(debit.date), "MM/dd/yyyy")}
                    </td>
                    <td className="px-4 py-2">
                      {debit.amount.toLocaleString()}
                    </td>
                    <td className="px-4 py-2">{debit.cashbook}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Totals Section */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold">Totals</h3>
            <div className="flex justify-between mt-2">
              <span className="font-medium">Total Credits:</span>
              <span>{ledgerData.total_credits.toLocaleString()}</span>
            </div>
            <div className="flex justify-between mt-2">
              <span className="font-medium">Total Debits:</span>
              <span>{ledgerData.total_debits.toLocaleString()}</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Ledger;
