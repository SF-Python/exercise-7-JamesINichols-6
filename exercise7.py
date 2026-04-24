# Allison Day
# COP2002.0M1
# April 5, 2026
# Exercise 7
# This program will generate a random MAC address or IPv6 address

def main():
    import random

    choices = [6, 16]
    number = random.choice(choices)


def generate_hex_digits(number=6):
    print("Generating random MAC Address...")
    
    # Uses random module to generate a random hex digit
    import random

    # Lists all possible hex digits that can be used
    hex_digits = "0123456789ABCDEF"
    mac_address = ""
    
    # Loop for 6 pairs to complete the MAC Address
    for int in range(6):
        pair = random.choice(hex_digits) + random.choice(hex_digits)
        mac_address += pair
        if int < 5:

            # Adds colon between pairs
            mac_address += ":"
    print(mac_address)
    print() 
    
def generate_hex_digits(number=16):
    print("Generating random IPv6 Address...")
    
    # Uses random module to generate a random hex digit
    import random

    # Lists all possible hex digits that can be used
    hex_digits = "0123456789ABCDEF"
    ipv6_address = ""
    
    # Loop for 8 pairs to complete the IPv6 Address
    for int in range(8):
        pair = random.choice(hex_digits) + random.choice(hex_digits)
        ipv6_address += pair
        if int < 7:

            # Adds colon between pairs
            ipv6_address += ":"
    print(ipv6_address)
    print()

if (main() == generate_hex_digits(number=6)):
    main()

elif (main() == generate_hex_digits(number=16)):
    main()