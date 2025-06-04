import pandas as pd

# Função para comparar a estrutura dos CSVs
def compare_csv_structure(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    if set(df1.columns) == set(df2.columns):
        print('A estrutura dos arquivos CSV é a mesma.')
    else:
        missing_columns = set(df1.columns) - set(df2.columns)
        additional_columns = set(df2.columns) - set(df1.columns)
        
        if missing_columns:
            print(f'As colunas {missing_columns} estão faltando no novo arquivo.')
        if additional_columns:
            print(f'As colunas {additional_columns} foram adicionadas no arquivo.')

# Chamada da função
compare_csv_structure('dados1.csv', 'dados2.csv')
