# relatorios.py

def gerar_relatorio_tarefas(tarefas):
    print("\n" + "=" * 30)
    print("   RELATÓRIO DE TAREFAS")
    print("=" * 30)

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    pendentes = [t for t in tarefas if not t.concluida]
    concluidas = [t for t in tarefas if t.concluida]

    print(f"PENDENTES ({len(pendentes)}):")
    for t in pendentes:
        print(f"  • {t.titulo}")

    print(f"\nCONCLUÍDAS ({len(concluidas)}):")
    for t in concluidas:
        print(f"  • {t.titulo}")


def gerar_relatorio_habitos(habitos):
    print("\n" + "=" * 30)
    print("   DESEMPENHO DE HÁBITOS")
    print("=" * 30)

    if not habitos:
        print("Nenhum hábito cadastrado.")
        return

    for habito in habitos:
        print(habito)

        if habito.tarefas_vinculadas:
            concluidas = len([t for t in habito.tarefas_vinculadas if t.concluida])
            total = len(habito.tarefas_vinculadas)
            progresso = (concluidas / total) * 100
            print(f"  >> Progresso das tarefas de apoio: {progresso:.1f}%")
            print("-" * 20)
