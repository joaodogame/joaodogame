num1= int(input())
num2= int(input())

if num1 % 3 == 0 and num2 % 3 == 0 or num1 % 5 == 0 and num2 % 5 == 0:
    print("sim")
else:
    print("nao")