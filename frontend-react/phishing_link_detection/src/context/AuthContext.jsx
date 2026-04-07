import { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const navigate = useNavigate();

  const [token, setToken] = useState(localStorage.getItem("token"));

  // ✅ Keep token in sync (important for refresh cases)
  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    if (storedToken) setToken(storedToken);
  }, []);

  const login = (t) => {
    localStorage.setItem("token", t);
    setToken(t);

    // ✅ redirect after login
    navigate("/");
  };

  const logout = () => {
    localStorage.removeItem("token");
    setToken(null);

    // ✅ redirect after logout
    navigate("/login");
  };

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};