import { useAuth } from "./hooks/useAuth";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";

function App() {
  const { token } = useAuth();
  return token ? <Dashboard /> : <Login />;
}

export default App;
