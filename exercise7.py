# Zoe Dobelstein
# COP2002-001
# 4/2/2026
# Exercise 7 - Functions
# program that makes a random mac and ipv6 address using a function

import random

def generate_hex_digits(number=6):
    hexVals = "0123456789ABCDEF"
    address = ""
    i = 0

    while i < number * 2:
        address += random.choice(hexVals)

        # formatting mac vs ipv6
        if number == 6:
            if i % 2 == 1 and i != (number * 2 - 1):
                address += ":"
        else:
            if i % 4 == 3 and i != (number * 2 - 1):
                address += ":"

        i += 1

    return address


def main():
    print("Generating random MAC address...")
    print(generate_hex_digits())

    print()

    print("Generating random IPv6 address...")
    print(generate_hex_digits(16))


if(__name__=="__main__"):
    main()