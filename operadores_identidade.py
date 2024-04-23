# Ocupam o mesmo local na memoria ?

saldo = 1000
limite = 500
saldo_2 = 1000

print(saldo is limite) # False
print(saldo is not limite) # True

print(saldo is saldo_2) # True