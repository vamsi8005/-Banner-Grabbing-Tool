# *****************************************
# *                                       *
# *   Created by   V A M S I              *
# *                                       *
# *****************************************
import socket

ip = input("Enter target IP address: ").strip()
max_port = int(input("Enter the maximum port number to scan: "))

banner_ports = [21, 22, 23, 25, 110, 143]

http_ports = [80, 443, 8080, 8000, 8443]

for port in range(1, max_port + 1):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.settimeout(2)
        server.connect((ip, port))
        displayed = False

        if port in banner_ports:
            try:
                banner = server.recv(1024).decode().strip()
                if banner:
                    print(f"[+] Port {port} open - Banner: {banner}")
                    displayed = True
            except:
                pass

        elif port in http_ports:
            try:
                request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
                server.send(request.encode())
                response = server.recv(1024).decode(errors="ignore").strip()
                if response:
                    print(f"[+] Port {port} open - HTTP Response: {response[:100]}")
                    displayed = True
            except:
                pass
        else:

            try:
                banner = server.recv(1024).decode().strip()
                if banner:
                    print(f"[+] Port {port} open - Banner: {banner}")
                    displayed = True
            except:
                pass

    except:
        continue  # ignore closed/filtere ports

    finally:
        server.close()
