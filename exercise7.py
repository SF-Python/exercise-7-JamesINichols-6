# Name: Cayden Major
# Course ID and Section:W26 COP2002.0M1
# Date Created: April 12, 2026
# Program Title: MAC and IPv6 Address Generator
# Program Description: This program generates a random MAC address and IPv6 address using a function.

import random

# Function to generate hexadecimal address
def generate_hex_digits(number=6):
    hex_digits = "0123456789ABCDEF"
    result = ""

    # Loop through number of groups
    for i in range(number):
        group = ""

        # MAC = pairs (2 digits), IPv6 = quartets (4 digits)
        if number == 6:
            for j in range(2):
                group += random.choice(hex_digits)
        else:
            for j in range(4):
                group += random.choice(hex_digits)

        result += group

        # Add colon if not last group
        if i < number - 1:
            result += ":"

    return result


def main():
    # Generate MAC Address
    print("Generating random MAC address...")
    mac_address = generate_hex_digits()
    print(mac_address)

    print()

    # Generate IPv6 Address
    print("Generating random IPv6 address...")
    ipv6_address = generate_hex_digits(16)
    print(ipv6_address)


if(__name__=="__main__"):
    main()
