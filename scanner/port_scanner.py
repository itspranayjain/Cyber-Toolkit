SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_single_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)   # 🔥 increased timeout

        result = s.connect_ex((target_ip, port))
        s.close()

        if result == 0:
            return port
    except:
        return None


def scan_ports(target):
    print(f"\nScanning {target}...\n")

    try:
        target_ip = socket.gethostbyname(target)
    except:
        print("Invalid target ❌")
        return

    print(f"Resolved IP: {target_ip}")

    open_ports = []

    # 🔥 Balanced threading
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_single_port, target_ip, port) for port in range(1, 1025)]

        for future in as_completed(futures):
            port = future.result()
            if port:
                service = SERVICES.get(port, "Unknown")
                print(f"[OPEN] Port {port} → {service}")
                open_ports.append(port)

    print("\nScan Complete ✅")

    if open_ports:
        print(f"Total open ports: {len(open_ports)}")

        with open("scan_results.txt", "w") as f:
            for port in open_ports:
                f.write(f"Port {port} is OPEN\n")

        print("Results saved to scan_results.txt 📄")
    else:
        print("No open ports found ❌")
