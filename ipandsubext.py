import socket
import fcntl
import struct
import os
def get_ip_and_mask(ifname: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get IP address
    ip_addr = socket.inet_ntoa(
        fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24]
    )

    # Get subnet mask
    netmask = socket.inet_ntoa(
        fcntl.ioctl(
            s.fileno(),
            0x891b,  # SIOCGIFNETMASK
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24]
    )

    # Convert subnet mask to prefix length
    mask_octets = map(int, netmask.split('.'))
    binary_str = ''.join([bin(octet)[2:].zfill(8) for octet in mask_octets])
    prefix_len = binary_str.count('1')

    return ip_addr, netmask, prefix_len


if __name__ == "__main__":
    interface_name = "eth0"   # Change to your interface, e.g., "wlan0"
    ip, mask, prefix = get_ip_and_mask(interface_name)
    print(f"Interface\t: {interface_name}")
    print(f"IP Address\t: {ip}")
    print(f"Subnet Mask\t: {mask}")
    print(f"CIDR Notation\t: {ip}/{prefix}")
