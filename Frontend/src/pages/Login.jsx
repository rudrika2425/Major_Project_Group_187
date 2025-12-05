import React from "react";

export default function Login() {
  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2>Login</h2>

        <input type="text" placeholder="Email" style={styles.input} />
        <input type="password" placeholder="Password" style={styles.input} />

        <button style={styles.button}>Login</button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "80vh",
  },
  card: {
    width: "300px",
    padding: "20px",
    boxShadow: "0 0 10px rgba(0,0,0,0.2)",
    borderRadius: "10px",
    background: "#f8f8f8",
    textAlign: "center",
  },
  input: {
    width: "90%",
    padding: "10px",
    margin: "8px 0",
    borderRadius: "5px",
    border: "1px solid gray",
  },
  button: {
    width: "100%",
    padding: "10px",
    marginTop: "10px",
    background: "#0f2027",
    color: "#f8f8f8",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
};
