# MÓDULO DE MODELOS (models.py)
# Contém as classes `Tarefa` e `Habito` usadas pelo restante do aplicativo.

class Tarefa:
    # Construtor da classe Tarefa: define atributos básicos de uma tarefa.
    def __init__(self, id_tarefa, titulo, descricao, data_limite, concluida=False, id_habito_vinculado=None):
        # ID único da tarefa (string neste projeto)
        self.id = id_tarefa
        # Título curto descritivo da tarefa
        self.titulo = titulo
        # Descrição mais detalhada (pode ser vazia)
        self.descricao = descricao
        # Data limite em formato string (sem validação específica aqui)
        self.data_limite = data_limite
        # Atributo interno que guarda se a tarefa foi concluída (privado)
        self._concluida = concluida
        # ID do hábito ao qual a tarefa pode estar vinculada (ou None)
        self.id_habito_vinculado = id_habito_vinculado

    @property
    def concluida(self):
        # Propriedade de leitura que retorna o estado de conclusão.
        return self._concluida

    def marcar_concluida(self):
        # Marca a tarefa como concluída alterando a flag interna.
        self._concluida = True

    def editar(self, novo_titulo=None, nova_desc=None, nova_data=None):
        """Método para atualizar os dados da tarefa.

        Os parâmetros são opcionais; se o usuário passar `None` ou string vazia,
        o campo não é alterado (essa lógica é tratada na camada de interação).
        """
        if novo_titulo: self.titulo = novo_titulo
        if nova_desc: self.descricao = nova_desc
        if nova_data: self.data_limite = nova_data

    def __str__(self):
        # Representação textual usada ao imprimir a tarefa.
        status = "[X]" if self.concluida else "[ ]"
        return f"{status} ID: {self.id} | {self.titulo} (Até: {self.data_limite})"


class Habito:
    # Construtor da classe Hábito: armazena informações e contador de execuções.
    def __init__(self, id_habito, nome, frequencia, contador_execucoes=0):
        # ID único do hábito (string)
        self.id = id_habito
        # Nome descritivo do hábito
        self.nome = nome
        # Frequência informada pelo usuário (ex: 'diário', 'semanal')
        self.frequencia = frequencia
        # Contador de execuções (interno), garantimos inteiro
        self._contador_execucoes = int(contador_execucoes)
        # Lista de tarefas de apoio vinculadas a este hábito
        self.tarefas_vinculadas = []

    @property
    def contador_execucoes(self):
        # Retorna o número de vezes que o hábito foi executado
        return self._contador_execucoes

    def registrar_execucao(self):
        # Incrementa o contador de execuções quando o usuário registra uma execução
        self._contador_execucoes += 1

    def editar(self, novo_nome=None, nova_freq=None):
        """Atualiza nome e/ou frequência do hábito se valores forem fornecidos."""
        if novo_nome: self.nome = novo_nome
        if nova_freq: self.frequencia = nova_freq

    def adicionar_tarefa(self, tarefa_objeto):
        # Adiciona um objeto `Tarefa` à lista de tarefas vinculadas.
        self.tarefas_vinculadas.append(tarefa_objeto)

    def __str__(self):
        # Cria uma string legível mostrando nome, frequência e execuções
        txt = f"HÁBITO: {self.nome} (ID: {self.id}) |Frequencia: {self.frequencia} | Execuções: {self.contador_execucoes}\n"
        # Se houver tarefas vinculadas, lista-as com seus status
        if self.tarefas_vinculadas:
            txt += "  └── Tarefas de Apoio:\n"
            for tarefa in self.tarefas_vinculadas:
                status = "✓" if tarefa.concluida else " "
                txt += f"      [{status}] {tarefa.titulo}\n"
        else:
            # Mensagem quando não há tarefas de apoio vinculadas
            txt += "  └── (Nenhuma tarefa vinculada)\n"
        return txt
