import React from "react";

export default function SentimentCards({ data }) {
  const colors = {
    positive: "#4CAF50", // green
    negative: "#F44336", // red
    neutral: "#2196F3",  // blue
  };

  return (
    <div style={styles.container}>
      {["positive", "neutral", "negative"].map((t) => (
        <div key={t} style={{ ...styles.card, borderColor: colors[t] }}>
          <h3 style={{ color: colors[t] }}>{t.toUpperCase()}</h3>
          <p style={{ color: "#f8f8f8", fontSize: "24px", fontWeight: "bold" }}>
            {data[t] || 0}
          </p>
        </div>
      ))}
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    gap: "20px",
    margin: "20px 0",
    flexWrap: "wrap",
    justifyContent: "center",
  },
  card: {
    flex: "1 1 150px",
    padding: "20px",
    borderRadius: "10px",
    border: "2px solid",
    backgroundColor: "#1C1C1C", // slightly lighter than dashboard
    textAlign: "center",
    boxShadow: "0 0 15px rgba(255, 255, 255, 0.1)",
  },
};
