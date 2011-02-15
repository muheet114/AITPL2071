# program to sort words in alphabetical order
s = input("Enter any String : ")
se = s.split()
se.sort()
for word in se:
    print(word)
