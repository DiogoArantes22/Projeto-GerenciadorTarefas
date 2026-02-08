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
                # Adicionamos a coluna 'id_habito' para salvar a relação
                writer.writerow(['id', 'titulo', 'descricao', 'data_limite', 'concluida', 'id_habito'])

    def salvar(self, tarefas):
        with open(self.arquivo_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'titulo', 'descricao', 'data_limite', 'concluida', 'id_habito'])
            for tarefa in tarefas:
                # Salvamos o ID do hábito vinculado (pode ser None)
                writer.writerow([tarefa.id, tarefa.titulo, tarefa.descricao, tarefa.data_limite, tarefa.concluida, tarefa.id_habito_vinculado])

    def carregar(self):
        tarefas = []
        if not os.path.exists(self.arquivo_csv): return tarefas
        with open(self.arquivo_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tarefa = Tarefa(
                    row['id'], 
                    row['titulo'], 
                    row['descricao'], 
                    row['data_limite'], 
                    row['concluida'] == 'True',
                    row.get('id_habito') # Carregamos o vínculo
                )
                tarefas.append(tarefa)
        return tarefas
