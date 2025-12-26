print("$$$$$$$tm n space complexity$$$$$$$")
print("we are going to add even numbers")
print(" ")
n = int(input("enter the number to stop addition"))
total = 0
for i in range(1,n+1):
    if i % 2 == 0:
        total += i 

print("the sum of even numers is ", total)