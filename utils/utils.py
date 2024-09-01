import csv  #biblioteca para ler e escrever em um arquivo no formato csv

def ler_csv(arquivo_csv):
    dados_csv = []                                              #cria uma lista em branco
    try:                                                        #tratamento de erro
        with open(arquivo_csv, newline='') as massa:            #com o arquivo --> informar o nome e o apelido da massa
                                                                #newline = caracter de final de linha
            tabela = csv.reader(massa, delimiter =',')         #com os dados do arquivo, menos o cabeçalho, 
                                                                #informando que o separador é a virgula
            next(tabela)                                        #serve para pular a linha 
            for linha in tabela:                                #para cada linha na tabela
                dados_csv.append(linha)                         #guardando os dados separados para uso
        return dados_csv                                        #devolver os dados separados para uso
    except FileNotFoundError:                                   #tratamento de erro para arquivo nao encontrado
        print(f'Arquivo não encontrado: {arquivo_csv}')         #mensagem de erro de arquivo nao encontrado
    except Exception as fail:                                   #qualquer erro não previsto
        print(f'Falha na leitura do arquivo:{fail}')            #mensagem de erro que voltará do sistema        