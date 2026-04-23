# Christopher Canty
# COP2002-0M1
# April 12th, 2026
# Exercise 7
# This an exercise on Functions in Python - generating MAC and IPv6 addresses.




import random

# List of valid hex characters
hex_characters = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

def generateMacAddress():

    address_mac = ""
    i = 0
# Loop continues until 12 hex characters have been generated
    while i < 12:       
        hex_pair = random.choice(hex_characters)
        address_mac += hex_pair
        i += 1

# Generating separation of : between each pair
        if i % 2 == 0 and i < 12:
            address_mac += ":"

    return address_mac


def generateIPv6():

    address_ipv6 = ""
    i = 0
# Loop continues until 32 hex characters have been generated
    while i < 32:
        hex_quartet = random.choice(hex_characters)
        address_ipv6 += hex_quartet
        i += 1
        
# Generating separation of : between each quartet
        if i % 4 == 0 and i < 32:
            address_ipv6 += ":"

    return address_ipv6


def main():   
# Function to call the MAC addresses
    print("Generating random MAC Address...")
    print (generateMacAddress())

    print()
# Function to call the IPv6 addresses
    print("Generating random IPv6 Address...")
    print (generateIPv6())

if __name__ == "__main__":
    main()