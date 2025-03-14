import socket

def scan(target, ports):
    """
    Scans a given target IP for open ports.

    :param target: The IP address to scan.
    :param ports: A list of ports to check.
    """
    print(f"Scanning {target} for open ports...\n")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a socket
        s.settimeout(1)  # Setting timeout for connection
        result = s.connect_ex((target, port))  # Trying to connect

        if result == 0:
            print(f"[+] Port {port} is OPEN")  # If the port is open, print it
        s.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")  # User enters an IP address
    common_ports = [21, 22, 23, 25, 53, 80, 443, 8080]  # List of common ports
    scan(target_ip, common_ports)  # Call the scan function
