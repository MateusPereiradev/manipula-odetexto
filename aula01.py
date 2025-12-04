frase= "Curso em Vídeo Python"
print(frase[9])#vai me mostrar só o 9 carácter
print(frase[9:13])#de 9 até o 13
print(frase[9:21:2]) #de 9 até 21 pulando de 2 em 2
print(frase[9:])#vai do caractere 9 até o final como se fosse 9 até o final
print(frase[:21])#é como se fosse de 0 até o 20
print(frase[9::3])# de nove até o final vai pular de 3 em 3.print
print(len(frase)) #qual é o comprimento da frase.
print(frase.count('o'))#quantas vezes aparece a letra 'o' minuscula.
print(frase.count('o', 0, 13))#contar quantos 'o' tem de 0 a 13.
print(frase.find('deo'))#O método find() retorna o índice (posição) da primeira ocorrência da substring procurada.
print(frase.rfind('a')) #o R significa reverse, então ele vai mostrar o primeiro 'a' de trás pra frente
print(frase.find('Android'))#se você coloca dentro do find uma str que não existe ele retorna -1
print('curso' in frase)#existe a palavra curso dentro de frase(retorna True se tiver e False se não)
print(frase.replace('Python', 'android'))#ele substitui python por android(não substitui diretamente na str)
print(frase.upper())#pra cima, vão ficar em maiúsculas, não se esqueça do parenteses após o método.
print(frase.lower())#pra baixo, vão ficar tudo em minúscula, não se esqueça dos parentes.
print(frase.capitalize())#vai jogar todos os caracteres em minusculo, e só o primeiro caractere fica em maiúsculo.
print(frase.title())#ele analisa quantas palavras tem a str e coloca maiúscula o primeiro caractere de cada palavra, ele identifica elas através dos espaços.
print(frase.strip())#remove os espaços inúteis, tanto no ínicio quanto no final.
print(frase.rstrip())#remove todos os espaços da direita
print(frase.lstrip())#remove todos os espaços da esquerda
print(frase.split())#cria uma lista com todas a palavras da str, separa as palavras
print('-'.join(frase.split()))#join é pra juntar uma coisa na outra, juntar todos os elementos da frase e vai usar esse separador '-'.(exemplo)
print(frase.isalpha())