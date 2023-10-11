test1 = False

while(test1 == False):
    x = input("Enter a number : ")
    if (x.isdigit() == True):
        test1 = True

length = len(str(x))
newnum = 0
for y in reversed(range(length)):
    newdig = int(x[y]) * (10**(y))
    print(newdig)
    newnum = newnum + newdig
print(newnum)
if (int(x) == int(newnum)):
    print("Palindrome")
else:
    print("Not Palindrome")