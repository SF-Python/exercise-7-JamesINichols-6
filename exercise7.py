# Kailey Swarthout
# COP2002.0M1
# 3/28/2026
# Exercise 7: Define Own Function (Generate MAC Address)

import random

def generate_hex_digits(number = 6):
    hex_digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    pairs = []
    count = 0

# Hex Pairs
    while count < number:
        first = random.choice(hex_digits)
        second = random.choice(hex_digits)
        pairs.append(first + second)
        count += 1

# MAC address
    if number == 6:
        return ":".join(pairs)
    
    # IPv6: 2 pairs -> quartets
    if number == 16:
        quartets = []
        i = 0
        while i < len(pairs):
            quartets.append(pairs[i] + pairs[i+1])
            i += 2
        return ":".join(quartets)
        
def main():
    mac = generate_hex_digits()
    ipv6 = generate_hex_digits(16)

    print(f"Generating random MAC address.... {mac}.")
    print(f"Generating random ipv6 address.... {ipv6}.")

if __name__ == "__main__":
    main()