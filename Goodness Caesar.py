#Lucas Wenger
#Goodnes Caesar returns the most likely plaintext for a message encoded using a caesar cipher according to the frequency with which
#letters appear in the English language. 

def GoodnessCaesar(ctext):
   letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
   alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0'
   goodnessval = []
   for S in range(0,27):
      tempvar = 0
      for i in "".join(ctext.upper().split()):
         tempvar += letterGoodness[((ord(i)-65)-S) % 25]
      goodnessval.append(tempvar)
   tempstr = ''
   for i in ctext.upper():
      if i not in alphabet:
         tempstr += i
      else:
         tempstr += alphabet[(alphabet.index(i) - goodnessval.index(max(goodnessval))) % 26]
   return tempstr
