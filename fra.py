frase= str(input('Digite aqui uma frase:')).strip().upper()
print(f'Quantas vezes aparece a letra A? {frase.count('A')}')
print(f'Em que posição ela aparece a primeira vez? {frase.find('A')+1}')
print(f'Em que posição ela aparece a última vez? {frase.rfind('A')+1}')


'''
Faça um programa que leia uma frase pelo teclado e mostre:
>Quantas vez aparece a letra 'A'
>Em que posição ela aparece a primeira vez
>Em que posição ela aparece a última vez

'''