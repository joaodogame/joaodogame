p= int(input())
d_1= int(input())
d_2= int(input())
num= 0

if p == 0:
    if d_1 % 2 == 0:
        num= 0
    else:
        num= 1
elif p == 1:
    if d_2 % 2 == 0:
        num= 1
    else:
        num= 0

print(num) #printando o valor que representa o ganhador