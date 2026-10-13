# 🛰️ Network Mapping & Containerized Web Stack

<img width="1536" height="942" alt="image" src="https://github.com/user-attachments/assets/3b918735-9b3a-4127-9ae6-4c7e541945c7" />



## 📌 Overview
This project integrates **network scanning, backend storage, and containerized web visualization** into a cohesive system.  
It is designed to:
- Run **Nmap scans** (`-PR -sn <CIDR>`) to discover hosts.
- Parse scan results into **JSON** format.
- Store results in a **MySQL database** (hostname, IP, MAC address).
- Serve data via a **Node.js backend** (REST API).
- Visualize the network topology using a **frontend (HTML/CSS/JS)** hosted on **Nginx**.
- All components are containerized using **Docker** for portability and scalability.

---

## ⚙️ Components
- **Nmap Scanner (Python Script)** → Generates JSON output of discovered hosts.
- **MySQL Database** → Stores structured scan results.
- **Node.js Backend** → Provides API endpoints to fetch stored data.
- **Nginx Frontend** → Displays interactive network mapping visualization.
- **Docker Compose** → Orchestrates multi-container setup.

---

## 🗂️ Project Structure
├── scanner/          # Python script for Nmap scan + JSON parsing

├── backend/          # Node.js server (server.js, Dockerfile, package.json)

├── frontend/         # HTML, CSS, JS files + Nginx Dockerfile

├── database/         # MySQL Dockerfile + init scripts

├── docker-compose.yml

└── README.md

---

## 🚀 Usage
1. **Run Nmap Scan**
   ```bash
   python3 scanner/nmap_scan.py <CIDR>
2. **Complete Container Setup**
   ```bash
   docker-compose up -d
## Conclusion
   This is a project which will need more enhancements for now this is Version 0.1.
