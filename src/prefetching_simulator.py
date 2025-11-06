import random

def simulate_prefetching(page_references, num_frames, prefetch=False):
    memory = []
    page_faults = 0
    total_accesses = len(page_references)

    for i, page in enumerate(page_references):
        page_in_memory = page in memory

        if not page_in_memory:
            page_faults += 1
            # Substituição FIFO
            if len(memory) < num_frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

            # Faz pré-busca APENAS quando ocorre falta
            if prefetch and i + 1 < total_accesses:
                next_page = page_references[i + 1]
                if next_page not in memory:
                    if len(memory) < num_frames:
                        memory.append(next_page)
                    else:
                        memory.pop(0)
                        memory.append(next_page)

        else:
            # Se foi hit, faz prefetch só se ainda houver espaço livre
            if prefetch and len(memory) < num_frames and i + 1 < total_accesses:
                next_page = page_references[i + 1]
                if next_page not in memory:
                    memory.append(next_page)

    fault_rate = page_faults / total_accesses
    efficiency = 1 - fault_rate
    return page_faults, fault_rate, efficiency


def printResults(page_faults, fault_rate, efficiency):
    print(f"Faltas de página: {page_faults}")
    print(f"Taxa de falta: {fault_rate:.2%}")
    print(f"Eficiência: {efficiency:.2%}")