nome= str(input('Digite aqui seu nome completo:')).strip()
nome_maiusculo= nome.upper()
print(f'O nome em letras maiúsculas é {nome_maiusculo}')
nome_minusculo= nome.lower()
print(f'O nome em letras minúsculas é {nome_minusculo}')
letras= len(nome.replace(' ', ''))
print(f'A contagem do nome completo, retirando os espaços é de {letras}')
nome_lista= nome.split()
print(f'O primeiro nome contém {len(nome_lista[0])} letras')
'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas as letas minúsculas;
Quantas letras ao todo (sem considerar espaços);
Quantas letras tem o primeiro nome;
'''
