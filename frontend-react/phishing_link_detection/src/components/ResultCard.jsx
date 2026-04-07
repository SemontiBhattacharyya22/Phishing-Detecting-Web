export default function ResultCard({ result }) {
  if (!result) return null;

  return (
    <div className="card p-3 shadow mt-3">
      <h4 className={
        result.prediction === "Phishing" ? "text-danger" : "text-success"
      }>
        {result.prediction}
      </h4>

      <ul>
        {result.reasons.map((r, i) => (
          <li key={i}>{r}</li>
        ))}
      </ul>
    </div>
  );
}