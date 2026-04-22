# Jackson Beard
# COP2002-0M1
# 04/02/2026
# Exercise 7 Defining own function
# The program will generate a random MAC or IPv6 address.

# Import statement for random functions
from random import randint

def generate_hex_digits(number=6):
    
    '''
    This function takes an integer parameter number and based upon this number 
    generates that many pairs of hexadecimal digits to return either a MAC address or IPv6 address.  
    The default for number is 6 because it will generate a properly formatted MAC address.  
    If number is 16, it will generate a properly formatted IPv6 address.
    '''

    # This constant string stores all the values that can be used in a hexadecimal number.
    HEX = "0123456789ABCDEF" 

    # Empty string to store all pairs of hexadecimal numbers that will be generated.
    address = ""

    if number == 6:
        print("Generating random MAC address...") # Generates a random MAC address when number is 6
        i = 0
        while i < number:
           firstHex = HEX[randint(0,15)]
           secondHex = HEX[randint(0,15)]
           address += firstHex + secondHex + ":" 
           i += 1
    elif number == 16:
        print("Generating random IPv6 address...") # Generates a random IPv6 address whne number is 16
        i = 0
        while i < number / 2:
           firstHex = HEX[randint(0,15)]
           secondHex = HEX[randint(0,15)]
           thirdHex = HEX[randint(0,15)]
           fourthHex = HEX[randint(0,15)]
           address += firstHex + secondHex + thirdHex + fourthHex + ":"
           i += 1
    else:
        print("Error. Invalid value.") # Outputs an error message if number is not 6 or 16
    
    return address[:-1] + "\n" # Returns the generated address without the last colon and adds a newline character


def main():

    print(generate_hex_digits())

if(__name__=="__main__"):
   main()
   