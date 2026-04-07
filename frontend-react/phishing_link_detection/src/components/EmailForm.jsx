import { useState } from "react";
import api from "../services/api";

export default function EmailForm({ setResult }) {
  const [email, setEmail] = useState("");

  const handleScan = async () => {
    const res = await api.post("detect/", { email });
    setResult(res.data);
  };

  return (
    <div className="card p-3 shadow mt-3">
      <textarea
        className="form-control"
        rows="5"
        placeholder="Paste email content..."
        onChange={(e) => setEmail(e.target.value)}
      />

      <button className="btn btn-primary mt-2" onClick={handleScan}>
        Scan Email
      </button>
    </div>
  );
}
