# models.py

class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao, data_limite, concluida=False, id_habito_vinculado=None):
        self.id = str(id_tarefa)
        self.titulo = titulo
        self.descricao = descricao
        self.data_limite = data_limite
        self._concluida = concluida
        self.id_habito_vinculado = id_habito_vinculado  # string ou None

    @property
    def concluida(self):
        return self._concluida

    def marcar_concluida(self):
        self._concluida = True

    def editar(self, novo_titulo="", nova_desc="", nova_data=""):
        if novo_titulo:
            self.titulo = novo_titulo
        if nova_desc:
            self.descricao = nova_desc
        if nova_data:
            self.data_limite = nova_data

    def __str__(self):
        status = "[X]" if self.concluida else "[ ]"
        return f"{status} ID: {self.id} | {self.titulo} (Até: {self.data_limite})"


class Habito:
    def __init__(self, id_habito, nome, frequencia, contador_execucoes=0):
        self.id = str(id_habito)
        self.nome = nome
        self.frequencia = frequencia
        self._contador_execucoes = int(contador_execucoes)
        self.tarefas_vinculadas = []

    @property
    def contador_execucoes(self):
        return self._contador_execucoes

    def registrar_execucao(self):
        self._contador_execucoes += 1

    def editar(self, novo_nome="", nova_freq=""):
        if novo_nome:
            self.nome = novo_nome
        if nova_freq:
            self.frequencia = nova_freq

    def adicionar_tarefa(self, tarefa_objeto):
        # Evita duplicar a mesma tarefa dentro do hábito
        for t in self.tarefas_vinculadas:
            if t.id == tarefa_objeto.id:
                return
        self.tarefas_vinculadas.append(tarefa_objeto)

    def __str__(self):
        txt = (
            f"HÁBITO: {self.nome} (ID: {self.id}) | "
            f"Frequência: {self.frequencia} | Execuções: {self.contador_execucoes}\n"
        )

        if self.tarefas_vinculadas:
            txt += "  └── Tarefas de Apoio:\n"
            for tarefa in self.tarefas_vinculadas:
                status = "✓" if tarefa.concluida else " "
                txt += f"      [{status}] {tarefa.titulo}\n"
        else:
            txt += "  └── (Nenhuma tarefa vinculada)\n"

        return txt
