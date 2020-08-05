#menu driven program
def add(x,y):
  return(x+y)
def sub(x,y):
  return(x-y)
def mul(x,y):
  return(x*y)
def div(x,y):
  return(x/y)
def mod(x,y):
  return(x%y)
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
choice=int(input("Enter your choice : "))
if choice == 1:
  a=int(input("Enter first number : "))
  b=int(input("Enter second number : "))
  print(a, " + ", b , "=",add(a,b))

elif choice == 2:
  a=int(input("Enter first number : "))
  b=int(input("Enter second number : "))
  print(a, " - ", b , "=",sub(a,b))
elif choice == 3:
  a=int(input("Enter first number : "))
  b=int(input("Enter second number : "))
  print(a, " * ", b , "=",mul(a,b))
elif choice == 4:
  a=int(input("Enter first number : "))
  b=int(input("Enter second number : "))
  print(a, " / ", b , "=",div(a,b))
elif choice == 5:
  a=int(input("Enter first number : "))
  b=int(input("Enter second number : "))
  print(a, " % ", b , "=",mod(a,b))
else:
  print("Invaid choice")