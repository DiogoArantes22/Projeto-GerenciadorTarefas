# repositorio_habitos.py

import os
from models import Habito


class RepositorioHabitos:
    def __init__(self, arquivo_csv="data/habitos.csv"):
        self.arquivo_csv = arquivo_csv
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(self.arquivo_csv):
            with open(self.arquivo_csv, "w", encoding="utf-8") as f:
                f.write("id,nome,frequencia,contador_execucoes\n")

    def salvar(self, habitos):
        with open(self.arquivo_csv, "w", encoding="utf-8") as f:
            f.write("id,nome,frequencia,contador_execucoes\n")
            for habito in habitos:
                linha = f"{habito.id},{habito.nome},{habito.frequencia},{habito.contador_execucoes}\n"
                f.write(linha)

    def carregar(self):
        habitos = []

        if not os.path.exists(self.arquivo_csv):
            return habitos

        with open(self.arquivo_csv, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        for linha in linhas[1:]:
            linha = linha.strip()
            if not linha:
                continue

            dados = linha.split(",")
            while len(dados) < 4:
                dados.append("")

            id_habito = dados[0]
            nome = dados[1]
            frequencia = dados[2]

            contador_txt = dados[3].strip()
            contador = int(contador_txt) if contador_txt.isdigit() else 0

            habitos.append(Habito(id_habito, nome, frequencia, contador))

        return habitos
