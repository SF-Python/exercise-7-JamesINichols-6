# Dakoda Melendez
# COP2002.0M1
# March 27, 2026
# Exercise 7: Define Own Function and Use It
# Revise the Exercise 5 program to use functions.  It will also allow the user to be able to generate both a mac address and an IPV6 address.

import random

def generate_hex_digits(number=6):
    """Generate a string of random hexadecimal digits."""
    hex_chars = "0123456789ABCDEF"
    hex_string = ""
    
    # Generate the specified number of hexadecimal characters
    for _ in range(number):
        hex_string += random.choice(hex_chars)
    
    return ":".join([hex_string[i:i+4] for i in range(0, len(hex_string), 4)])


def generate_macaddress(number=6):
    """Generate a random MAC address using a while loop."""
    hex_chars = "0123456789ABCDEF"
    mac_address = []

    # Generate 6 pairs of hexadecimal characters using a while loop
    while len(mac_address)<6:
        # Pick two random hexadecimal characters
        char1=random.choice(hex_chars)
        char2=random.choice(hex_chars)
        # Combine the two characters to form a byte
        byte = char1 + char2
        mac_address.append(byte)

    # Join each byte with a colon to form MAC address
    return ":".join(mac_address)

def main():
    mac_address = generate_macaddress()
    print("Generating random MAC Address...","\n",mac_address)
    ipv6_address = generate_hex_digits(32)
    print("Generating random IPv6 Address...","\n",ipv6_address)

if __name__ == "__main__":
    main()