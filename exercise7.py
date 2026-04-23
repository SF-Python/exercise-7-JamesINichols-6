import random

def generate_hex_digits(number=6):
    hex_chars = "0123456789ABCDEF"
    pairs = []

    # generate pairs of hex digits
    for i in range(number):
        pair = random.choice(hex_chars) + random.choice(hex_chars)
        pairs.append(pair)

    # MAC address (6 pairs)
    if number == 6:
        return ":".join(pairs)

    # IPv6 address (16 pairs -> 8 groups of 4 hex digits)
    elif number == 16:
        groups = []
        for i in range(0, 16, 2):
            groups.append(pairs[i] + pairs[i + 1])
        return ":".join(groups)


def main():
    mac_address = generate_hex_digits(6)
    ipv6_address = generate_hex_digits(16)

    print("Generating random MAC address...")
    print(f"{mac_address}")
    print("Generating random IPv6 address...")
    print(f"{ipv6_address}")


if(__name__ == "__main__"):
    main()
    