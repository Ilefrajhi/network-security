import os

def configure_firewall():
    os.system("iptables -F")
    os.system("iptables -P INPUT DROP")
    os.system("iptables -P FORWARD DROP")
    os.system("iptables -P OUTPUT ACCEPT")
    os.system("iptables -A INPUT -i lo -j ACCEPT")
    os.system("iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")

    # Allow specific ports
    os.system("iptables -A INPUT -p tcp --dport 22 -j ACCEPT")  # SSH
    os.system("iptables -A INPUT -p tcp --dport 80 -j ACCEPT")  # HTTP
    os.system("iptables -A INPUT -p tcp --dport 443 -j ACCEPT") # HTTPS

configure_firewall()
print("Firewall rules configured.")
