numrows = 0
list2 = []
i = 0
temp = 0
numrows = int(input("Enter the amount of rows: "))

while (i < numrows):
    temp = pow(11,i)
    temp = str(temp)
    x = 0
    list1 = []
    while (x < len(temp)):
        list1.append(temp[x])
        x = x + 1
    list2.append(list1)
    i = i + 1
print(list2)