nome= str(input('Digite aqui seu nome completo:')).strip().upper()
print(f'O nome com todas as letras maiúsculas:{nome}')
print(f'O nome com todas as letras minúsculas:{nome.lower()}')
print(f'Quantas letras tem o nome sem considerar os espaços? {len(nome.replace(' ', ''))}')
nome_lista= nome.split()
print(f'Quantas letras tem o primeiro nome? {len(nome_lista[0])}')


'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas as letas minúsculas;
Quantas letras ao todo (sem considerar espaços);
Quantas letras tem o primeiro nome;
'''
