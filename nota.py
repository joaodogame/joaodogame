#variaveis:
b=int(input())
t=int(input())
#calculos:
triangulo= (abs(b-t)*70)/2
retangulo= min(b,t)*70
area_felix=triangulo + retangulo
#condições:
if area_felix > 5600:
    print(1)
elif area_felix < 5600:
    print(2)
else:
    print(0)