from src.prefetching_simulator import simulate_prefetching, printResults
import random
import matplotlib.pyplot as plt

random.seed(42)
frames = 3

def gerar_grafico(page_refs, frames, titulo):
    pf_no_prefetch, rate_no_prefetch, eff_no_prefetch = simulate_prefetching(page_refs, frames, prefetch=False)
    pf_prefetch, rate_prefetch, eff_prefetch = simulate_prefetching(page_refs, frames, prefetch=True)

    print("\n--- SEM PRÉ-BUSCA ---")
    printResults(pf_no_prefetch, rate_no_prefetch, eff_no_prefetch)
    print("\n--- COM PRÉ-BUSCA ---")
    printResults(pf_prefetch, rate_prefetch, eff_prefetch)

    plt.figure(figsize=(6, 4))
    plt.bar(["Sem Pré-busca", "Com Pré-busca"], [eff_no_prefetch, eff_prefetch], color=["steelblue", "orange"])
    plt.title(f"Eficiência — {titulo}")
    plt.ylabel("Eficiência (1 - Taxa de Falta)")
    plt.ylim(0, 1)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def exemplo_1():
    page_refs = [random.randint(0, 9) for _ in range(15)]
    print("\nSequência de páginas:", page_refs)
    gerar_grafico(page_refs, frames, "Exemplo 1 (15 páginas)")


def exemplo_2():
    page_refs = [random.randint(0, 9) for _ in range(30)]
    print("\nSequência de páginas:", page_refs)
    gerar_grafico(page_refs, frames, "Exemplo 2 (30 páginas)")


def exemplo_3():
    page_refs = [random.randint(0, 9) for _ in range(50)]
    print("\nSequência de páginas:", page_refs)
    gerar_grafico(page_refs, frames, "Exemplo 3 (50 páginas)")


def exemplo_4():
    page_refs = [random.randint(0, 9) for _ in range(8000)]
    print("\nSequência de páginas (primeiras 20):", page_refs[:20], "...")
    gerar_grafico(page_refs, frames, "Exemplo 4 (8000 páginas)")


def menu():
    while True:
        print("\n=== SIMULADOR DE PRÉ-BUSCA DE PÁGINAS (FIFO) ===")
        print("1 - Executar Exemplo 1 (15 páginas)")
        print("2 - Executar Exemplo 2 (30 páginas)")
        print("3 - Executar Exemplo 3 (50 páginas)")
        print("4 - Executar Exemplo 4 (8000 páginas)")
        print("5 - Executar todos os exemplos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            exemplo_1()
        elif opcao == "2":
            exemplo_2()
        elif opcao == "3":
            exemplo_3()
        elif opcao == "4":
            exemplo_4()
        elif opcao == "5":
            exemplo_1(); exemplo_2(); exemplo_3(); exemplo_4()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()