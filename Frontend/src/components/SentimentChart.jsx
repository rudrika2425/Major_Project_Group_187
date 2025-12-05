import { useEffect, useRef } from "react";
import Chart from "chart.js/auto";
import React from "react";

export default function SentimentChart({ data }) {
  const pieRef = useRef();
  const barRef = useRef();

  useEffect(() => {
    // Destroy previous charts to avoid duplication
    if (pieRef.current.chart) pieRef.current.chart.destroy();
    if (barRef.current.chart) barRef.current.chart.destroy();

    // Pie chart
    pieRef.current.chart = new Chart(pieRef.current.getContext("2d"), {
      type: "pie",
      data: {
        labels: ["Positive", "Neutral", "Negative"],
        datasets: [
          {
            data: [data.positive, data.negative, data.neutral],
            backgroundColor: ["#4CAF50", "#2196F3","#F44336"], // green, red, blue
            borderColor: "#0f2027", // border to blend with background
            borderWidth: 2,
          },
        ],
      },
      options: {
        plugins: {
          legend: {
            labels: { color: "#f8f8f8", font: { size: 14 } },
          },
        },
      },
    });

    // Bar chart
    barRef.current.chart = new Chart(barRef.current.getContext("2d"), {
      type: "bar",
      data: {
        labels: ["Positive", "Neutral", "Negative"],
        datasets: [
          {
            label: "Number of Tweets",
            data: [data.positive, data.negative, data.neutral],
            backgroundColor: ["#4CAF50",  "#2196F3","#F44336"],
          },
        ],
      },
      options: {
        scales: {
          x: { ticks: { color: "#f8f8f8" }, grid: { color: "#444" } },
          y: { ticks: { color: "#f8f8f8" }, grid: { color: "#444" } },
        },
        plugins: {
          legend: {
            labels: { color: "#f8f8f8", font: { size: 14 } },
          },
        },
      },
    });
  }, [data]);

  return (
    <div style={styles.container}>
      <canvas ref={pieRef} width="300" height="300"></canvas>
      <canvas ref={barRef} width="300" height="300"></canvas>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    gap: "30px",
    margin: "20px 0",
    justifyContent: "center",
    flexWrap: "wrap",
    backgroundColor: "#0f2027", // matches dashboard
    padding: "20px",
    borderRadius: "12px",
    boxShadow: "0 0 20px rgba(255,255,255,0.05)",
  },
};
