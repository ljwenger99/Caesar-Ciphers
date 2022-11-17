#Lucas Wenger
#A collection of Caesar functions made for Into to Python (Fall 2018)
#NOTE: This Caesar decode function can decode a text file

#letters
def letters(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vals = {i:0 for i in alphabet}
    text = text.lower()
    for i in text:
        try:
            vals[i] += 1
        except KeyError:
            continue
    #return vals - COMMENT OUT for list of letters
    listvals = [(x,vals[x]) for x in vals]
    listvals = [(y,x) for (x,y) in listvals]
    listvals.sort(reverse = True)
    letterlist = [y for (x,y) in listvals]
    return letterlist
    
#encode
def caesar(text,shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    codedstr = ''
    for i in text:
        if i in alphabet:
            codedstr += alphabet[(alphabet.index(i) + shift) % 26]
        else:
            codedstr += i
    return codedstr

#check
def checker(text,shift):
    print ('\n' + caesar(text,shift))
    user = input("\nDo you recognize the sample as English?\ny or n\n")
    if user == 'y':
        return True
    if user == 'n':
        return False


#decode
def decode():
    answer = input('Would you like to import a textfile?\ny or n\n')
    if answer == 'y':
        textfile = input('Enter the name of the textfile:\n')
        with open (textfile, 'r+') as f:
            text = f.read()
    elif answer == 'n':
        text = input('Enter text to decode:\n')
    for i in range(26):
        isenglish = checker(text,i)
        if isenglish == True:
            return 
        if isenglish == False:
            continue
    
