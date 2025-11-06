from src.prefetching_simulator import simulate_prefetching, printResults
import random
import matplotlib.pyplot as plt

random.seed(42)
frames = 3

# Sequência de acessos 1
page_refs = [random.randint(0, 9) for _ in range(15)]
print("Sequência de páginas:", page_refs)

print("\n--- SEM PRÉ-BUSCA ---")
pf_no_prefetch, rate_no_prefetch, eff_no_prefetch = simulate_prefetching(page_refs, frames, prefetch=False)
printResults(pf_no_prefetch, rate_no_prefetch, eff_no_prefetch)

print("\n--- COM PRÉ-BUSCA ---")
pf_prefetch, rate_prefetch, eff_prefetch = simulate_prefetching(page_refs, frames, prefetch=True)
printResults(pf_prefetch, rate_prefetch, eff_prefetch)

# Sequência de acessos 2
page_refs = [random.randint(0, 9) for _ in range(30)]
print("\nSequência de páginas:", page_refs)

print("\n--- SEM PRÉ-BUSCA ---")
pf_no_prefetch, rate_no_prefetch, eff_no_prefetch = simulate_prefetching(page_refs, frames, prefetch=False)
printResults(pf_no_prefetch, rate_no_prefetch, eff_no_prefetch)

print("\n--- COM PRÉ-BUSCA ---")
pf_prefetch, rate_prefetch, eff_prefetch = simulate_prefetching(page_refs, frames, prefetch=True)
printResults(pf_prefetch, rate_prefetch, eff_prefetch)

# Sequência de acessos 3
page_refs = [random.randint(0, 9) for _ in range(50)]
print("\nSequência de páginas:", page_refs)

print("\n--- SEM PRÉ-BUSCA ---")
pf_no_prefetch, rate_no_prefetch, eff_no_prefetch = simulate_prefetching(page_refs, frames, prefetch=False)
printResults(pf_no_prefetch, rate_no_prefetch, eff_no_prefetch)

print("\n--- COM PRÉ-BUSCA ---")
pf_prefetch, rate_prefetch, eff_prefetch = simulate_prefetching(page_refs, frames, prefetch=True)
printResults(pf_prefetch, rate_prefetch, eff_prefetch)

# Sequência de acessos 4
page_refs = [random.randint(0, 9) for _ in range(8000)]
print("\nSequência de páginas:", page_refs)

print("\n--- SEM PRÉ-BUSCA ---")
pf_no_prefetch, rate_no_prefetch, eff_no_prefetch = simulate_prefetching(page_refs, frames, prefetch=False)
printResults(pf_no_prefetch, rate_no_prefetch, eff_no_prefetch)

print("\n--- COM PRÉ-BUSCA ---")
pf_prefetch, rate_prefetch, eff_prefetch = simulate_prefetching(page_refs, frames, prefetch=True)
printResults(pf_prefetch, rate_prefetch, eff_prefetch)

if __name__ == "__main__":
    pass  # Mantido apenas para compatibilidade se quiser rodar no terminal

# Dados coletados das execuções anteriores
sequence_lengths = [15, 30, 50, 8000]
efficiencies_no_prefetch = []
efficiencies_prefetch = []

# Reexecutar para capturar dados de forma organizada
for n in sequence_lengths:
    page_refs = [random.randint(0, 9) for _ in range(n)]

    pf_no_prefetch, rate_no_prefetch, eff_no_prefetch = simulate_prefetching(page_refs, frames, prefetch=False)
    pf_prefetch, rate_prefetch, eff_prefetch = simulate_prefetching(page_refs, frames, prefetch=True)

    efficiencies_no_prefetch.append(eff_no_prefetch)
    efficiencies_prefetch.append(eff_prefetch)

# Criar gráfico de linha comparando as eficiências
plt.figure(figsize=(8, 5))
plt.plot(sequence_lengths, efficiencies_no_prefetch, marker='o', label='Sem Pré-busca', linewidth=2)
plt.plot(sequence_lengths, efficiencies_prefetch, marker='o', label='Com Pré-busca', linewidth=2)
plt.title('Comparação de Eficiência — Pré-busca vs. Sem Pré-busca')
plt.xlabel('Tamanho da sequência de páginas')
plt.ylabel('Eficiência (1 - Taxa de Falta)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()