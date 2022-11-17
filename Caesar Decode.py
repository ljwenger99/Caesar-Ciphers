#Lucas Wenger
#15 July 2020
#Caesar Cypher Decoder
#This is just a basic manual decoder, meaning you go through
#all 25 possibilities and identify yourself which one is decoded. 

def caesardecode(string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    success = False
    tempcode = string.upper()
    while success == False:
        testcode = ""
        user = 0
        for char in tempcode:
            if char in alphabet:
                if char == alphabet[25]:
                    testcode += alphabet[0]
                else:
                    testcode += alphabet[alphabet.index(char)+1]
            else:
                testcode += char
        print(testcode)
        while user not in ["y","n"]:
            user = input("\nIs this message decoded? Answer y/n.")
        if user == "y":
            return
        else:
            tempcode = testcode
            continue
