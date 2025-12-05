import { useState } from 'react';
import Navbar from '../components/Navbar';
import TweetInput from '../components/TweetInput';
import SentimentCards from '../components/SentimentCards';
import SentimentChart from '../components/SentimentChart';
import React from 'react';

export default function Dashboard(){
  const [result,setResult] = useState({positive:0,negative:0,neutral:0});
  const [rows,setRows] = useState([]);

  return (
    <>
      <TweetInput setResult={(r)=>{ setResult(r.summary); setRows(r.rows||[]); }} />
      <SentimentCards data={result}/>
      <SentimentChart data={result}/>
    </>
  );
}
