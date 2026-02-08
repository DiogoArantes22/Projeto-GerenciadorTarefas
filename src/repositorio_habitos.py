import csv
import os
from models import Habito

class RepositorioHabitos:
    def __init__(self, arquivo_csv='data/habitos.csv'):
        self.arquivo_csv = arquivo_csv
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists(self.arquivo_csv):
            with open(self.arquivo_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'nome', 'frequencia', 'contador_execucoes'])

    def salvar(self, habitos):
        with open(self.arquivo_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'nome', 'frequencia', 'contador_execucoes'])
            for habito in habitos:
                writer.writerow([habito.id, habito.nome, habito.frequencia, habito.contador_execucoes])

    def carregar(self):
        habitos = []
        with open(self.arquivo_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                habito = Habito(
                    row['id'], 
                    row['nome'], 
                    row['frequencia'], 
                    int(row['contador_execucoes'])
                )
                habitos.append(habito)
        return habitos
