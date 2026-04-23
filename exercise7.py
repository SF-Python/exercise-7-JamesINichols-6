# Thomas Eckenrode
# COP2002.0M1
# March 23, 2026
# exercise7.py (generateMACAddress and generateIPv6Address)
# This program will generate and output a random MAC Address and a random IPv6 address

import random

def generate_hex_digits(number=6):  # This line contains the function definition "def generate_hex_digits(number=6)", the function name "generate_hex_digits", 
                                    # and the parameter "(number=6)" and "6" is the default argument.
    """ Generates a string of hexadecimal digits formatted as either:
    - MAC Address (default of 6 pairs)
    - IPv6 Address (16 pairs)"""

    # variables
    hexDigits="0123456789ABCDEF"
    address=""
    count=0

    # Total number of hex characters needed
    totalDigits=number*2

    # This determines the grouping size
    if number==6:
        groupSize=2
    else:
        groupSize=4

    # This generates the hex digits
    while count<totalDigits:
        address+=hexDigits[random.randint(0,15)]
        count+=1

        # This adds colons at the correct intervals
        if count % groupSize==0 and count<totalDigits:
            address+=":"


    return address  #This is the return statement



def main():
    """Generates and returns the desired MAC and IPv6 addresses"""
    print("Generating random MAC address...")   
    print(generate_hex_digits())
    print()
    print("Generating random IPv6 address...")
    print(generate_hex_digits(16)) 

if(__name__=="__main__"):
    main()








