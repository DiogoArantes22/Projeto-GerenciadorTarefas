"""
MÓDULO DE MODELOS (models.py)
Inclui métodos para edição de atributos.
"""

class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao, data_limite, concluida=False, id_habito_vinculado=None):
        self.id = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.data_limite = data_limite
        self._concluida = concluida
        self.id_habito_vinculado = id_habito_vinculado

    @property
    def concluida(self):
        return self._concluida

    def marcar_concluida(self):
        self._concluida = True

    def editar(self, novo_titulo=None, nova_desc=None, nova_data=None):
        """Método para atualizar os dados da tarefa."""
        if novo_titulo: self.titulo = novo_titulo
        if nova_desc: self.descricao = nova_desc
        if nova_data: self.data_limite = nova_data

    def __str__(self):
        status = "[X]" if self.concluida else "[ ]"
        return f"{status} ID: {self.id} | {self.titulo} (Até: {self.data_limite})"


class Habito:
    def __init__(self, id_habito, nome, frequencia, contador_execucoes=0):
        self.id = id_habito
        self.nome = nome
        self.frequencia = frequencia
        self._contador_execucoes = int(contador_execucoes)
        self.tarefas_vinculadas = []

    @property
    def contador_execucoes(self):
        return self._contador_execucoes

    def registrar_execucao(self):
        self._contador_execucoes += 1

    def editar(self, novo_nome=None, nova_freq=None):
        """Método para atualizar os dados do hábito."""
        if novo_nome: self.nome = novo_nome
        if nova_freq: self.frequencia = nova_freq

    def adicionar_tarefa(self, tarefa_objeto):
        self.tarefas_vinculadas.append(tarefa_objeto)

    def __str__(self):
        txt = f"HÁBITO: {self.nome} (ID: {self.id}) |Frequencia: {self.frequencia} | Execuções: {self.contador_execucoes}\n"
        if self.tarefas_vinculadas:
            txt += "  └── Tarefas de Apoio:\n"
            for tarefa in self.tarefas_vinculadas:
                status = "✓" if tarefa.concluida else " "
                txt += f"      [{status}] {tarefa.titulo}\n"
        else:
            txt += "  └── (Nenhuma tarefa vinculada)\n"
        return txt
