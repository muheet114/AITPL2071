m,n,i,j,flag=0,0,0,0,0
m = input("Enter from : ")
n = input("Enter to : ")
# Print display message
print("Prime numbers between", n, "and",
      m, "are:", end="")
for i in range(m, n +1):
    if ( i == 1 ):
        continue
    flag=1;
    for j in range(2,i // 2+1):
        if(i % j == 0):
            flag=0
            break
    if (flag == 1):
        print(i, end=" ")
