list = []
num = int(input("Enter how many "))
for x in range(0,num):
    enter = int(input())
    list.append(enter)

want = input("Enter a number that can be had when adding the two numbers")

tex = "false"

for x in range(0, num):
    temp1 = list[x]
    if tex == "true":
        break
    for y in range(0, num):
        temp2 = list[y]
        test = int(temp1 + temp2)
        if (int(test) == int(want)):
            print("[", x , "," , y , "]")
            tex = "true"
            break

            