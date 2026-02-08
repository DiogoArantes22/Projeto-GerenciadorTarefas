# Importa as classes de modelo `Tarefa` e `Habito` do módulo `models`.
# Essas classes representam as estruturas de dados principais do aplicativo.
from models import Tarefa, Habito
# Importa o repositório de tarefas que gerencia leitura/gravação em CSV.
from repositorio_tarefas import RepositorioTarefas
# Importa o repositório de hábitos que gerencia leitura/gravação em CSV.
from repositorio_habitos import RepositorioHabitos
# Importa o módulo de relatórios para gerar resumos de tarefas e hábitos.
import relatorios

def exibir_menu():
    # Exibe o menu principal para o usuário e retorna a opção digitada.
    # Linha abaixo imprime uma quebra de linha seguida de uma linha de separação.
    print("\n" + "="*40)
    # Título do aplicativo
    print("   GERENCIADOR DE TAREFAS E HÁBITOS")
    # Repete a linha de separação
    print("="*40)
    # Opções relacionadas a tarefas
    print("1. Cadastrar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Editar Tarefa")
    print("5. Excluir Tarefa")
    # Pequena divisão visual
    print("-" * 20)
    # Opções relacionadas a hábitos
    print("6. Cadastrar Hábito")
    print("7. Listar Hábitos")
    print("8. Registrar Execução de Hábito")
    print("9. Editar Hábito")
    print("10. Excluir Hábito")
    # Outra divisão visual
    print("-" * 20)
    # Opções de vínculo e relatórios
    print("11. Vincular Tarefa a um Hábito")
    print("12. Relatórios")
    # Opção para sair do programa
    print("0. Sair")
    # Retorna a string digitada pelo usuário para ser processada pelo `main`.
    return input("Escolha uma opção: ")

def listar_ids_tarefas(tarefas):
    # Mostra uma lista enxuta com IDs e títulos das tarefas.
    # Isso facilita ao usuário escolher uma tarefa por ID.
    print("\nTarefas disponíveis:")
    # Para cada objeto `tarefa` na lista `tarefas`...
    for tarefa in tarefas:
        # Definimos um símbolo visual para indicar se está concluída.
        status = "✓" if tarefa.concluida else " "
        # Imprime ID, status e título em formato compacto.
        print(f"  ID: {tarefa.id} | [{status}] {tarefa.titulo}")

def listar_ids_habitos(habitos):
    # Mostra uma lista enxuta com IDs e nomes dos hábitos.
    print("\nHábitos disponíveis:")
    # Itera sobre a lista de hábitos exibindo ID e nome.
    for habito in habitos:
        print(f"  ID: {habito.id} | {habito.nome}")

def main():
    # Cria instâncias dos repositórios que cuidam do armazenamento em CSV.
    repo_tarefas = RepositorioTarefas()
    repo_habitos = RepositorioHabitos()

    # Carrega listas atuais de tarefas e hábitos a partir dos arquivos.
    tarefas = repo_tarefas.carregar()
    habitos = repo_habitos.carregar()

    # Sincroniza as relações entre hábitos e tarefas após o carregamento.
    # Primeiro, zera a lista de tarefas vinculadas para evitar duplicatas
    for habito in habitos:
        habito.tarefas_vinculadas = [] # Limpa para evitar duplicatas ao recarregar
        # Para cada tarefa carregada, se ela referenciar o hábito atual,
        # adicionamos essa tarefa à lista de apoio do hábito.
        for tarefa in tarefas:
            if tarefa.id_habito_vinculado == habito.id:
                habito.adicionar_tarefa(tarefa)

    # Loop principal do aplicativo: processa opções até o usuário sair.
    while True:
        # Pede ao usuário que escolha uma opção do menu.
        opcao = exibir_menu()

        # Opção 1: cadastrar nova tarefa
        if opcao == "1":
            # Calcula novo ID como o maior ID atual + 1 (tratando lista vazia)
            id_tarefa = str(max([int(tarefa.id) for tarefa in tarefas] + [0]) + 1)
            # Solicita dados da tarefa ao usuário
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            data = input("Data limite: ")
            # Cria objeto `Tarefa` e adiciona à lista
            tarefas.append(Tarefa(id_tarefa, titulo, descricao, data))
            # Persiste alterações no repositório
            repo_tarefas.salvar(tarefas)
            print("Tarefa cadastrada!")

        # Opção 2: listar todas as tarefas
        elif opcao == "2":
            print("\n--- TODAS AS TAREFAS ---")
            # Usa o __str__ de Tarefa para imprimir cada uma
            for tarefa in tarefas: print(tarefa)

        # Opção 3: marcar tarefa como concluída
        elif opcao == "3":
            # Mostra IDs para o usuário escolher
            listar_ids_tarefas(tarefas)
            id_busca = input("ID da tarefa a concluir: ")
            # `next` busca a primeira tarefa com o ID informado, ou None
            tarefa = next((x for x in tarefas if x.id == id_busca), None)
            if tarefa:
                # Marca como concluída e salva
                tarefa.marcar_concluida()
                repo_tarefas.salvar(tarefas)
                print("Tarefa concluída!")
            else: print("ID não encontrado.")

        # Opção 4: editar tarefa
        elif opcao == "4":
            listar_ids_tarefas(tarefas)
            id_busca = input("ID da tarefa a editar: ")
            tarefa = next((x for x in tarefas if x.id == id_busca), None)
            if tarefa:
                # Informa que deixar em branco não altera o campo
                print("(Deixe em branco para não alterar)")
                # Chama o método `editar` de `Tarefa` com possíveis novos valores
                tarefa.editar(
                    input(f"Novo título [{tarefa.titulo}]: "),
                    input(f"Nova descrição [{tarefa.descricao}]: "),
                    input(f"Nova data [{tarefa.data_limite}]: ")
                )
                repo_tarefas.salvar(tarefas)
                print("Tarefa atualizada!")
            else: print("ID não encontrado.")

        # Opção 5: excluir tarefa
        elif opcao == "5":
            listar_ids_tarefas(tarefas)
            id_busca = input("ID da tarefa a excluir: ")
            tarefa = next((x for x in tarefas if x.id == id_busca), None)
            if tarefa:
                # Remove da lista em memória e salva
                tarefas.remove(tarefa)
                repo_tarefas.salvar(tarefas)
                print("Tarefa removida!")
            else: print("ID não encontrado.")

        # Opção 6: cadastrar novo hábito
        elif opcao == "6":
            # Calcula novo ID para hábito similarmente às tarefas
            id_habito = str(max([int(habito.id) for habito in habitos] + [0]) + 1)
            nome = input("Nome do hábito: ")
            freq = input("Frequência: ")
            habitos.append(Habito(id_habito, nome, freq))
            repo_habitos.salvar(habitos)
            print("Hábito cadastrado!")

        # Opção 7: listar hábitos
        elif opcao == "7":
            print("\n--- TODOS OS HÁBITOS ---")
            for habito in habitos: print(habito)

        # Opção 8: registrar execução de hábito
        elif opcao == "8":
            listar_ids_habitos(habitos)
            id_busca = input("ID do hábito executado: ")
            habito = next((x for x in habitos if x.id == id_busca), None)
            if habito:
                # Incrementa contador interno de execuções
                habito.registrar_execucao()
                repo_habitos.salvar(habitos)
                print("Execução registrada!")
            else: print("ID não encontrado.")

        # Opção 9: editar hábito
        elif opcao == "9":
            listar_ids_habitos(habitos)
            id_busca = input("ID do hábito a editar: ")
            habito = next((x for x in habitos if x.id == id_busca), None)
            if habito:
                print("(Deixe em branco para não alterar)")
                habito.editar(
                    input(f"Novo nome [{habito.nome}]: "),
                    input(f"Nova frequência [{habito.frequencia}]: ")
                )
                repo_habitos.salvar(habitos)
                print("Hábito atualizado!")
            else: print("ID não encontrado.")

        # Opção 10: excluir hábito
        elif opcao == "10":
            listar_ids_habitos(habitos)
            id_busca = input("ID do hábito a excluir: ")
            habito = next((x for x in habitos if x.id == id_busca), None)
            if habito:
                # Antes de remover o hábito, desconecta tarefas que apontam para ele
                for tarefa in tarefas:
                    if tarefa.id_habito_vinculado == habito.id:
                        tarefa.id_habito_vinculado = None
                habitos.remove(habito)
                # Salva alterações em ambos os repositórios
                repo_habitos.salvar(habitos)
                repo_tarefas.salvar(tarefas)
                print("Hábito removido!")
            else: print("ID não encontrado.")

        # Opção 11: vincular uma tarefa a um hábito
        elif opcao == "11":
            listar_ids_tarefas(tarefas)
            listar_ids_habitos(habitos)
            id_tarefa = input("\nID da Tarefa: ")
            id_habito = input("ID do Hábito: ")
            # Busca objetos correspondentes por ID
            tarefa_obj = next((x for x in tarefas if x.id == id_tarefa), None)
            habito_obj = next((x for x in habitos if x.id == id_habito), None)
            if tarefa_obj and habito_obj:
                # Atualiza referência na tarefa e adiciona tarefa ao hábito
                tarefa_obj.id_habito_vinculado = habito_obj.id
                habito_obj.adicionar_tarefa(tarefa_obj)
                repo_tarefas.salvar(tarefas)
                print("Vínculo realizado!")
            else: print("IDs não encontrados.")

        # Opção 12: gerar relatórios
        elif opcao == "12":
            # Chama funções do módulo `relatorios` para imprimir resumos
            relatorios.gerar_relatorio_tarefas(tarefas)
            relatorios.gerar_relatorio_habitos(habitos)

        # Opção 0: sair
        elif opcao == "0":
            break
        # Opção inválida: informa o usuário
        else: print("Opção inválida.")

if __name__ == "__main__":
    main()
