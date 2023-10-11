s = ""
length = 0
final = 0
found = False
s = input("Please enter a Sentence: ")
length = len(s)

for x in reversed(range(length)):
    if (s[x] == " " and found == True):
        break
    if (s[x].isalpha()):
        final = final + 1
        found = True
    
print( "Total Letters for final word is {}".format(final))
