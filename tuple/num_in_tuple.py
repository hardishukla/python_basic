#check if a given number exists in a given tuple of numbers
num = tuple(map(int, input("Enter the numbers: ").split()))#input
n = int(input("Enter the number to check: "))#input to check
if n in num: # condition
    print("number exists at index", num.index(n))
else:
    print("Number does not exist")
