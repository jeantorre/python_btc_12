import pandas as pd


class ProcessarCsv:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtra_por(self, coluna: str, atributo: str):
        """
        Retorna um DataFrame a partir de um filtro
        de coluna e atributo selecionado
        """
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return self.df_filtrado

    def sub_filtra_por(self, coluna: str, atributo: str):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo]


if __name__ == "__main__":
    caminho_csv = "src/exemplo.csv"
    # filtro = "estado"
    # atributo = "SP"

    arquivo_csv = ProcessarCsv(caminho_csv)
    arquivo_csv.carregar_csv()
    # print(arquivo_csv.df.columns)
    print(arquivo_csv.filtra_por(coluna="estado", atributo="SP"))
    print(arquivo_csv.sub_filtra_por(coluna="preco", atributo=10.50))
