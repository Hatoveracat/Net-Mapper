import subprocess
import json
import re

def nmap_scan(cidr, output_file="hosts.json"):
    try:
        # Run nmap with -PR (ARP ping) and -sn (ping scan, no port scan)
        result = subprocess.run(
            ["sudo", "nmap", "-PR", "-sn", cidr],
            capture_output=True,
            text=True,
            check=True
        )

        output = result.stdout
        devices = []
        
        # Regex patterns for IP and MAC
        ip_pattern = re.compile(r"Nmap scan report for (\d+\.\d+\.\d+\.\d+)")
        mac_pattern = re.compile(r"MAC Address: ([0-9A-Fa-f:]{17})")

        current_ip = None
        for line in output.splitlines():
            ip_match = ip_pattern.search(line)
            mac_match = mac_pattern.search(line)

            if ip_match:
                current_ip = ip_match.group(1)

            if mac_match and current_ip:
                devices.append({
                    "IP Address": current_ip,
                    "MAC Address": mac_match.group(1)
                })
                current_ip = None  # reset after pairing

        # Save results to JSON file
        with open(output_file, "w") as f:
            json.dump(devices, f, indent=4)

        # Return JSON string for console output
        return json.dumps(devices, indent=4)

    except subprocess.CalledProcessError as e:
        return f"Error running nmap: {e}"

if __name__ == "__main__":
    cidr_input = input("Enter CIDR notation (e.g., 192.168.1.0/24): ")
    json_output = nmap_scan(cidr_input)
    print(json_output)
    #print(f"\n✅ Results saved to hosts.json")

