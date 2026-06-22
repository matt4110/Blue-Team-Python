import socket
import struct
import os

if not os.path.exists("blacklisted_ips.txt"):
    print("blacklisted_ips.txt not found. Please run bsoup-column.py to generate the file.")
    exit()

with open("blacklisted_ips.txt", "r") as file:
    monitored_ips = [line.strip() for line in file.readlines()]

host = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
s.bind((host, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

while True:
    packet, addr = s.recvfrom(65565)
    ip_header = packet[0:20]  # Extract the IP header (first 20 bytes)
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header) # Divide IP header into its components

    version_ihl = iph[0]  # Extract the version and IHL (Internet Header Length) from the first byte
    ihl = version_ihl & 0xF # Extract Header Length (IHL) by masking the lower 4 bits
    iph_length = ihl * 4 # Calculate the total length of the IP header in bytes

    # ntoa converts the packed binary format of the IP address to a human-readable string format
    src_addr = socket.inet_ntoa(iph[8])
    dst_addr = socket.inet_ntoa(iph[9])

    if src_addr in monitored_ips:
        print(f"Alert: Incoming connection from blacklisted IP {src_addr}")

    if dst_addr in monitored_ips:
        print(f"Alert: Outgoing connection to blacklisted IP {dst_addr}")