# Miguel Evangelista
# COP2002-0M1
# Apr 12, 2026
# Exercise5: Loops
# Program generates random MAC Address

from random import randint

def generate_hex_digits(number=6):
    counter=0
    endloop=False
    addressStore="" # adding raw hexadecimals numbers (not formatted with colon in between)

    # Loops until the endloop value turn into False.
    while(not endloop): 
        randomHex=randint(0,15) # random number generator from 0 up to 15 since hexadecimal is up to 15
        
        '''
            if statements that converts and adds the converted/unconverted number to the addressStore variable
            it also append the characters into the addressStore variable
        '''
        if (randomHex==10):
            randomHex="A"
            addressStore+=randomHex
            
        elif (randomHex==11):
            randomHex="B"
            addressStore+=randomHex

        elif (randomHex==12):
            randomHex="C"
            addressStore+=randomHex

        elif (randomHex==13):
            randomHex="D"
            addressStore+=randomHex

        elif (randomHex==14):
            randomHex="E"
            addressStore+=randomHex

        elif (randomHex==15):
            randomHex="F"
            addressStore+=randomHex

        else:
            addressStore+=str(randomHex)

        counter+=1 # Increment the value of counter variable by 1 for the if statement below

        # if statement if number is either 6 or 16 if it is 6, it will generate MAC address and if it is 16, it will generate IPv6 Address.
        if(number == 6):
            if(counter==2):
                addressStore+=":"
                counter=0 # decrement the value to 0 again to reiterate the appending of columns in addressStore variable
            
            # Check if the characters are already exact characters (12 hex numbers and 5 colons, 1 colon each every 2 characters.)
            if(len(addressStore)>16):
                endloop=True

        elif(number == 16):
            if(counter==4):
                addressStore+=":"
                counter=0 # decrement the value to 0 again to reiterate the appending of columns in addressStore variable
            
            # Check if the characters are already exact characters (12 hex numbers and 5 colons, 1 colon each every 2 characters.)
            if(len(addressStore)>39):
                endloop=True

    # output the result removing the extra colon at the end of the MAC address that has been generated randomly.
    return f"{addressStore.rstrip(":")}"

def main():
    print("\nGenerating random MAC address...")
    print(generate_hex_digits())
    
    print("")
    
    print("Generating random IPv6 address...")
    print(generate_hex_digits(16))
    
    print("")

   


if(__name__=="__main__"):
    main()