# Jordyn Solano
# COP2002-0M1
# April 12, 2026
# Defining a function and using it
# Generates a random IPv6 Address and MAC Address

import random

# Defines the function that generates a random address
def generate_hex_digits(number=6):
    if number == 6:
        # Same code from Exercise 5
        mac_address = ""
        count = 0
        while count < 6:
            hex_part = random.randint(0, 255)
            address_part = f"{hex_part:02X}"
            mac_address += address_part
            if count < 5:
                mac_address += ":"
            count += 1
        return mac_address
    elif number == 16:
        # Altered code from Exercise 5
        ipv6_address = ""
        count = 0
        while count < 8:
            hex_part = random.randint(0, 65535)
            address_part = f"{hex_part:04X}"
            ipv6_address += address_part
            if count < 7:
                ipv6_address += ":"
            count += 1
        return ipv6_address

# Defines the function where the strings and values is printed
def main():
    print()
    print("Generating random MAC address...")
    mac = generate_hex_digits()
    print(mac)
    print()

    print("Generating random IPv6 Address...")
    # Generates IPv6 address from this function call
    ipv6 = generate_hex_digits(16)
    print(ipv6)
    print()

# Executes the random MAC and IPv6 address generator
if(__name__=="__main__"):
    main()
