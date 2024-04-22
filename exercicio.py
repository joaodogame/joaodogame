#variaveis:
ch1= float(input())
ch2= input()
valor= float(input())
#casos:
if ch1 == valor or ch2 != "m":
    print("primeiro")
elif ch1 < valor and ch2 == "m":
    print("segundo")
elif ch1 == valor or ch2 != "M":
    print("primeiro")
elif ch1 < valor and ch2 == "M":
    print("segundo")
