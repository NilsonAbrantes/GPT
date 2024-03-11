import pandas
import pandas as pd

def csv_to_dataset(csv_file):
    # Carregar o CSV em um DataFrame do pandas
    df = pd.read_csv(csv_file)

    # Converter o DataFrame em uma estrutura de dados Python desejada
    dataset = df.to_dict(orient='records')

    return dataset

if __name__ == "__main__":
    # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
    arquivo_csv = 'dados.csv'

    # Chame a função para converter o CSV em um dataset Python
    dados_python = csv_to_dataset(arquivo_csv)

    # Agora, você pode usar 'dataset_python' conforme necessário no seu código
    print(dados_python)
