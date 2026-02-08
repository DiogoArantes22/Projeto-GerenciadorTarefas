from models import Tarefa, Habito
from repositorio_tarefas import RepositorioTarefas
from repositorio_habitos import RepositorioHabitos
import relatorios

def exibir_menu():
    print("\n" + "="*40)
    print("   GERENCIADOR DE TAREFAS E HÁBITOS")
    print("="*40)
    print("1. Cadastrar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Editar Tarefa")
    print("5. Excluir Tarefa")
    print("-" * 20)
    print("6. Cadastrar Hábito")
    print("7. Listar Hábitos")
    print("8. Registrar Execução de Hábito")
    print("9. Editar Hábito")
    print("10. Excluir Hábito")
    print("-" * 20)
    print("11. Vincular Tarefa a um Hábito")
    print("12. Relatórios")
    print("0. Sair")
    return input("Escolha uma opção: ")

def listar_ids_tarefas(tarefas):
    print("\nTarefas disponíveis:")
    for tarefa in tarefas:
        status = "✓" if tarefa.concluida else " "
        print(f"  ID: {tarefa.id} | [{status}] {tarefa.titulo}")

def listar_ids_habitos(habitos):
    print("\nHábitos disponíveis:")
    for habito in habitos:
        print(f"  ID: {habito.id} | {habito.nome}")

def main():
    repo_tarefas = RepositorioTarefas()
    repo_habitos = RepositorioHabitos()
    
    tarefas = repo_tarefas.carregar()
    habitos = repo_habitos.carregar()

    # Sincroniza relações
    for habito in habitos:
        habito.tarefas_vinculadas = [] # Limpa para evitar duplicatas ao recarregar
        for tarefa in tarefas:
            if tarefa.id_habito_vinculado == habito.id:
                habito.adicionar_tarefa(tarefa)

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            id_tarefa = str(max([int(tarefa.id) for tarefa in tarefas] + [0]) + 1)
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            data = input("Data limite: ")
            tarefas.append(Tarefa(id_tarefa, titulo, descricao, data))
            repo_tarefas.salvar(tarefas)
            print("Tarefa cadastrada!")

        elif opcao == "2":
            print("\n--- TODAS AS TAREFAS ---")
            for tarefa in tarefas: print(tarefa)

        elif opcao == "3":
            listar_ids_tarefas(tarefas)
            id_busca = input("ID da tarefa a concluir: ")
            # x quer dizer "para cada x em tarefas, encontre o primeiro que tenha id igual a id_busca, ou None se não encontrar"
            tarefa = next((x for x in tarefas if x.id == id_busca), None)
            if tarefa:
                tarefa.marcar_concluida()
                repo_tarefas.salvar(tarefas)
                print("Tarefa concluída!")
            else: print("ID não encontrado.")

        elif opcao == "4":
            listar_ids_tarefas(tarefas)
            id_busca = input("ID da tarefa a editar: ")
            tarefa = next((x for x in tarefas if x.id == id_busca), None)
            if tarefa:
                print("(Deixe em branco para não alterar)")
                tarefa.editar(
                    input(f"Novo título [{tarefa.titulo}]: "),
                    input(f"Nova descrição [{tarefa.descricao}]: "),
                    input(f"Nova data [{tarefa.data_limite}]: ")
                )
                repo_tarefas.salvar(tarefas)
                print("Tarefa atualizada!")
            else: print("ID não encontrado.")

        elif opcao == "5":
            listar_ids_tarefas(tarefas)
            id_busca = input("ID da tarefa a excluir: ")
            tarefa = next((x for x in tarefas if x.id == id_busca), None)
            if tarefa:
                tarefas.remove(tarefa)
                repo_tarefas.salvar(tarefas)
                print("Tarefa removida!")
            else: print("ID não encontrado.")

        elif opcao == "6":
            id_habito = str(max([int(habito.id) for habito in habitos] + [0]) + 1)
            nome = input("Nome do hábito: ")
            freq = input("Frequência: ")
            habitos.append(Habito(id_habito, nome, freq))
            repo_habitos.salvar(habitos)
            print("Hábito cadastrado!")

        elif opcao == "7":
            print("\n--- TODOS OS HÁBITOS ---")
            for habito in habitos: print(habito)

        elif opcao == "8":
            listar_ids_habitos(habitos)
            id_busca = input("ID do hábito executado: ")
            habito = next((x for x in habitos if x.id == id_busca), None)
            if habito:
                habito.registrar_execucao()
                repo_habitos.salvar(habitos)
                print("Execução registrada!")
            else: print("ID não encontrado.")

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

        elif opcao == "10":
            listar_ids_habitos(habitos)
            id_busca = input("ID do hábito a excluir: ")
            habito = next((x for x in habitos if x.id == id_busca), None)
            if habito:
                # Remove vínculo das tarefas antes de excluir o hábito
                for tarefa in tarefas:
                    if tarefa.id_habito_vinculado == habito.id:
                        tarefa.id_habito_vinculado = None
                habitos.remove(habito)
                repo_habitos.salvar(habitos)
                repo_tarefas.salvar(tarefas)
                print("Hábito removido!")
            else: print("ID não encontrado.")

        elif opcao == "11":
            listar_ids_tarefas(tarefas)
            listar_ids_habitos(habitos)
            id_tarefa = input("\nID da Tarefa: ")
            id_habito = input("ID do Hábito: ")
            tarefa_obj = next((x for x in tarefas if x.id == id_tarefa), None)
            habito_obj = next((x for x in habitos if x.id == id_habito), None)
            if tarefa_obj and habito_obj:
                tarefa_obj.id_habito_vinculado = habito_obj.id
                habito_obj.adicionar_tarefa(tarefa_obj)
                repo_tarefas.salvar(tarefas)
                print("Vínculo realizado!")
            else: print("IDs não encontrados.")

        elif opcao == "12":
            relatorios.gerar_relatorio_tarefas(tarefas)
            relatorios.gerar_relatorio_habitos(habitos)

        elif opcao == "0":
            break
        else: print("Opção inválida.")

if __name__ == "__main__":
    main()
