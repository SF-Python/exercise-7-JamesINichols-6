# Nicholas Warren
# COP2002.0M1
# April 4, 2026
# Exercise 7
# Generates a MAC address or IPv6 Adress based on user needs

import random

hex=("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")

def generate_hex_digits(number=6):
    # Generates a MAC address
    if(number==6):
        print("Generating random MAC address...")
        MACAddress = ""
        while(len(MACAddress) < 17):
            if((len(MACAddress)-1)%3==1):
                MACAddress += ":"
            else:
                MACAddress += str(hex[(random.randint(0,15))])
        return MACAddress
    # Generate a IPv6 address
    elif(number==16):
        print("Generating random IPv6 address...")
        IPv6 = ""
        while(len(IPv6) < 39):
            for i in range(4):
                IPv6 += str(hex[(random.randint(0,15))])
            if(len(IPv6)!=39):
                IPv6 += ":"
        return IPv6


# Display that a address is being generated and the output of that address
def main():
    print(generate_hex_digits())
    print()
    print(generate_hex_digits(16))

if(__name__=="__main__"):
    main()