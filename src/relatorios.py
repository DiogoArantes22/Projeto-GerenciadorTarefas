def gerar_relatorio_tarefas(tarefas):
    """Exibe tarefas pendentes e concluídas."""
    print("\n--- RELATÓRIO DE TAREFAS ---")
    pendentes = [tarefa for tarefa in tarefas if not tarefa.concluida]
    concluidas = [tarefa for tarefa in tarefas if tarefa.concluida]
    
    print(f"Pendentes ({len(pendentes)}):")
    for tarefa in pendentes:
        print(f"  - {tarefa.titulo} (ID: {tarefa.id})")
        
    print(f"\nConcluídas ({len(concluidas)}):")
    for tarefa in concluidas:
        print(f"  - {tarefa.titulo} (ID: {tarefa.id})")

def gerar_relatorio_habitos(habitos):
    """Exibe o desempenho de cada hábito."""
    print("\n--- DESEMPENHO DE HÁBITOS ---")
    if not habitos:
        print("Nenhum hábito cadastrado.")
        return
        
    for habito in habitos:
        print(f"Hábito: {habito.nome} | Frequência: {habito.frequencia} | Total de Execuções: {habito.contador_execucoes}")
