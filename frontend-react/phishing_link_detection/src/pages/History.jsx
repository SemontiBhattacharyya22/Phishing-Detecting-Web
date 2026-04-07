import { useEffect, useState } from "react";
import api from "../services/api";

export default function History() {
  const [data, setData] = useState([]);

  useEffect(() => {
    api.get("history/").then(res => setData(res.data));
  }, []);

  return (
    <div className="card p-3 shadow mt-3">
      <h4>History</h4>

      {data.map((item, i) => (
        <div key={i} className="border-bottom py-2">
          <p>{item.email}</p>
          <p className={
            item.prediction === "Phishing" ? "text-danger" : "text-success"
          }>
            {item.prediction}
          </p>
        </div>
      ))}
    </div>
  );
}