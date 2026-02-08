def gerar_relatorio_tarefas(tarefas):
    # Imprime um relatório simples separando tarefas pendentes e concluídas.
    print("\n" + "="*30)
    # Título do relatório de tarefas
    print("   RELATÓRIO DE TAREFAS")
    print("="*30)
    # Lista compreensiva para filtrar tarefas não concluídas
    pendentes = [tarefa for tarefa in tarefas if not tarefa.concluida]
    # Lista compreensiva para filtrar tarefas concluídas
    concluidas = [tarefa for tarefa in tarefas if tarefa.concluida]

    # Imprime resumo de pendentes
    print(f"PENDENTES ({len(pendentes)}):")
    for tarefa in pendentes:
        # Somente o título é mostrado no relatório compacto
        print(f"  • {tarefa.titulo}")

    # Imprime resumo de concluídas
    print(f"\nCONCLUÍDAS ({len(concluidas)}):")
    for tarefa in concluidas:
        print(f"  • {tarefa.titulo}")

def gerar_relatorio_habitos(habitos):
    # Relatório que mostra cada hábito e seu desempenho, incluindo tarefas de apoio.
    """
    Este relatório percorre cada hábito e exibe suas informações e tarefas vinculadas.
    """
    print("\n" + "="*30)
    # Título do relatório de hábitos
    print("   DESEMPENHO DE HÁBITOS")
    print("="*30)

    # Se não houver hábitos cadastrados, avisa e retorna
    if not habitos:
        print("Nenhum hábito cadastrado.")
        return

    for habito in habitos:
        # Usa o método __str__ da classe Habito para imprimir detalhes
        print(habito)

        # Se o hábito tiver tarefas vinculadas, calcula o percentual concluído
        if habito.tarefas_vinculadas:
            concluidas = len([tarefa for tarefa in habito.tarefas_vinculadas if tarefa.concluida])
            total = len(habito.tarefas_vinculadas)
            progresso = (concluidas / total) * 100
            # Mostra o progresso com uma casa decimal
            print(f"  >> Progresso das tarefas de apoio: {progresso:.1f}%")
            # Linha separadora após cada hábito
            print("-" * 20)
