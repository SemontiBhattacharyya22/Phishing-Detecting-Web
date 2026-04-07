import { useAuth } from "../hooks/useAuth";

export default function Navbar() {
  const { logout } = useAuth();

  return (
    <nav className="navbar navbar-dark bg-dark px-4">
      <span className="navbar-brand mb-0 h1">PhishGuard</span>
      <button className="btn btn-danger" onClick={logout}>
        Logout
      </button>
    </nav>
  );
}