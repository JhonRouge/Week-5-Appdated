#for demo

num =int(input("Enter a number: "))

#for i in range(num): #starts at 0 (Default)
#for i in range(1, num+1): #starts at 1
for i in range (0, num, 2): #Skips every 2 number
    print(i)