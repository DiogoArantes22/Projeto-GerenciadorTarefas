from models import Tarefa, Habito
from repositorio_tarefas import RepositorioTarefas
from repositorio_habitos import RepositorioHabitos
import relatorios

def exibir_menu():
    print("\n=== GERENCIADOR DE TAREFAS E HÁBITOS ===")
    print("1. Cadastrar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Cadastrar Hábito")
    print("5. Listar Hábitos")
    print("6. Registrar Execução de Hábito")
    print("7. Relatórios")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    repo_tarefas = RepositorioTarefas()
    repo_habitos = RepositorioHabitos()
    
    tarefas = repo_tarefas.carregar()
    habitos = repo_habitos.carregar()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            id_tarefa = str(len(tarefas) + 1)
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição: ")
            data = input("Data limite (DD/MM/AAAA): ")
            tarefas.append(Tarefa(id_tarefa, titulo, descricao, data))
            repo_tarefas.salvar(tarefas)
            print("Tarefa cadastrada!")

        elif opcao == "2":
            print("\n--- LISTA DE TAREFAS ---")
            for tarefa in tarefas:
                print(tarefa)

        elif opcao == "3":
            id_busca = input("ID da tarefa a concluir: ")
            encontrada = False
            for tarefa in tarefas:
                if tarefa.id == id_busca:
                    tarefa.marcar_concluida()
                    repo_tarefas.salvar(tarefas)
                    print("Tarefa concluída!")
                    encontrada = True
                    break
            if not encontrada: print("Tarefa não encontrada.")

        elif opcao == "4":
            id_h = str(len(habitos) + 1)
            nome = input("Nome do hábito: ")
            freq = input("Frequência (Diário/Semanal): ")
            habitos.append(Habito(id_h, nome, freq))
            repo_habitos.salvar(habitos)
            print("Hábito cadastrado!")

        elif opcao == "5":
            print("\n--- LISTA DE HÁBITOS ---")
            for habito in habitos:
                print(habito)

        elif opcao == "6":
            id_busca = input("ID do hábito executado: ")
            encontrada = False
            for habito in habitos:
                if habito.id == id_busca:
                    habito.registrar_execucao()
                    repo_habitos.salvar(habitos)
                    print("Execução registrada!")
                    encontrada = True
                    break
            if not encontrada: print("Hábito não encontrado.")

        elif opcao == "7":
            relatorios.gerar_relatorio_tarefas(tarefas)
            relatorios.gerar_relatorio_habitos(habitos)

        elif opcao == "0":
            print("Gerenciador encerrado!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
