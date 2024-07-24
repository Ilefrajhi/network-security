import subprocess
import re

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

interface = "eth0"
new_mac = "00:11:22:33:44:55"
current_mac = get_current_mac(interface)
print(f"Current MAC = {current_mac}")

change_mac(interface, new_mac)
current_mac = get_current_mac(interface)
print(f"MAC address was successfully changed to {current_mac}")
