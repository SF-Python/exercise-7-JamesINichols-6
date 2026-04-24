# Grant Tidwell
# COP2002.0M1
# 4/12/2026
# Exercise 7: Define Own Function and Use It

import random


def generate_hex_digits(number=6):
    #Generates either a MAC address (number=6) or IPv6 address (number=16)
    hex_pairs = []
    count = 0
    
    while count < number:
        byte_value = random.randint(0, 255)
        hex_pair = f"{byte_value:02X}"
        hex_pairs.append(hex_pair)
        count += 1
    
    if number == 6:
        # MAC Address
        return ":".join(hex_pairs)
    elif number == 16:
        # IPv6 Address - group every 4 hex digits
        ipv6_groups = []
        for i in range(0, len(hex_pairs), 2):
            group = hex_pairs[i] + hex_pairs[i+1]
            ipv6_groups.append(group)
        return ":".join(ipv6_groups)
    
    else: return "Error: Invalid number"


def main():
    print("Random Address Generator\n")
    
    while True:
        print("1. Generate MAC Address")
        print("2. Generate IPv6 Address")
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            address = generate_hex_digits(6)          # Must call with 6
            print(f"\nGenerated MAC Address: {address}\n")
            
        elif choice == "2":
            address = generate_hex_digits(16)         # Must call with 16
            print(f"\nGenerated IPv6 Address: {address}\n")
            
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()