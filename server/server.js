const express = require("express");
const mysql = require("mysql2");
const cors = require("cors");

const app = express();
app.use(cors());

// MySQL connection
const db = mysql.createConnection({
  host: "172.17.0.2",
  user: "logger",
  password: "logger@123",
  database: "network_db"
});

// API endpoint to fetch hosts
app.get("/hosts", (req, res) => {
  db.query("SELECT ip, mac FROM hosts", (err, results) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json(results);
  });
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});

