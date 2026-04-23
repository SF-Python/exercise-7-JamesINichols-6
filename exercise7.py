#Kaleb Parkhurst   
#COP2002.0M1
#4/8/2026
#Exercise 7
#MAC address generator
import random

# Generates random hexadecimal digits for MAC and IPv6 addresses
def generate_hex_digits(number=6):
    # List of hexadecimal digits
    hex_digits = "0123456789ABCDEF"
    
    # Empty list to hold address parts
    address_parts = []
    
    # address generation based on the number of parts (6 for MAC, 16 for IPv6)
    if number == 6:
        for i in range(number):
            pair = ""
            for j in range(2):
                pair += random.choice(hex_digits)
            address_parts.append(pair)
    
    # address generation for IPv6 (8 groups of 4 hexadecimal digits)
    elif number == 16:
        for i in range(8):
            quartet = ""
            for j in range(4):
                quartet += random.choice(hex_digits)
            address_parts.append(quartet)
    
    # colon-separated address
    address = ":".join(address_parts)
    
    return address


def main():
    # mac address generation
    print("Generating random MAC address...", generate_hex_digits())
    
    print()  # Blank line for separation
    
    # Generate random IPv6 address
    print("Generating random IPv6 address...", generate_hex_digits(16))


if(__name__=="__main__"):
    main()