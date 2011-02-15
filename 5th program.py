m=int(input("Enter the range form :"))
n=int(input("Enter the range to : "))
for num in range(m,n + 1):
    if num > 1:
        for i in range(2, num):
            if(num%1) == 0:
                break
            else:
                print(num)