def gerar_relatorio_tarefas(tarefas):
    """Exibe tarefas pendentes e concluídas."""
    print("\n--- RELATÓRIO DE TAREFAS ---")
    pendentes = [t for t in tarefas if not t.concluida]
    concluidas = [t for t in tarefas if t.concluida]
    
    print(f"Pendentes ({len(pendentes)}):")
    for t in pendentes:
        print(f"  - {t.titulo} (ID: {t.id})")
        
    print(f"\nConcluídas ({len(concluidas)}):")
    for t in concluidas:
        print(f"  - {t.titulo} (ID: {t.id})")

def gerar_relatorio_habitos(habitos):
    """Exibe o desempenho de cada hábito."""
    print("\n--- DESEMPENHO DE HÁBITOS ---")
    if not habitos:
        print("Nenhum hábito cadastrado.")
        return
        
    for h in habitos:
        print(f"Hábito: {h.nome} | Frequência: {h.frequencia} | Total de Execuções: {h.contador_execucoes}")
