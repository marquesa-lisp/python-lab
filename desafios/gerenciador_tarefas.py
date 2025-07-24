#!/usr/bin/env python3
"""
Desafio: Gerenciador de Tarefas

Este projeto implementa um gerenciador de tarefas simples com as seguintes funcionalidades:
1. Adicionar Tarefas
2. Ver tarefas
3. Atualizar tarefas
4. Completar tarefas
5. Deletar tarefas completadas
6. Sair

Conceitos utilizados:
- Funções
- Listas
- Dicionários
- Loops (while)
- Condicionais (if/elif/else)
- Enumerate
- Input do usuário
"""

# ========== FUNÇÕES DO GERENCIADOR ==========

def adicionar_tarefas(tarefas, nome_tarefa):
    """
    Adiciona uma nova tarefa à lista de tarefas.
    
    Args:
        tarefas (list): Lista de tarefas existentes
        nome_tarefa (str): Nome da nova tarefa
    
    Returns:
        None
    """
    # Criamos um dicionário para armazenar as informações da tarefa
    # Cada tarefa tem um nome e um status de completada (inicialmente False)
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\n✅ Tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    return


def ver_tarefas(tarefas):
    """
    Exibe todas as tarefas com seus respectivos status.
    
    Args:
        tarefas (list): Lista de tarefas
    
    Returns:
        None
    """
    if not tarefas:  # Verifica se a lista está vazia
        print("\n📋 Nenhuma tarefa cadastrada.")
        return
    
    print("\n📋 Lista de tarefas:")
    print("-" * 40)
    
    # enumerate() nos dá o índice e o item ao mesmo tempo
    # start=1 faz a contagem começar de 1 ao invés de 0
    for indice, tarefa in enumerate(tarefas, start=1):
        # Operador ternário: if-else em uma linha
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    
    print("-" * 40)
    return


def atualizar_tarefas(tarefas, indice_tarefa, novo_nome_tarefa):
    """
    Atualiza o nome de uma tarefa existente.
    
    Args:
        tarefas (list): Lista de tarefas
        indice_tarefa (str): Índice da tarefa (começando de 1)
        novo_nome_tarefa (str): Novo nome para a tarefa
    
    Returns:
        None
    """
    # Ajusta o índice: usuário vê 1,2,3... mas lista usa 0,1,2...
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    
    # Verifica se o índice é válido
    if 0 <= indice_tarefa_ajustado < len(tarefas):
        tarefa_antiga = tarefas[indice_tarefa_ajustado]["tarefa"]
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"\n✏️  Tarefa '{tarefa_antiga}' atualizada para: '{novo_nome_tarefa}'")
    else:
        print("\n❌ Índice de tarefa inválido!")
    return


def completar_tarefa(tarefas, indice_tarefa):
    """
    Marca uma tarefa como completada.
    
    Args:
        tarefas (list): Lista de tarefas
        indice_tarefa (str): Índice da tarefa (começando de 1)
    
    Returns:
        None
    """
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    
    if 0 <= indice_tarefa_ajustado < len(tarefas):
        nome_tarefa = tarefas[indice_tarefa_ajustado]["tarefa"]
        tarefas[indice_tarefa_ajustado]["completada"] = True
        print(f"\n✅ Tarefa '{nome_tarefa}' marcada como completada!")
    else:
        print("\n❌ Índice de tarefa inválido!")
    return


def deletar_tarefas_completadas(tarefas):
    """
    Remove todas as tarefas que foram marcadas como completadas.
    
    Args:
        tarefas (list): Lista de tarefas
    
    Returns:
        None
    """
    # Cria uma nova lista apenas com tarefas não completadas
    # Isso evita problemas ao remover itens durante a iteração
    tarefas_nao_completadas = [tarefa for tarefa in tarefas if not tarefa["completada"]]
    
    # Calcula quantas tarefas foram removidas
    tarefas_removidas = len(tarefas) - len(tarefas_nao_completadas)
    
    # Limpa a lista original e adiciona apenas as não completadas
    tarefas.clear()
    tarefas.extend(tarefas_nao_completadas)
    
    if tarefas_removidas > 0:
        print(f"\n🗑️  {tarefas_removidas} tarefa(s) completada(s) foi(foram) deletada(s).")
    else:
        print("\n📋 Nenhuma tarefa completada para deletar.")
    return


# ========== PROGRAMA PRINCIPAL ==========

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    # Lista que irá armazenar todas as tarefas
    tarefas = []
    
    print("=" * 50)
    print("🗂️  BEM-VINDO AO GERENCIADOR DE TAREFAS 🗂️")
    print("=" * 50)
    
    # Loop principal do programa
    while True:
        print("\n📌 MENU DO GERENCIADOR DE TAREFAS:")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Atualizar tarefa")
        print("4. Completar tarefa")
        print("5. Deletar tarefas completadas")
        print("6. Sair")
        print("-" * 30)
        
        escolha = input("Digite sua escolha (1-6): ")
        
        if escolha == "1":
            nome_tarefa = input("\n📝 Digite o nome da tarefa: ")
            if nome_tarefa.strip():  # Verifica se não está vazio
                adicionar_tarefas(tarefas, nome_tarefa)
            else:
                print("\n❌ Nome da tarefa não pode ser vazio!")
                
        elif escolha == "2":
            ver_tarefas(tarefas)
            
        elif escolha == "3":
            ver_tarefas(tarefas)
            if tarefas:  # Só permite atualizar se houver tarefas
                indice_tarefa = input("\n📝 Digite o número da tarefa que deseja atualizar: ")
                novo_nome = input("📝 Digite o novo nome da tarefa: ")
                if novo_nome.strip():
                    atualizar_tarefas(tarefas, indice_tarefa, novo_nome)
                else:
                    print("\n❌ Nome da tarefa não pode ser vazio!")
                    
        elif escolha == "4":
            ver_tarefas(tarefas)
            if tarefas:  # Só permite completar se houver tarefas
                indice_tarefa = input("\n✅ Digite o número da tarefa que deseja completar: ")
                completar_tarefa(tarefas, indice_tarefa)
                
        elif escolha == "5":
            deletar_tarefas_completadas(tarefas)
            ver_tarefas(tarefas)
            
        elif escolha == "6":
            print("\n👋 Obrigado por usar o Gerenciador de Tarefas!")
            print("Até a próxima! 🚀")
            break
            
        else:
            print("\n❌ Opção inválida! Por favor, escolha uma opção de 1 a 6.")
    
    print("\n" + "=" * 50)
    print("Programa Finalizado")
    print("=" * 50)


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main() 