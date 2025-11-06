# Simulação de Pré-Busca de Páginas (Page Prefetching)

Este projeto implementa uma **simulação de gerenciamento de memória com e sem pré-busca de páginas**, baseado no capítulo de **Memória** do livro *Andrew S. Tanenbaum – Sistemas Operacionais: Projeto e Implementação*.

O objetivo é comparar o desempenho de um sistema de **substituição de páginas FIFO** tradicional com um sistema que faz **pré-busca sequencial**, reduzindo faltas de página (*page faults*).

---

## 📚 Conceitos

- **Page Fault:** ocorre quando uma página requerida não está na memória principal.
- **Substituição FIFO:** remove a página mais antiga quando a memória está cheia.
- **Pré-Busca (Prefetching):** técnica que tenta antecipar quais páginas serão usadas e as carrega antes da necessidade.

---

## 🧠 Funcionalidades

- Simulação com e sem pré-busca
- Vários tamanhos de sequências de acesso
- Cálculo de:
  - Total de *page faults*
  - Taxa de falta
  - Eficiência global

