def gerar_relatorio_tarefas(tarefas):
    print("\n" + "="*30)
    print("   RELATÓRIO DE TAREFAS")
    print("="*30)
    pendentes = [tarefa for tarefa in tarefas if not tarefa.concluida]
    concluidas = [tarefa for tarefa in tarefas if tarefa.concluida]
    
    print(f"PENDENTES ({len(pendentes)}):")
    for tarefa in pendentes:
        print(f"  • {tarefa.titulo}")
        
    print(f"\nCONCLUÍDAS ({len(concluidas)}):")
    for tarefa in concluidas:
        print(f"  • {tarefa.titulo}")

def gerar_relatorio_habitos(habitos):
    """
    Este relatório agora mostra claramente a RELAÇÃO.
    Ele percorre cada hábito e, dentro dele, percorre suas tarefas.
    """
    print("\n" + "="*30)
    print("   DESEMPENHO DE HÁBITOS")
    print("="*30)
    
    if not habitos:
        print("Nenhum hábito cadastrado.")
        return
        
    for habito in habitos:
        # Aqui usamos o __str__ customizado que mostra as tarefas vinculadas
        print(habito)
        
        # Lógica extra para a apresentação: Cálculo de progresso
        if habito.tarefas_vinculadas:
            concluidas = len([tarefa for tarefa in habito.tarefas_vinculadas if tarefa.concluida])
            total = len(habito.tarefas_vinculadas)
            progresso = (concluidas / total) * 100
            print(f"  >> Progresso das tarefas de apoio: {progresso:.1f}%")
            print("-" * 20)
