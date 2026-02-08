# main.py

from models import Tarefa, Habito
from repositorio_tarefas import RepositorioTarefas
from repositorio_habitos import RepositorioHabitos
import relatorios


def exibir_menu():
    print("\n" + "=" * 40)
    print("   GERENCIADOR DE TAREFAS E HÁBITOS")
    print("=" * 40)
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
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return False

    print("\nTarefas disponíveis:")
    for tarefa in tarefas:
        status = "✓" if tarefa.concluida else " "
        print(f"  ID: {tarefa.id} | [{status}] {tarefa.titulo}")
    return True


def listar_ids_habitos(habitos):
    if not habitos:
        print("\nNenhum hábito cadastrado.")
        return False

    print("\nHábitos disponíveis:")
    for habito in habitos:
        print(f"  ID: {habito.id} | {habito.nome}")
    return True


def gerar_novo_id(lista_objetos):
    # IDs são strings, mas numéricos
    maior = 0
    for obj in lista_objetos:
        try:
            n = int(obj.id)
            if n > maior:
                maior = n
        except ValueError:
            pass
    return str(maior + 1)


def buscar_por_id(lista_objetos, id_busca):
    for obj in lista_objetos:
        if obj.id == id_busca:
            return obj
    return None


def main():
    repo_tarefas = RepositorioTarefas()
    repo_habitos = RepositorioHabitos()

    tarefas = repo_tarefas.carregar()
    habitos = repo_habitos.carregar()

    # Reconstrói tarefas vinculadas após carregar
    for habito in habitos:
        habito.tarefas_vinculadas = []
        for tarefa in tarefas:
            if tarefa.id_habito_vinculado == habito.id:
                habito.adicionar_tarefa(tarefa)

    while True:
        opcao = exibir_menu()

        # 1 - Cadastrar tarefa
        if opcao == "1":
            id_tarefa = gerar_novo_id(tarefas)
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            data = input("Data limite: ")

            tarefas.append(Tarefa(id_tarefa, titulo, descricao, data))
            repo_tarefas.salvar(tarefas)
            print("Tarefa cadastrada!")

        # 2 - Listar tarefas
        elif opcao == "2":
            print("\n--- TODAS AS TAREFAS ---")
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for tarefa in tarefas:
                    print(tarefa)

        # 3 - Concluir tarefa
        elif opcao == "3":
            if not listar_ids_tarefas(tarefas):
                continue

            id_busca = input("ID da tarefa a concluir: ")
            tarefa = buscar_por_id(tarefas, id_busca)

            if tarefa:
                tarefa.marcar_concluida()
                repo_tarefas.salvar(tarefas)
                print("Tarefa concluída!")
            else:
                print("ID não encontrado.")

        # 4 - Editar tarefa
        elif opcao == "4":
            if not listar_ids_tarefas(tarefas):
                continue

            id_busca = input("ID da tarefa a editar: ")
            tarefa = buscar_por_id(tarefas, id_busca)

            if tarefa:
                print("(Deixe em branco para não alterar)")
                novo_titulo = input(f"Novo título [{tarefa.titulo}]: ")
                nova_desc = input(f"Nova descrição [{tarefa.descricao}]: ")
                nova_data = input(f"Nova data [{tarefa.data_limite}]: ")
                tarefa.editar(novo_titulo, nova_desc, nova_data)
                repo_tarefas.salvar(tarefas)
                print("Tarefa atualizada!")
            else:
                print("ID não encontrado.")

        # 5 - Excluir tarefa
        elif opcao == "5":
            if not listar_ids_tarefas(tarefas):
                continue

            id_busca = input("ID da tarefa a excluir: ")
            tarefa = buscar_por_id(tarefas, id_busca)

            if tarefa:
                # Se estava vinculada a um hábito, remove do hábito também
                if tarefa.id_habito_vinculado is not None:
                    hab = buscar_por_id(habitos, str(tarefa.id_habito_vinculado))
                    if hab:
                        # remove a tarefa da lista vinculada
                        novas = []
                        for t in hab.tarefas_vinculadas:
                            if t.id != tarefa.id:
                                novas.append(t)
                        hab.tarefas_vinculadas = novas

                tarefas.remove(tarefa)
                repo_tarefas.salvar(tarefas)
                print("Tarefa removida!")
            else:
                print("ID não encontrado.")

        # 6 - Cadastrar hábito
        elif opcao == "6":
            id_habito = gerar_novo_id(habitos)
            nome = input("Nome do hábito: ")
            freq = input("Frequência: ")

            habitos.append(Habito(id_habito, nome, freq))
            repo_habitos.salvar(habitos)
            print("Hábito cadastrado!")

        # 7 - Listar hábitos
        elif opcao == "7":
            print("\n--- TODOS OS HÁBITOS ---")
            if not habitos:
                print("Nenhum hábito cadastrado.")
            else:
                for habito in habitos:
                    print(habito)

        # 8 - Registrar execução de hábito
        elif opcao == "8":
            if not listar_ids_habitos(habitos):
                continue

            id_busca = input("ID do hábito executado: ")
            habito = buscar_por_id(habitos, id_busca)

            if habito:
                habito.registrar_execucao()
                repo_habitos.salvar(habitos)
                print("Execução registrada!")
            else:
                print("ID não encontrado.")

        # 9 - Editar hábito
        elif opcao == "9":
            if not listar_ids_habitos(habitos):
                continue

            id_busca = input("ID do hábito a editar: ")
            habito = buscar_por_id(habitos, id_busca)

            if habito:
                print("(Deixe em branco para não alterar)")
                novo_nome = input(f"Novo nome [{habito.nome}]: ")
                nova_freq = input(f"Nova frequência [{habito.frequencia}]: ")
                habito.editar(novo_nome, nova_freq)
                repo_habitos.salvar(habitos)
                print("Hábito atualizado!")
            else:
                print("ID não encontrado.")

        # 10 - Excluir hábito
        elif opcao == "10":
            if not listar_ids_habitos(habitos):
                continue

            id_busca = input("ID do hábito a excluir: ")
            habito = buscar_por_id(habitos, id_busca)

            if habito:
                # Desvincula tarefas que apontavam para esse hábito
                for tarefa in tarefas:
                    if tarefa.id_habito_vinculado == habito.id:
                        tarefa.id_habito_vinculado = None

                habitos.remove(habito)
                repo_habitos.salvar(habitos)
                repo_tarefas.salvar(tarefas)
                print("Hábito removido!")
            else:
                print("ID não encontrado.")

        # 11 - Vincular tarefa a hábito
        elif opcao == "11":
            if not listar_ids_tarefas(tarefas):
                continue
            if not listar_ids_habitos(habitos):
                continue

            id_tarefa = input("ID da Tarefa: ")
            id_habito = input("ID do Hábito: ")

            tarefa_obj = buscar_por_id(tarefas, id_tarefa)
            habito_obj = buscar_por_id(habitos, id_habito)

            if tarefa_obj and habito_obj:
                tarefa_obj.id_habito_vinculado = habito_obj.id
                habito_obj.adicionar_tarefa(tarefa_obj)  # não duplica
                repo_tarefas.salvar(tarefas)
                print("Vínculo realizado!")
            else:
                print("IDs não encontrados.")

        # 12 - Relatórios
        elif opcao == "12":
            relatorios.gerar_relatorio_tarefas(tarefas)
            relatorios.gerar_relatorio_habitos(habitos)

        # 0 - Sair
        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
