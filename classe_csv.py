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

    def filtros_por(self, colunas: list, atributos: list):
        """
        Função que faz múltiplos filtros ao passar uma lista
        de colunas e atributos a serem filtrados
        """
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")

        if len(colunas) == 0:
            return self.df

        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado

        else:
            return self.filtros_por(colunas[1:], atributos[1:])

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
    print("#############################")
    print(arquivo_csv.filtros_por(["estado", "preco"], ["SP", 10.5]))
