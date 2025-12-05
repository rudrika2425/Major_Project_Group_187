import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <div style={{
      padding:'15px',
      background:'#f8f8f8',
      color:'#0f2027',
      fontSize:'22px',
      display:'flex',
      justifyContent:'space-between',
      alignItems:'center'
    }}>
      
      <div style={{fontWeight: 900, fontSize: '24px', letterSpacing: '1px' }}>Twitter Sentiment Analysis Dashboard</div>

      <div>
        <Link to="/login" style={styles.btn}>Login</Link>
        <Link to="/signup" style={styles.btn}>Signup</Link>
      </div>
    </div>
  );
}

const styles = {
  btn: {
    marginLeft:'15px',
    padding:'8px 12px',
    background:'#0f2027',
    color:'#f8f8f8',
    borderRadius:'6px',
    textDecoration:'none',
    fontSize:'16px',
    fontWeight:'bold'
  }
};
