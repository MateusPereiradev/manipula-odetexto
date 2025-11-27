frase= str(input('Digite aqui uma frase:')).strip().lower()
print(f'Referente a frase, quantas vezes aparece a letra a: {frase.count('a')}')
print(f'A primeira letra a aparece: {frase.find('a')+1}')
print(f'A ultima letra a aparece: {frase.rfind('a')+1}')
'''
Faça um programa que leia uma frase pelo teclado e mostre:
>Quantas vez aparece a letra 'A'
>Em que posição ela aparece a primeira vez
>Em que posição ela aparece a última vez

'''