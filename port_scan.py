import socket

def port_scan(target_ip, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

target_ip = "192.168.1.1"
ports = port_scan(target_ip, (1, 1024))
print(f"Open ports on {target_ip}: {ports}")
