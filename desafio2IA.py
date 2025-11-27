nome_arquivo= 'DocumentoImportante.2025.pdf  '
codigo_limpo= nome_arquivo.lower().rstrip()
ultimo_caracter= codigo_limpo.rfind('.')
termina_pdf= codigo_limpo.endswith('.pdf')
print(f'O arquivo termina em .pdf? {termina_pdf}')
print(f'Aqui está o arquivo limpo: {codigo_limpo}')
print(f'O ponto final está no índice: {ultimo_caracter}')


