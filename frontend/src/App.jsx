
import { useState } from "react";

function App() {
  const [topic,setTopic] = useState("");
  const [result,setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const runResearch = async ()=>{
    if(!topic) return;
    setLoading(true);
    setError(null);
    try{
      const res = await fetch("http://127.0.0.1:8000/research",{
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({topic}),
      });
      if(!res.ok) throw new Error("Request Failed");
      const data = await res.json();
      setResult(data);
    }catch(error){
      setError(error.message)
    }finally{
      setLoading(false);
    }
  };
  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>AI Research Assistant</h1>

      <input
        type="text"
        placeholder="Enter research topic"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <button onClick={runResearch} disabled={loading}>
        {loading ? "Researching..." : "Start Research"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Research Questions</h3>
          <ul>
            {result.questions.map((q, i) => (
              <li key={i}>{q}</li>
            ))}
          </ul>

          <h3>Final Answer</h3>
          <pre style={{ whiteSpace: "pre-wrap" }}>
            {result.final_answer}
          </pre>
        </div>
      )}
    </div>
  );
}

export default App;
