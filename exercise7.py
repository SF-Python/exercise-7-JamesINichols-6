# Name: Parveen Kumar
# Course ID and Section: COP2002 0M1
# Date Created: April 12, 2026
# Program Title: Exercise 7 - Define Own Function and Use It
# Program Description: Generates a random MAC address and a random IPv6 address using a required function.

import random


def generate_hex_digits(number=6):
    """Generate and return a MAC address or IPv6 address as a string."""
    hex_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                  "A", "B", "C", "D", "E", "F"]
    address = ""
    pair_count = 0

    # Build the address one pair of hexadecimal digits at a time.
    while pair_count < number:
        first_digit = hex_digits[random.randint(0, 15)]
        second_digit = hex_digits[random.randint(0, 15)]
        address += first_digit + second_digit

        # Place colons after every pair for MAC or after every two pairs for IPv6.
        if number == 6 and pair_count < number - 1:
            address += ":"
        elif number == 16 and pair_count < number - 1 and (pair_count + 1) % 2 == 0:
            address += ":"

        pair_count += 1

    return address


def main():
    """Display one random MAC address and one random IPv6 address."""
    print("Generating random MAC address...")
    print(generate_hex_digits())

    print()

    print("Generating random IPv6 address...")
    print(generate_hex_digits(16))


if(__name__ == "__main__"):
    main()
