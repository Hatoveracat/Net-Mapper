import json
import mysql.connector

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as f:
        return json.load(f)

def connect_db():
    """Connect to MySQL database."""
    return mysql.connector.connect(
        host="localhost",       # Change if needed
        user="root",            # Your MySQL username
        password="password",    # Your MySQL password
        database="network_db"   # Database name
    )

def insert_hosts(data, conn):
    """Insert JSON data into MySQL table."""
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hosts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            hostname VARCHAR(255),
            ip VARCHAR(50),
            mac VARCHAR(50)
        )
    """)

    # Insert each host record
    for host in data:
        cursor.execute("""
            INSERT INTO hosts (hostname, ip, mac)
            VALUES (%s, %s, %s)
        """, (host.get("hostname"), host.get("ip"), host.get("mac")))

    conn.commit()
    cursor.close()

if __name__ == "__main__":
    # Load JSON file
    hosts_data = load_json("hosts.json")

    # Connect to DB
    connection = connect_db()

    # Insert data
    insert_hosts(hosts_data, connection)

    connection.close()
    print("Data inserted successfully!")

