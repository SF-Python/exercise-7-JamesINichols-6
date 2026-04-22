# Alex Libertowski
# COP2002-0M1
# April 01, 2026
# Exercise 7: Define Own Functions and Use It
# Practicing the use of functions by generating MAC and IPv6 addresses

from random import choice


def generate_hex_digits(number=6):
    hexValues = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]

    HEX_CHUNKS = 2
    COLON_INTERVAL = 2
    if number == 6:
        COLON_INTERVAL = 2
    else:
        COLON_INTERVAL = 4

    address = ""
    i = 0
    for i in range(number * HEX_CHUNKS):
        # Add a colon at every two hex values, except the first index
        if i != 0 and i % COLON_INTERVAL == 0:
            address += ":"

        hexValue = choice(hexValues)
        address += hexValue
        i += 1

    return address


def main():
    print("Generating random MAC address...")
    hexAddress = generate_hex_digits()
    print(hexAddress)

    print("\nGenerating random IPv6 address...")
    hexAddress = generate_hex_digits(16)
    print(hexAddress)


if __name__ == "__main__":
    main()
