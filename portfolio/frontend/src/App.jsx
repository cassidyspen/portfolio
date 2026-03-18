import { useState, useEffect } from "react";
import CardTable from "./components/CardTable";
import "./styles/globals.css";

function App() {
  const [loaded, setLoaded] = useState(false);
  useEffect(() => {
    const t = setTimeout(() => setLoaded(true), 80);
    return () => clearTimeout(t);
  }, []);

  return (
    <div className={`app ${loaded ? "app--loaded" : ""}`}>
      <CardTable />
    </div>
  );
}

export default App;
