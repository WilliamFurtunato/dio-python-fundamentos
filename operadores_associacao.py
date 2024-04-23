# verificar se está presente em uma sequencia

curso = "Curso de Python"
frutas = ["laranja", "uva", "limao"]
saques = [1500, 100]

print("python" in curso) # False -> CASE SENSITIVE
print("Python" in curso) # True
print("maça" not in frutas) # True
print(200 in saques) # False