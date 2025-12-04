nome_completo= ' ANA CAROLINA SILVA   '
remover= nome_completo.lower().title().strip()
indice_espaco= remover.find(' ')
primeiro_nome= remover.split()
print(f'primeiro nome: {primeiro_nome[0]}')
print(f'Nome limpo: {remover}')
print(f'primeiro espaço: {indice_espaco}')