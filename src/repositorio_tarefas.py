# repositorio_tarefas.py

import os
from models import Tarefa


class RepositorioTarefas:
    def __init__(self, arquivo_csv="data/tarefas.csv"):
        self.arquivo_csv = arquivo_csv
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(self.arquivo_csv):
            with open(self.arquivo_csv, "w", encoding="utf-8") as f:
                f.write("id,titulo,descricao,data_limite,concluida,id_habito\n")

    def salvar(self, tarefas):
        with open(self.arquivo_csv, "w", encoding="utf-8") as f:
            f.write("id,titulo,descricao,data_limite,concluida,id_habito\n")
            for tarefa in tarefas:
                id_habito = "" if tarefa.id_habito_vinculado is None else str(tarefa.id_habito_vinculado)
                linha = (
                    f"{tarefa.id},"
                    f"{tarefa.titulo},"
                    f"{tarefa.descricao},"
                    f"{tarefa.data_limite},"
                    f"{tarefa.concluida},"
                    f"{id_habito}\n"
                )
                f.write(linha)

    def carregar(self):
        tarefas = []

        if not os.path.exists(self.arquivo_csv):
            return tarefas

        with open(self.arquivo_csv, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        # pula cabeçalho
        for linha in linhas[1:]:
            linha = linha.strip()
            if not linha:
                continue

            dados = linha.split(",")
            # garante que tenha 6 campos
            while len(dados) < 6:
                dados.append("")

            id_tarefa = dados[0]
            titulo = dados[1]
            descricao = dados[2]
            data_limite = dados[3]
            concluida = (dados[4] == "True")

            id_habito = dados[5].strip()
            if id_habito == "":
                id_habito = None

            tarefas.append(Tarefa(id_tarefa, titulo, descricao, data_limite, concluida, id_habito))

        return tarefas
