# Elijah Morris
# COP2002 0M1
# 4/11/2026
# Random Hexadecimal Generator for MAC and IPv6 Addresses
# This program generates random hexadecimal digits to create valid MAC addresses and IPv6 addresses.

import random 

def generate_hex_digits(number=6):
    hex_digits = "0123456789ABCDEF"
    result = ""

    # MAC address 
    if number == 6:
        for i in range(number):
            pair = ""
            for j in range(2):
                pair += random.choice(hex_digits)
            result += pair
            if i < number - 1:
                result += ":"

    # IPv6 address 
    elif number == 16:
        for i in range(8):  # 8 quartets
            quartet = ""
            for j in range(4):
                quartet += random.choice(hex_digits)
            result += quartet
            if i < 7:
                result += ":"

    return result


def main():
    print("Generating random MAC address...")
    mac = generate_hex_digits()
    print(mac)

    print()

    print("Generating random IPv6 address...")
    ipv6 = generate_hex_digits(16)
    print(ipv6)


if(__name__=="__main__"):
    main()