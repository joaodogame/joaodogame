L= int(input())
C= int(input())

if L % 2 == 0 and L % C == 1:
    print(0)
else:
    print(1)