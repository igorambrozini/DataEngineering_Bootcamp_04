"""3.Lendo arquivos
Para ler um arquivo CSV em Python utilizando o módulo nativo,
você pode usar a combinação do comando with open... para abrir
o arquivo e o método .reader() do módulo csv para ler o arquivo
linha por linha. O uso de with assegura que o arquivo será fechado
corretamente após sua leitura, mesmo que ocorram erros durante o
processo."""

import csv

caminho_arquivo = 'exemplo.csv'

dados = []

with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    
    for linha in leitor_csv:
        dados.append(linha)
        
for registro in dados:
    print(registro)