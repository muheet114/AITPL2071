#program to find greatest of 3 numbers
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
c = int(input("Enter 3rd Number : "))
if a > b and a > c:
  print("%d is greater : " %(a))
elif b > a and b > c:
  print("%d is greater : " %(b))
else:
  print("%d is greater : " %(c))