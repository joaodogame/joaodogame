#variaveis:
jog1= int(input())
jog2= int(input())
jog3= int(input())
#condições:
if jog1 != jog2 and jog1 != jog3:
    print("jog1")
elif jog2 != jog1 and jog2 != jog3:
    print("jog2")
elif jog3 != jog1 and jog3 != jog1:
    print("jog3")
else:
    print("empate")
