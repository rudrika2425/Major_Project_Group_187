import axios from 'axios';
import { useState } from 'react';
import React from 'react';

export default function TweetInput({ setResult }) {
  const [text, setText] = useState('');

  const analyze = async () => {
    try {
      const res = await axios.post('http://localhost:5000/analyze', { text });
      setResult(res.data);
    } catch (error) {
      console.error('Error analyzing text:', error);
    }
  };

  return (
    <div style={styles.container}>
      <textarea
        value={text}
        onChange={e => setText(e.target.value)}
        rows={4}
        placeholder="Enter tweet text here..."
        style={styles.textarea}
      />
      <button onClick={analyze} style={styles.button}>
        Analyze
      </button>
    </div>
  );
}

const styles = {
  container: {
    margin: '20px 0',
    padding: '20px',
    borderRadius: '10px',
    backgroundColor: '#1C1C1C', // slightly lighter than dashboard for contrast
    boxShadow: '0 0 15px rgba(255, 255, 255, 0.1)',
  },
  textarea: {
    width: '98%',
    padding: '12px',
    borderRadius: '8px',
    border: '1px solid #555',
    backgroundColor: '#0f2027', // matches dashboard
    color: '#f8f8f8',           // text color
    fontSize: '16px',
    resize: 'none',
  },
  button: {
    marginTop: '10px',
    padding: '12px 20px',
    backgroundColor: '#FFD700', // gold to pop on dark background
    color: '#0f2027',           // dark text on gold button
    border: 'none',
    borderRadius: '8px',
    fontSize: '16px',
    fontWeight: 'bold',
    cursor: 'pointer',
    transition: '0.3s',
  },
};
