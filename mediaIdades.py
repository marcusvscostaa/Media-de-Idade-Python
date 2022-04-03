idades=[ ]
cont=0
soma=0
media=0
grupo= int(input('Quantas pessoas ?'))

while cont <grupo:
	cont = cont + 1
	idade = int(input(f'{cont}- Adicione a idade:'))
	idades.append(idade)
	
print(f'Lista de idades: {idades}')
soma = sum(idades)
print(f'Soma das idades: {soma}')
media = soma/cont
print(f'Media das idades: {media}')