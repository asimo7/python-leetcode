n = int(input("Enter how many entries: "))
list = []
temp2 = 0
temp3 = 0
sell = 0
check = False
save =0
for i in range(0,n):
    inp = int(input("Price: "))
    list.append(inp)

for x in range (0,n):
    for z in range (x,n):
        sell = list[z] - list[x]
        if (sell > temp2):
            temp2 = sell
            check = True
            print(temp2)
    
if(check == False):
    print(0)
elif(check == True):
    print(temp2)