class Tarefa:
    """
    Representa uma tarefa individual no sistema.
    """
    def __init__(self, id_tarefa, titulo, descricao, data_limite, concluida=False):
        self.id = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.data_limite = data_limite
        self._concluida = concluida

    @property
    def concluida(self):
        return self._concluida

    def marcar_concluida(self):
        self._concluida = True

    def __str__(self):
        status = "[X]" if self.concluida else "[ ]"
        return f"{status} ID: {self.id} | {self.titulo} (Até: {self.data_limite})"

class Habito:
    """
    Representa um hábito recorrente.
    """
    def __init__(self, id_habito, nome, frequencia, contador_execucoes=0):
        self.id = id_habito
        self.nome = nome
        self.frequencia = frequencia # Diário ou Semanal
        self._contador_execucoes = int(contador_execucoes)

    @property
    def contador_execucoes(self):
        return self._contador_execucoes

    def registrar_execucao(self):
        """Incrementa o contador de execuções do hábito."""
        self._contador_execucoes += 1

    def __str__(self):
        return f"ID: {self.id} | Hábito: {self.nome} ({self.frequencia}) | Execuções: {self.contador_execucoes}"
