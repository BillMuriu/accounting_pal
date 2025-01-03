import React from "react";
import { Document, Page, Text, View, StyleSheet } from "@react-pdf/renderer";

const TrialBalancePDF = ({ startDate, endDate, transformedData }) => {
  return (
    <Document>
      <Page size="A4" style={styles.page}>
        <Text style={styles.mainTitle}>
          Trial Balance Report ({startDate} to {endDate})
        </Text>

        {/* Opening Balances Table */}
        <Text style={styles.sectionTitle}>Opening Balances</Text>
        <View style={styles.table}>
          <View style={styles.tableRow}>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Account
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Debits
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Credits
            </Text>
          </View>
          {transformedData.openingBalances.length > 0 ? (
            transformedData.openingBalances.map((row, index) => (
              <View
                key={index}
                style={[
                  styles.tableRow,
                  index % 2 === 0 ? styles.evenRow : styles.oddRow,
                ]}
              >
                <Text style={[styles.tableCell, styles.flex1]}>
                  {row.description}
                </Text>
                <Text style={[styles.tableCell, styles.flex1, styles.debit]}>
                  {row.debits}
                </Text>
                <Text style={[styles.tableCell, styles.flex1, styles.credit]}>
                  {row.credits}
                </Text>
              </View>
            ))
          ) : (
            <Text style={styles.tableCell}>No opening balances available</Text>
          )}
        </View>

        {/* Closing Balances Table */}
        <Text style={styles.sectionTitle}>Closing Balances</Text>
        <View style={styles.table}>
          <View style={styles.tableRow}>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Account
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Debits
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Credits
            </Text>
          </View>
          {transformedData.closingBalances.length > 0 ? (
            transformedData.closingBalances.map((row, index) => (
              <View
                key={index}
                style={[
                  styles.tableRow,
                  index % 2 === 0 ? styles.evenRow : styles.oddRow,
                ]}
              >
                <Text style={[styles.tableCell, styles.flex1]}>
                  {row.description}
                </Text>
                <Text style={[styles.tableCell, styles.flex1, styles.debit]}>
                  {row.debits}
                </Text>
                <Text style={[styles.tableCell, styles.flex1, styles.credit]}>
                  {row.credits}
                </Text>
              </View>
            ))
          ) : (
            <Text style={styles.tableCell}>No closing balances available</Text>
          )}
        </View>

        {/* Other Accounts Table */}
        <Text style={styles.sectionTitle}>Other Accounts</Text>
        <View style={styles.table}>
          <View style={styles.tableRow}>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Account
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Debits
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Credits
            </Text>
          </View>
          {transformedData.others.length > 0 ? (
            transformedData.others.map((row, index) => (
              <View
                key={index}
                style={[
                  styles.tableRow,
                  index % 2 === 0 ? styles.evenRow : styles.oddRow,
                ]}
              >
                <Text style={[styles.tableCell, styles.flex1]}>
                  {row.description}
                </Text>
                <Text style={[styles.tableCell, styles.flex1, styles.debit]}>
                  {row.debits}
                </Text>
                <Text style={[styles.tableCell, styles.flex1, styles.credit]}>
                  {row.credits}
                </Text>
              </View>
            ))
          ) : (
            <Text style={styles.tableCell}>No other accounts available</Text>
          )}
        </View>

        {/* Totals Table */}
        <Text style={styles.sectionTitle}>Totals</Text>
        <View style={styles.table}>
          <View style={styles.tableRow}>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Account
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Debits
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Credits
            </Text>
          </View>
          <View style={styles.tableRow}>
            <Text style={[styles.tableCell, styles.flex1, styles.bold]}>
              Total
            </Text>
            <Text style={[styles.tableCell, styles.flex1, styles.debit]}>
              {transformedData.totalDebits}
            </Text>
            <Text style={[styles.tableCell, styles.flex1, styles.credit]}>
              {transformedData.totalCredits}
            </Text>
          </View>
        </View>
        {/* <Text style={styles.summaryTitle}>Summary</Text>
        <View style={styles.summary}>
          <Text style={styles.summaryText}>
            Total Debits: {transformedData.totalDebits}
          </Text>
          <Text style={styles.summaryText}>
            Total Credits: {transformedData.totalCredits}
          </Text>
        </View> */}
      </Page>
    </Document>
  );
};

// Updated styles
const styles = StyleSheet.create({
  page: {
    padding: 30,
    backgroundColor: "#f0f0f0",
  },
  mainTitle: {
    fontSize: 18,
    marginBottom: 20,
    color: "#333",
    textAlign: "center",
  },
  sectionTitle: {
    fontSize: 12, // Reduced font size for subtitles
    fontWeight: "bold",
    color: "#2F4F4F",
    marginVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: "#B0BEC5",
    paddingBottom: 4,
    textAlign: "center",
  },
  table: {
    display: "table",
    width: "100%",
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: "#e0e0e0",
    borderRadius: 10,
    overflow: "hidden",
    marginBottom: 15,
  },
  tableRow: {
    flexDirection: "row",
  },
  tableColHeader: {
    padding: 8,
    backgroundColor: "#B0BEC5",
    borderStyle: "solid",
    borderColor: "#B0BEC5",
    borderWidth: 1,
    fontSize: 10,
    fontWeight: "bold",
    color: "#607D8B",
    textAlign: "center",
  },
  tableCell: {
    padding: 8,
    fontSize: 10,
    borderStyle: "solid",
    borderColor: "#dddddd",
    borderWidth: 1,
    textAlign: "left",
    color: "#212121",
  },
  debit: {
    color: "#F44336",
  },
  credit: {
    color: "#4CAF50",
  },
  flex1: {
    flex: 1,
  },
  oddRow: {
    backgroundColor: "#f7f7f7",
  },
  evenRow: {
    backgroundColor: "#fff",
  },
  bold: {
    fontWeight: "bold",
  },
  summaryTitle: {
    fontSize: 14,
    fontWeight: "bold",
    color: "#2F4F4F",
    marginTop: 10,
    textAlign: "center",
  },
  summary: {
    marginTop: 5,
    padding: 10,
    borderWidth: 1,
    borderColor: "#ddd",
    borderRadius: 5,
    backgroundColor: "#f7f7f7",
  },
  summaryText: {
    fontSize: 10,
    marginBottom: 4,
    color: "#212121",
  },
});

export default TrialBalancePDF;
