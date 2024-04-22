#variaveis:
jog1= input()
jog2= input()
#condições:
if jog1 == "R" and jog2 == "S":
    print("jog1")
elif jog1 == "S" and jog2 == "P":
    print("jog1")
elif jog1 == "P" and jog2 == "R":
    print("jog1")
elif jog1 == "R" and jog2 == "P":
    print("jog2")
elif jog1 == "P" and jog2 == "S":
    print("jog2")
elif jog1 == "S" and jog2 == "R":
    print("jog2")
else:
    print("empate")
