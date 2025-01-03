import React from "react";
import { HashRouter as Router, Route, Routes, Link } from "react-router-dom";
import CashBook from "./pdf-apps/operations/cashbooks/Cash-book";
import Ledger from "./pdf-apps/operations/ledgers/Ledger";
import TrialBalance from "./pdf-apps/operations/trialbalances/trial-balance";
import Home from "./Home";

const App = () => {
  return (
    <Router>
      <div className="min-h-screen flex flex-col overflow-x-hidden">
        {" "}
        {/* Prevent horizontal overflow globally */}
        {/* Main Content */}
        <div className="flex-grow bg-gray-50 p-4">
          <Routes>
            <Route path="/operations-cashbook-pdfs" element={<CashBook />} />
            <Route path="/home" element={<Home />} />
            <Route path="/operations-ledger" element={<Ledger />} />
            <Route
              path="/operations-trial-balance"
              element={<TrialBalance />}
            />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
