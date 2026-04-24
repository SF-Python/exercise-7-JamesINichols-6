# Travis Prescott
# COP2002-0M1
# April 12, 2026
# Exercise 7
# Program generates a random MAC address and a random IPv6 address using nested loops to create hexadecimal digits and concatenate them into the final address strings. The program defines a function that can generate either a MAC address or an IPv6 address based on the number of groups specified.

import random
# The function generates a random string of hexadecimal digits formatted as either a MAC address (6 groups of 2 digits) or an IPv6 address (8 groups of 4 digits) based on the input parameter 'number'.
def generate_hex_digits(number=6):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7',
                 '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    address = ""
    group_count = 0

    if number == 6:
        digits_per_group = 2
    else:
        digits_per_group = 4

    while group_count < number:
        group = ""
        digit_count = 0

        while digit_count < digits_per_group:
            group += random.choice(hex_chars)
            digit_count += 1

        address += group

        if group_count < number - 1:
            address += ":"

        group_count += 1

    return address

# The main function generates and prints a random MAC address and a random IPv6 address by calling the 'generate_hex_digits' function with the appropriate number of groups for each address type.
def main():
    print("Generating random MAC address...")
    mac_address = generate_hex_digits()
    print(mac_address)

    print()

    print("Generating random IPv6 address...")
    ipv6_address = generate_hex_digits(8)
    print(ipv6_address)


if(__name__ == "__main__"):
    main()