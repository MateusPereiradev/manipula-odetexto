<<<<<<< HEAD
frase= str(input("Digite aqui uma frase:")).strip().upper()
print(f"Quantas vezes aparece a letra A? {frase.count('A')}")
print(f"Em que posição ela aparece a primeira vez? {frase.find('A')+1}")
print(f"Em que posição ela aparece pela última vez? {frase.rfind('A')+1}")


=======
frase= str(input('Digite aqui uma frase qualquer:')).strip().upper()
print(f'Referente a frase, a letra A aparece {frase.count('A')}')
print(f'Referente a frase a letra A aparece na {frase.find('A')+1} posição')
print(f'Referente a frase a letra A aparece na ultima vez na posição {frase.rfind('A')+1}')
>>>>>>> 1100eb16bc928c721ad2aff157d52e53e7b33ee8
'''
Faça um programa que leia uma frase pelo teclado e mostre:
>Quantas vez aparece a letra 'A'
>Em que posição ela aparece a primeira vez
>Em que posição ela aparece a última vez

'''