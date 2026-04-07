import { useEffect, useState } from "react";
import api from "../services/api";

export default function Stats() {
  const [stats, setStats] = useState({});

  useEffect(() => {
    api.get("stats/").then(res => setStats(res.data));
  }, []);

  return (
    <div className="row mt-3">
      <div className="col-md-4">
        <div className="card text-center p-3 shadow">
          <h5>Total</h5>
          <h3>{stats.total}</h3>
        </div>
      </div>

      <div className="col-md-4">
        <div className="card text-center p-3 shadow bg-danger text-white">
          <h5>Phishing</h5>
          <h3>{stats.phishing}</h3>
        </div>
      </div>

      <div className="col-md-4">
        <div className="card text-center p-3 shadow bg-success text-white">
          <h5>Safe</h5>
          <h3>{stats.safe}</h3>
        </div>
      </div>
    </div>
  );
}