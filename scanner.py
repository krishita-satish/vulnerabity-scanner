import socket
import colorama
from colorama import Fore, Style

colorama.init()  # Initialize color support for Windows

def scan_ports(target):
    print(Fore.CYAN + f"\nScanning {target} for open ports...\n" + Style.RESET_ALL)
    
    for port in range(1, 65536):  # Scanning all ports
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  # Shorter timeout for faster scanning
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(Fore.GREEN + f"[+] Port {port} is OPEN" + Style.RESET_ALL)
            
            s.close()
        except KeyboardInterrupt:
            print(Fore.RED + "\nScan interrupted by user. Exiting..." + Style.RESET_ALL)
            break
        except socket.error:
            print(Fore.RED + "Could not connect to target." + Style.RESET_ALL)
            break

# Get target from user
target_ip = input("Enter target IP or domain: ")
scan_ports(target_ip)
