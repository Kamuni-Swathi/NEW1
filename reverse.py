n = int(input("Enter a number:"))
res = 0
while(n!=0):
    rem = n%10
    res = res*10 +rem
    n = n//10
print(f"Reverse of num is: {res}")    