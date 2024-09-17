# Aprendendo as condicionais

salario = float (input("Informe o salário: "))

if salario <= 3000:
    print ("programador junior")
elif salario > 3000 and salario <= 6000:
    print ("programador pleno")
elif salario > 6000 and salario <= 15000:
    print ("programador senior")
else:
    print ("gerente de projetos")

# Alguns métodos nos permite mudar listas 

""" 

.append = Acrescenta um novo item no final da lista [item]
.insert = Insere um novo item na posição dada [posição, item]
.pop = Remove e retorna o último item []
.pop = Remove e retorna o item da posição [posição]
.sort = Ordena a lista []
.reverse = Ordena em oredem reversa []
.index = Retorna a posição da primeira ocorrência do item [item]
.count = Retorna o número de ocorrências do item [item]
.remove = Remove a primeira ocorência do item [item]

"""