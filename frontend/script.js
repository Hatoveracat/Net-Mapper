async function fetchHosts() {
  try {
    const response = await fetch("http://localhost:3000/hosts");
    const hosts = await response.json();

    const networkDiv = document.getElementById("network");
    networkDiv.innerHTML = "";

    hosts.forEach(host => {
      const node = document.createElement("div");
      node.className = "node";

      node.innerHTML = `
        <p><strong>IP:</strong> ${host.ip}</p>
        <p><strong>MAC:</strong> ${host.mac}</p>
      `;

      networkDiv.appendChild(node);
    });
  } catch (error) {
    console.error("Error fetching hosts:", error);
  }
}

fetchHosts();

