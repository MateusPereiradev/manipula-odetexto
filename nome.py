nome= str(input('Digite aqui seu nome completo:')).strip()
print(f'Seu nome em maiúsculas é {nome.upper()}!')
print(f'Seu nome em minúsculas é {nome.lower()}!')
print(f'Seu nome tem ao todo sem considerar espaços {len(nome.replace(' ',''))} letras!')
nome_lista= nome.split()
print(f'Seu primeiro nome tem {len(nome_lista[0])} letras!')
print('Fim do programa!')

'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas as letas minúsculas;
Quantas letras ao todo (sem considerar espaços);
Quantas letras tem o primeiro nome;
'''
