# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(nome):
    nome = nome.strip()
    if nome in tarefas:
        return f"Erro: Tarefa '{nome}' já existe."
    else:
        tarefas[nome] = False
        return f"Tarefa '{nome}' adicionada com sucesso!!"

def listar_tarefas(_=None):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = ["Lista de tarefas:"]
        for nome, concluida in sorted(tarefas.items(), key=lambda item: item[0]):
            status = "✔ Concluída" if concluida else "❌ Pendente"
            resultado.append(f"- {nome}: {status}")
        return "\n".join(resultado)

def remover_tarefa(nome):
    nome = nome.strip()
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    else:
        return f"Erro: Tarefa não encontrada."

def marcar_concluida(nome):
    nome = nome.strip()
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída!"
    else:
        return f"Erro: Tarefa não encontrada."

def exibir_menu():
    return (
        "\n===== Menu =====\n"
        "1. Adicionar tarefa\n"
        "2. Listar tarefas\n"
        "3. Remover tarefa\n"
        "4. Marcar tarefa como concluída\n"
        "5. Sair\n"
        "================"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            print(adicionar_tarefa(nome))
        elif opcao == "2":
            print(listar_tarefas())
        elif opcao == "3":
            nome = input("Digite o nome da tarefa para remover: ")
            print(remover_tarefa(nome))
        elif opcao == "4":
            nome = input("Digite o nome da tarefa para marcar como concluída: ")
            print(marcar_concluida(nome))
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()