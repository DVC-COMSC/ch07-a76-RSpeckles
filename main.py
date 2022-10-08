
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

#Checks if num1 is shorter or equal in length to num2. If it is, it will be added first
#if not num2 will be added first
if len(num1) <= len(num2):
    num3 = num1 + num2
else:
    num3 = num2 + num1

print (num3) 
