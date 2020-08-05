#program to check if the sting is palindrome
my_str=str(input("Enter a String to check if it is palindrome : "))
my_str = my_str.casefold()
rev_str= reversed(my_str)
if list(my_str)==list(rev_str):
  print("the string is palindrome")
else:
  print("the string is not a palindrome")