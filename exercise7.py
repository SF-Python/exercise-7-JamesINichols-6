# Morgan Palmer
# COP2002-0M1
# 4/12/26
# MAC and IPv6 Address Generator
# Program generates MAC address and an IPv6 address

import random

# number = 6 MAC address
# number = 16 IPv6
def generate_hex_digits(number = 6):
    # valid hexadecimal digits
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    result = ""
    pair_count = 0

    # loop for hex pairs
    while pair_count < number:

        digit_count = 0
        hex_pair = ""


        while digit_count < 2:
            random_index = random.randint(0, len(hex_digits) - 1)
            hex_pair = hex_pair + hex_digits[random_index]
            digit_count += 1

        result = result + hex_pair


        if number == 6:
            if pair_count < number - 1:
                result = result + ":"


        else:
            if pair_count % 2 == 1 and pair_count < number - 1:
                result = result + ":"

        pair_count += 1

    return result

def main():

    # Displays the generated MAC address
    print("Generating random MAC address...")
    print(generate_hex_digits())

    print()
    
    # Displays the generated IPv6 address
    print("Generating random IPv6 address...")
    print(generate_hex_digits(16))


if (__name__ == "__main__"):
    main()