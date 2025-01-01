import React from "react";
import { Document, Page, Text, View, StyleSheet } from "@react-pdf/renderer";

const LedgerPDF = ({ month, year, ledgerData }) => (
  <Document>
    {Object.entries(ledgerData).map(([ledgerName, entries], index) => (
      <Page size="A4" style={styles.page} key={index}>
        <Text style={styles.title}>
          Ledger Report - {ledgerName} ({month}/{year})
        </Text>

        <View style={styles.table}>
          {/* Table Header */}
          <View style={styles.tableRow}>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex1]}
            >
              Date
            </Text>
            <Text
              style={[styles.tableCell, styles.tableColHeader, styles.flex2]}
            >
              Cashbook
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

          {/* Table Rows */}
          {entries.map((entry, rowIndex) => (
            <View
              key={rowIndex}
              style={[
                styles.tableRow,
                rowIndex % 2 === 0 ? styles.evenRow : styles.oddRow,
              ]}
            >
              <Text style={[styles.tableCell, styles.flex1]}>
                {entry.date || "-"}
              </Text>
              <Text style={[styles.tableCell, styles.flex2]}>
                {entry.cashbook || "-"}
              </Text>
              <Text style={[styles.tableCell, styles.flex1]}>
                {entry.debits || 0}
              </Text>
              <Text style={[styles.tableCell, styles.flex1]}>
                {entry.credits || 0}
              </Text>
            </View>
          ))}
        </View>
      </Page>
    ))}
  </Document>
);

const styles = StyleSheet.create({
  page: {
    padding: 30,
    backgroundColor: "#f0f0f0",
  },
  title: {
    fontSize: 18,
    marginBottom: 20,
    color: "#333",
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
  },
  tableRow: {
    flexDirection: "row",
  },
  tableColHeader: {
    padding: 10,
    backgroundColor: "#3f51b5", // Blue background for headers
    borderStyle: "solid",
    borderColor: "#303f9f",
    borderWidth: 1,
    fontSize: 12,
    fontWeight: "bold",
    color: "#ffffff",
    textAlign: "center",
  },
  tableCell: {
    padding: 10,
    fontSize: 10,
    borderStyle: "solid",
    borderColor: "#dddddd",
    borderWidth: 1,
    textAlign: "left",
    color: "#212121",
  },
  flex1: {
    flex: 1,
  },
  flex2: {
    flex: 2,
  },
  oddRow: {
    backgroundColor: "#f7f7f7",
  },
  evenRow: {
    backgroundColor: "#fff",
  },
});

export default LedgerPDF;
