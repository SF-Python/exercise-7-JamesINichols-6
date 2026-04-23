# Name: Omar Salahat
# Course ID and Section: Program Logic 2002.0m1
# Date Created: April 12, 2026
# Program Title: MAC and IPv6 Address Generator
# Program Description: This program generates a random MAC address and IPv6 address using a reusable function.

import random


# This function generates hexadecimal digits for MAC or IPv6 addresses
def generate_hex_digits(number=6):
    hex_chars = "0123456789ABCDEF"
    result = ""

    # Loop through the required number of pairs
    for i in range(number):
        pair = ""

        # Each pair consists of two hexadecimal digits
        for j in range(2):
            pair += random.choice(hex_chars)

        # Add the pair to the result
        result += pair

        # Add colon formatting
        if i < number - 1:
            # MAC address: colon after every pair
            if number == 6:
                result += ":"
            # IPv6 address: colon after every 2 pairs (quartet)
            elif number == 16 and (i % 2 == 1):
                result += ":"

    return result


def main():
    # Generate and print MAC address
    print("Generating random MAC address...")
    print(generate_hex_digits())

    print()

    # Generate and print IPv6 address
    print("Generating random IPv6 address...")
    print(generate_hex_digits(16))


if(__name__ == "__main__"):
    main()