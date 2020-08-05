#2nd and 4th largest number in a list
n = int(input("Enter number of elements : "))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
a.sort()
print(a)
print(" 2nd large number is {0}, 4th large number {1} ".format(a[-2],a[-4]))