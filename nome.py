nome= str(input('Digite aqui seu nome completo:')).strip()
print(f'O nome com todas as letras maiúsculas é {nome.upper()}')
print(f'O nome com todas as letras minúsculas é {nome.lower()}')
print(f'O total de letras sem considerar espações é {len(nome.replace(' ', ''))}')
lista_nome= nome.split()
print(f'O primeiro nome tem {len(lista_nome[0])} letras!')

'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas as letas minúsculas;
Quantas letras ao todo (sem considerar espaços);
Quantas letras tem o primeiro nome;
'''
