// src/App.jsx
import React from "react";
import { HashRouter as Router, Route, Routes, Link } from "react-router-dom";
import Pdf from "./pdf-apps/operations/cashbooks/Pdf";
import Ledger from "./pdf-apps/operations/ledgers/Ledger";
import TrialBalance from "./pdf-apps/operations/trialbalances/trial-balance";
import Home from "./Home";

const App = () => {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/home">Home</Link>
          </li>
          <li>
            <Link to="/operations-cashbook-pdfs">Operations Cashbook PDFs</Link>
          </li>
          <li>
            <Link to="/operations-ledger">Operations Ledgers</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/operations-cashbook-pdfs" element={<Pdf />} />
        <Route path="/home" element={<Home />} />
        <Route path="/operations-ledger" element={<Ledger />} /> {/* Fixed */}
        <Route
          path="/operations-trial-balance"
          element={<TrialBalance />}
        />{" "}
        {/* Fixed */}
      </Routes>
    </Router>
  );
};

export default App;
