# Loops e repetições
# for = repetições definidas
# while = repetições definidas ou infinitas

"""notas = []

matricula = input("Mat: ")
nota= float(input("Nota: "))
resultado = [matricula, nota]
notas.append(resultado)"""
"""Isso acima, deve ser repetido para todos os alunos/funcionários (errado/trabalhoso)"""

# Usando as funções

"""notas = []

for x in range(5):
    matricula = input("Mat: ")
    nota = float(input("Nota: "))
    resultado = (matricula, nota)
    notas.append(resultado)
print("quantidade de notas", len(notas))

for n in notas:
    matricula = n[0]
    nota = n[1]
    print("O aluno", matricula,  "tirou a nota: ", nota)"""

# Usando While 

notas = []

contador = 1

while contador <= 5:
    matricula = input("Mat: ")
    nota = float(input("Nota: "))
    resultado = [matricula, nota]
    notas.append(resultado)

    # alternativa: contador = +1
    contador = contador + 1

print("Quantidade de notas", len(notas))