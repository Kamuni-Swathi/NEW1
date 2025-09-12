while True:
    n = int(input("enter a number:"))
    if(n==0):
        print("Thank you!!!")
        break
    else:
        for i in range(1,11):
            x = n*i
            print(f" {n} * {i} = {x}")
# uploading to git Hub