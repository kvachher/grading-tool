import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError("Please select a file first.");
      return;
    }
    
    setLoading(true);
    setError(null);
    
    // Create form data to send file
    const formData = new FormData();
    formData.append("file", file);
    
    try {
      const response = await fetch("http://localhost:8000/api/upload", {
        method: "POST",
        body: formData,
      });
      
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Failed to process the image");
      }
      
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error:", error);
      setError(error.message || "An error occurred while processing the image.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Intelligent Grading Tool</h1>
      <div className="upload-section">
        <form onSubmit={handleSubmit}>
          <div className="file-input-container">
            <input 
              type="file" 
              onChange={handleFileChange} 
              accept="image/jpeg,image/png" 
              className="file-input"
            />
            <button type="submit" className="submit-button" disabled={loading}>
              {loading ? "Processing..." : "Submit for Grading"}
            </button>
          </div>
        </form>
      </div>
      
      {error && <div className="error-message">{error}</div>}
      
      {loading && <div className="loading">Processing your image...</div>}
      
      {result && (
        <div className="result-container">
          <h2>Results</h2>
          <div className="result-section">
            <h3>Extracted Text:</h3>
            <div className="text-content">{result.text}</div>
          </div>
          <div className="result-section">
            <h3>Analysis:</h3>
            <div className="analysis-content">{result.analysis.grade}</div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
