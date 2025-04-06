# Atividade 1 de Algoritimo

- Professor: Anderson

- Atividade dividida em 3 partes.

    - [Parte 1](/Parte-1/README.md)
    - [Parte 3](/Parte-2/README.md)
    - [Parte 3](/Parte-3/README.md)

```mermaid
flowchart TD
    A[Início] --> B[Leia nota1 e nota2]
    B --> C[Calcule média = (nota1 + nota2) / 2]
    C --> D{Média <= 3?}
    D -- Sim --> E[Reprovado sem rendimento]
    D -- Não --> F{Média <= 6?}
    F -- Sim --> G[Reprovado com Insuficiente]
    F -- Não --> H{Média <= 7?}
    H -- Sim --> I[Aprovado com Regular]
    H -- Não --> J{Média <= 9?}
    J -- Sim --> K[Aprovado com Bom]
    J -- Não --> L{Média <= 10?}
    L -- Sim --> M[Aprovado com Excelente]
    L -- Não --> N[Nota inválida]
    E --> O[Fim]
    G --> O
    I --> O
    K --> O
    M --> O
    N --> O
```    

>> Kauã Felipe Martins