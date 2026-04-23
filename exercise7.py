# Arthur Mozzoni
# COP2002.0M1
# 4/12/2026
# Hex digit generator
# generate hex digits for IP addresses
from random import randint


def decToHexTranslator(decimalNum):
    # Take a decimal number and translate it to hexadecimal
    hexDigits = "0123456789ABCDEF"
    finalHex = ""
    
    if decimalNum == 0:
        return "0"
    while decimalNum > 0:
        remainder = decimalNum % 16
        finalHex = hexDigits[remainder] + finalHex
        decimalNum = decimalNum // 16
 
    return finalHex


# Below is the
#   (1)Name         (2)parameter and (4)defualt arguement(which is 6)
def generate_hex_digits(number=6):
    # Create a list with number amount of hexadecimal numbers
    finishedAddress = []
    
    for i in range(0,number):
        randomNum = randint(0,32)        #RandomNum is an argument
        addressGroup = decToHexTranslator(randomNum)
        
        if randomNum < 16:
            finishedAddress.append(f"0{addressGroup}")
        else:
            finishedAddress.append(f"{addressGroup}")
    
        
    return finishedAddress
# (5)finishedAddress is a return value
# (6)Lines 26-40 is the definition for the function generate_hex_digits


def main():
    # Run the main block of code for the file
    listForMAC = generate_hex_digits()
    listForIPV6 = generate_hex_digits(16) 
    # (3&7) The 16 is an argument being passed into the function call generate_hex_digits
    
    print("Generating random MAC address...")
    for i in range(len(listForMAC)):
        if i == len(listForMAC) -1:
            print(listForMAC[i])
        else:
            print(listForMAC[i],end=":")
    
    print("\nGenerating random IPV6 address...")
    for i in range(0,len(listForIPV6),2):
        pair = listForIPV6[i]+listForIPV6[i+1]
        if i == len(listForIPV6) -2:
            print(pair)
        else:
            print(pair, end=":")
    
    
    
    

if __name__ == "__main__":
    main()