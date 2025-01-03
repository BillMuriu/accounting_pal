import React from "react";
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

const CashBookFormComponent = ({ onSubmit, defaultValues }) => {
  const form = useForm({
    resolver: zodResolver(formSchema),
    defaultValues,
  });

  const {
    handleSubmit,
    control,
    formState: { errors },
  } = form;

  return (
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
                    {[...Array(12)].map((_, i) => (
                      <SelectItem key={i + 1} value={(i + 1).toString()}>
                        {new Date(0, i).toLocaleString("default", {
                          month: "long",
                        })}
                      </SelectItem>
                    ))}
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
  );
};

export default CashBookFormComponent;
