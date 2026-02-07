import csv
import os
from models import Tarefa

class RepositorioTarefas:
    def __init__(self, arquivo_csv='data/tarefas.csv'):
        self.arquivo_csv = arquivo_csv
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists(self.arquivo_csv):
            with open(self.arquivo_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'titulo', 'descricao', 'data_limite', 'concluida'])

    def salvar(self, tarefas):
        with open(self.arquivo_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'titulo', 'descricao', 'data_limite', 'concluida'])
            for t in tarefas:
                writer.writerow([t.id, t.titulo, t.descricao, t.data_limite, t.concluida])

    def carregar(self):
        tarefas = []
        with open(self.arquivo_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                t = Tarefa(
                    row['id'], 
                    row['titulo'], 
                    row['descricao'], 
                    row['data_limite'], 
                    row['concluida'] == 'True'
                )
                tarefas.append(t)
        return tarefas
