while True:
    num = input("Enter a number:")
    if num.isnumeric():
        num = int(num)
        break

myAst = num-1

for num1 in range(num):
    newline = ""
    for num2 in range(num1, num-1):
        newline = newline + " "

    for newNum in range(myAst, num):
        newline += "*"
    myAst -= 1
    print(newline)