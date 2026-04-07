import { useState } from "react";
import Navbar from "../components/Navbar";
import Stats from "../components/Stats";
import EmailForm from "../components/EmailForm";
import ResultCard from "../components/ResultCard";
import History from "./History";

export default function Dashboard() {
  const [result, setResult] = useState(null);

  return (
    <div>
      <Navbar />

      <div className="container mt-4">
        <Stats />
        <EmailForm setResult={setResult} />
        <ResultCard result={result} />
        <History />
      </div>
    </div>
  );
}