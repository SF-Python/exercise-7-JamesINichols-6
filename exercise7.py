
# Name: Mikesael Nieves
# Course ID and section: COP2002.0M1
# Date Created: 04/09/2026
# Program Title: MAC and IPv6 Address Generator
# Program Description: This program makes random MAC and IPv6 addresses using functions.



import random

# This function makes a MAC or IPv6 address.
# number is how many pairs or quartets to make. Default is 6 for MAC.
def generate_hex_digits(number=6):
    hex_digits = []  # list to hold the parts

    if number == 6:
        # MAC address: 6 pairs (2 hex digits each)
        for i in range(number):
            a = random.randint(0, 15)
            b = random.randint(0, 15)
            pair = hex(a)[2:].upper() + hex(b)[2:].upper()
            if len(pair) < 2:
                pair = "0" + pair
            hex_digits.append(pair)
        address = ':'.join(hex_digits)  # join with colons
        return address  # return value
    elif number == 16:
        # IPv6 address: 8 quartets (4 hex digits each)
        for i in range(8):
            quartet = f"{random.randint(0, 65535):04X}"
            hex_digits.append(quartet)
        address = ':'.join(hex_digits)
        return address
    else:
        return ''


# This is the main function
def main():
    print("Generating random MAC address...")
    mac = generate_hex_digits()  # function call, uses default
    print(mac)

    print()  # blank line

    print("Generating random IPv6 address...")
    ipv6 = generate_hex_digits(16)  # function call, uses 16
    print(ipv6)


# This makes the main function run
if __name__ == "__main__":
    main()