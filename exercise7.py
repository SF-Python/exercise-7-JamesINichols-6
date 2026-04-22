# Jarek Martin
# COP2002-0M1
# 4/4/2026
# MAC address or IPV6 address generator
# Generates a random MAC or IPV6 address based upon input


import random


# generates random Hexadecimal digits
def getHexDigits(length):              
                                        
    # variables
    hexDigits = "0123456789ABCDEF"
    result = ""

    # for loop to generate hexdigits
    for count in range(length):
        result += random.choice(hexDigits)

    return result                       

# 6. Function Definition = generate_hex_digits
# generates either MAC address or IPv6 address
def generate_hex_digits(number=6):      # 1. Name = generate_hex_digits
                                        # 2. Parameter = number
    address = ""                        # 4. Default Argument = 6

    if number == 6:

        # generates MAC address
        for count in range(6):
            address += getHexDigits(2)  # 7. Function Call = getHexDigits(2)
                                        # 3. Argument = 2
            # places colons
            if count < 5:
                address += ":"

        return address                  # 5. Return Value = address

    elif number == 16:

        # generates IPv6 address
        for count in range(8):
            address += getHexDigits(4)  # 7. Function Call = getHexDigits(4)
                                        # 3. Argument = 4
            # places colons             
            if count < 7:
                address += ":"

        return address                  # 5. Return Value = address

   
def main():

    MACAddress = generate_hex_digits()
    Ipv6Address = generate_hex_digits(16)
    
    print(f"Generating random MAC address...\n{MACAddress}")

    print()

    print(f"Generation random IPv6 address...\n{Ipv6Address}")

    


if (__name__ == "__main__"):
    main()               