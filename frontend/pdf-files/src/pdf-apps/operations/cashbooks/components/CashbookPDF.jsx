import React from "react";
import { Document, Page, Text, View, StyleSheet } from "@react-pdf/renderer";

const CashbookPDF = ({ month, year, cashbookData }) => (
  <Document>
    {/* Receipts Page */}
    <Page size="A4" style={styles.page}>
      <Text style={styles.title}>
        Cashbook Report - Receipts ({month}/{year})
      </Text>

      <View style={styles.table}>
        {/* Table Header */}
        <View style={styles.tableRow}>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            From
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Receipt No
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Cash
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Bank
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            RMI
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex2]}>
            Other Voteheads
          </Text>
        </View>

        {/* Table Rows */}
        {cashbookData.receipts.map((receipt, index) => (
          <View
            key={index}
            style={[
              styles.tableRow,
              index % 2 === 0 ? styles.evenRow : styles.oddRow, // Alternate row colors
            ]}
          >
            <Text style={[styles.tableCell, styles.flex1]}>
              {receipt.from_whom}
            </Text>
            <Text style={[styles.tableCell, styles.flex1]}>
              {receipt.receipt_no}
            </Text>
            <Text style={[styles.tableCell, styles.flex1]}>{receipt.cash}</Text>
            <Text style={[styles.tableCell, styles.flex1]}>{receipt.bank}</Text>
            <Text style={[styles.tableCell, styles.flex1]}>{receipt.rmi}</Text>
            <Text style={[styles.tableCell, styles.flex2]}>
              {receipt.other_voteheads}
            </Text>
          </View>
        ))}
      </View>
    </Page>

    {/* Payments Page */}
    <Page size="A4" style={styles.page}>
      <Text style={styles.title}>
        Cashbook Report - Payments ({month}/{year})
      </Text>

      <View style={styles.table}>
        {/* Table Header */}
        <View style={styles.tableRow}>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Type
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Voucher No
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Cheque No
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Cash
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Bank
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Bank Charge
          </Text>
          <Text style={[styles.tableCell, styles.tableColHeader, styles.flex1]}>
            Date
          </Text>
        </View>

        {/* Table Rows */}
        {cashbookData.payments.map((payment, index) => (
          <View
            key={index}
            style={[
              styles.tableRow,
              index % 2 === 0 ? styles.evenRow : styles.oddRow, // Alternate row colors
            ]}
          >
            <Text style={[styles.tableCell, styles.flex1]}>{payment.type}</Text>
            <Text style={[styles.tableCell, styles.flex1]}>
              {payment.voucher_no}
            </Text>
            <Text style={[styles.tableCell, styles.flex1]}>
              {payment.cheque_no}
            </Text>
            <Text style={[styles.tableCell, styles.flex1]}>{payment.cash}</Text>
            <Text style={[styles.tableCell, styles.flex1]}>{payment.bank}</Text>
            <Text style={[styles.tableCell, styles.flex1]}>
              {payment.bank_charge}
            </Text>
            <Text style={[styles.tableCell, styles.flex1]}>
              {new Date(payment.date).toLocaleDateString()}
            </Text>
          </View>
        ))}
      </View>
    </Page>
  </Document>
);

// PDF styles
const styles = StyleSheet.create({
  page: {
    padding: 30,
    backgroundColor: "#f0f0f0", // Light background for the entire page
  },
  title: {
    fontSize: 18,
    marginBottom: 20,
    color: "#333", // Dark title color
    textAlign: "center",
  },
  table: {
    display: "table",
    width: "100%", // Ensure table takes full width
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: "#e0e0e0",
    borderRadius: 10, // Rounded corners for the table
    overflow: "hidden",
  },
  tableRow: {
    flexDirection: "row",
  },
  tableColHeader: {
    padding: 10,
    backgroundColor: "#4CAF50", // Bold green background for headers
    borderStyle: "solid",
    borderColor: "#388E3C",
    borderWidth: 1,
    fontSize: 12,
    fontWeight: "bold",
    color: "#ffffff", // White text for the header
    textAlign: "center",
  },
  tableCell: {
    padding: 10,
    fontSize: 10,
    borderStyle: "solid",
    borderColor: "#dddddd",
    borderWidth: 1,
    textAlign: "left",
    color: "#212121", // Darker text color for better readability
  },
  flex1: {
    flex: 1, // Make sure all columns have equal width except special ones
  },
  flex2: {
    flex: 2, // This will make "Other Voteheads" column wider
  },
  oddRow: {
    backgroundColor: "#f7f7f7", // Light gray background for odd rows
  },
  evenRow: {
    backgroundColor: "#fff", // White background for even rows
  },
});

export default CashbookPDF;
