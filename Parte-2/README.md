# Parte 2 - Estrutura condicional simples e composta

1. Escrever um algoritmo que leia dois valores numéricos e escreva o menor valor.

- [Diagrama: ](/Parte-2/atividade1.png)<br>
![Diagrama atividade 1](/Parte-2/atividade1.png)
- [Código atividade 1: ](/Parte-2/atividade1.py)
    ```python

    ```

2. Escrever um algoritmo que leia valores referentes às duas notas escolares de um aluno. Calcular a média e escrever: a média e a situação do aluno. Considerando: "Aprovado por Média” se (media >=7), "Não Aprovado por média” se (média < 7).

- [Diagrama: ](/Parte-2/atividade2.png)<br>
![Diagrama atividade 2](/Parte-2/atividade2.png)
- [Código atividade 2: ](/Parte-2/atividade2.py)
    ```python

    ```

3. Escrever um algoritmo que leia dois valores numéricos, efetue a adição desses valores. Se o valor somado for maior ou igual a dez, este deve ser escrito somando-se a ele mais cinco; caso contrário este deverá ser escrito subtraindo-se sete.

- [Diagrama: ](/Parte-2/atividade3.png)<br>
![Diagrama atividade 3](/Parte-2/atividade3.png)
- [Código atividade 3: ](/Parte-2/atividade3.py)
    ```python

    ```

4. Criar um algoritmo que leia dois números e imprimir uma mensagem dizendo se eles são iguais ou diferentes. Se forem diferentes, imprimir em ordem crescente.

- [Diagrama: ](/Parte-2/atividade4.png)<br>
![Diagrama atividade 4](/Parte-2/atividade4.png)
- [Código atividade 4: ](/Parte-2/atividade4.py)
    ```python

    ```

5. Elabore um algoritmo que leia dois valores digitados pelo usuário em seguida leia uma operação matemática desejada [ + , - , * , / ], após ler os valores e a operação calcular e escrever o resultado desta da operação.

- [Diagrama: ](/Parte-2/atividade5.png)<br>
![Diagrama atividade 5](/Parte-2/atividade5.png)
- [Código atividade 5: ](/Parte-2/atividade5.py)
    ```python

    ```

6. Elaborar um algoritmo que efetue o cálculo do reajuste de salário de um funcionário. Considere que o funcionário deve receber um reajuste de 15% caso seu salário seja menor que R$ 800,00. Se o salário for maior ou igual a R$ 800,00 e menor ou igual a R$ 1.500,00, seu reajuste será de 10%, e caso seja maior que R$ 1.500,00, o reajuste deverá ser de 5%.

- [Diagrama: ](/Parte-2/atividade6.png)<br>
![Diagrama atividade 6](/Parte-2/atividade6.png)
- [Código atividade 6: ](/Parte-2/atividade6.py)
    ```python

    ```

7. Escrever um algoritmo que leia duas notas escolares de um aluno, calcule sua média e escreva a média calculada e sua situação final. Considerando: se (media <= 3): “Reprovado sem rendimento", se (3 < média <= 6): "Reprovado com Insuficiente", se (6 < média <= 7): "Aprovado com Regular", se (7 < média <= 9): "Aprovado com Bom" e finalmente se (9 < média <= 10): "Aprovado com Excelente".



- [Diagrama: ](/Parte-2/atividade7.png)<br>
![Diagrama atividade 7](/Parte-2/atividade7.png)
```mermaid
---
config:
  theme: neo-dark
  layout: elk  
title: Atividade 7
---
flowchart LR
    start([start]) --> n1@{shape: manual-input} --> n2@{shape: manual-input}
    n2 --> media["média = (n1 + n2) / 2"]
    media --> média@{shape: display} --> if1{"`média <= 3`"}
    if1 -->|True| r@{shape: display, label: "\"Reprovado sem rendimento\""}
    if1 -->|False| if2{"média <= 6"}
    if2 -->|True| r2@{shape: display, label: "\"Reprovado com insuficiente\""}
    if2 -->|False| if3{"média <= 7"}
    if3 -->|True| a@{shape: display, label: "Aprovado com Regular"}
    if3 -->|False| if4{"média <= 9"}
    if4 -->|True| a2@{shape: display, label: "Aprovado com Bom"}
    if4 -->|False| if5{"média <= 10"}
    if5 -->|True| a3@{shape: display, label: "Aprovado com Excelente"}

    r --> c
    r2 --> c
    a --> c
    a2 --> c
    a3 --> c
    c@{shape: circle, label: " "} --> final([end])
```
- [Código atividade 7: ](/Parte-2/atividade7.py)
    ```python

    ```

8. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule e escreva o seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72,7*h)-58; Para mulheres: (62,1*h)-44,7.

- [Diagrama: ](/Parte-2/atividade8.png)<br>
![Diagrama atividade 8](/Parte-2/atividade8.png)
```mermaid
---
config:
  theme: neo-dark
  layout: elk  
title: Atividade 8
---
flowchart TB
    start([start])
    fim([end])
    altura@{shape: manual-input}
    sexo@{shape: manual-input}
    if{sexo == homem}
    homem["peso_ideal = (72,7 * altura) - 58"]
    mulher["peso_ideal = (62,1 * altura) - 44,7"]

    start --> altura --> sexo
    sexo --> if
    if -->|True| homem
    if -->|false| mulher
    homem --> display@{shape: display, label: "peso_ideal"}
    mulher ---> display
    display --> fim
```
- [Código atividade 8: ](/Parte-2/atividade8.py)
    ```python

    ```

9. Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias: 
Infantil A: 5 - 7 anos; 
Infantil B: 8 - 10 anos; 
Juvenil A: 11 - 13 anos; 
Juvenil B: 14 - 17 anos; 
Sênior: maiores de 18 anos; 
Inválida: menor que 5 maior 60.

- [Diagrama: ](/Parte-2/atividade9.png)<bra>
![Diagrama atividade 9](/Parte-2/atividade9.png)
```mermaid
---
config:
  theme: neo-dark 
title: Atividade 9
---
flowchart LR
    start([start])
    fim([end])
    conector@{shape: circle, label: " "}
    idade@{shape: manual-input}

    subgraph Categorias
        ia@{shape: display, label: "\"Infantil A\""}
        ib@{shape: display, label: "\"Infantil B\""}
        ja@{shape: display, label: "\"Juvenil A\""}
        jb@{shape: display, label: "\"Juvenil B\""}
        se@{shape: display, label: "\"Sênior\""}
        invalida@{shape: display, label: "\"Inválida\""}
    end

    subgraph Condições
        if1{"idade < 5 || idade > 60"}
        if2{"idade >= 5 && idade <= 7"}
        if3{"idade >= 8 && idade <= 10"}
        if4{"idade >= 11 && idade <= 13"}
        if5{"idade >= 14 && idade <= 17"}
        if6{"idade >= 18"}
    end

    start --> idade
    idade --> if1
    if1 --->|true| invalida
    if2 --->|true| ia
    if3 --->|true| ib
    if4 --->|true| ja 
    if5 --->|true| jb 
    if6 --->|true| se

    if1 --->|false| if2
    if2 --->|false| if3
    if3 --->|false| if4
    if4 --->|false| if5
    if5 --->|false| if6

    ia --> conector
    ib --> conector
    ja --> conector
    jb --> conector
    se --> conector
    invalida --> conector
    conector --> fim
```
- [Código atividade 9: ](/Parte-2/atividade9.py)
    ```python

    ```

10. Elaborar um algoritmo para verificar se um funcionário pode se aposentar, considerando as seguintes condições necessárias: - Condição 1: Se for mulher e estiver com mais de 60 anos; - Condição 2: Se for homem e estiver com mais de 65 anos.

- [Diagrama: ](/Parte-2/atividade10.png)<br>
![Diagrama atividade 10](/Parte-2/atividade10.png)
```mermaid
---
config:
  theme: neo-dark  
title: Atividade 10
---
flowchart TB
    start([start])
    fim([end])
    idade@{shape: manual-input}
    sexo@{shape: manual-input}
    conector@{shape: circle, label: " "}

    subgraph Condições
        if1{"sexo == 'homem'"}
        if2{idade > 65}
        if3{idade > 60}
    end
    subgraph Saídas
        valido@{shape: display, label: "\"Pode se aposentar\""}
        invalido@{shape: display, label: "\"Não pode se aposentar\""}
    end

    start --> idade --> sexo --> if1
    if1 -->|true| if2
    if1 -->|false| if3
    if2 -->|true| valido
    if3 -->|true| valido
    if2 -->|false| invalido
    if3 -->|false| invalido

    valido --> conector
    invalido --> conector
    conector --> fim
```
- [Código atividade 10: ](/Parte-2/atividade10.py)
    ```python

    ```

11. Preparar um algoritmo para ler os valores dos coeficientes a, b e c e imprimir os valores de delta e das raízes reais, quando houver.

- [Diagrama: ](/Parte-2/atividade11.png)<br>
![Diagrama atividade 11](/Parte-2/atividade11.png)
```mermaid
---
config:
  theme: neo-dark
  layout: elk
title: Atividade 11
---
flowchart TD
    start([start])
    fim([end])
    conector@{shape: circle, label: " "}
    subgraph " "
        a@{shape: manual-input}
        b@{shape: manual-input}
        c@{shape: manual-input}
    end
    delta["delta = b² - 4ac"]
    x1["x1 = (- b + √delta) / 2a"]
    x2["x2 = (- b - √delta) / 2a"]
    subgraph Displays
        ddelta@{shape: display, label: "delta"}
        dx1@{shape: display, label: "x1"}
        dx2@{shape: display, label: "x2"}
        invalido@{shape: display, label: "\"Não possui raizes reais\""}
    end
    if{delta < 0}
    start --> a --> b --> c --> delta --> if
    if --> |true| invalido
    if --> |false| x1 --> x2 --> ddelta --> dx1 --> dx2 --> conector
    invalido --> conector
    conector --> fim
```
- [Código atividade 11: ](/Parte-2/atividade11.py)
    ```python

    ```

12. Escreva um algoritmo para ler as coordenadas (X,Y) de um ponto no sistema cartesiano e escrever o quadrante ao qual o ponto pertence. Se o ponto estiver sobre os eixos, ou na origem, escrever NÃO ESTÁ EM NENHUM QUADRANTE.

- [Diagrama: ](/Parte-2/atividade12.png)<br>
![Diagrama atividade 12](/Parte-2/atividade12.png)
```mermaid
---
config:
theme: neo-dark  
title: Atividade 12
---
flowchart LR
    start([start])
    fim([end])
    conector@{shape: circle, label: " "}
    subgraph " "
        X@{shape: manual-input}
        Y@{shape: manual-input}
    end
    subgraph Condições
        if1{"X == 0 || Y == 0"}
        if2{"X > 0 && Y > 0"}
        if3{"X < 0 && Y > 0"}
        if4{"X < 0 && Y < 0"}
        if5{"X > 0 && Y < 0"}
    end
    subgraph Displays
        q0@{shape: display, label: "\"Nenhum quadrante\""}
        q1@{shape: display, label: "\"Quadrante 1\""}
        q2@{shape: display, label: "\"Quadrante 2\""}
        q3@{shape: display, label: "\"Quadrante 3\""}
        q4@{shape: display, label: "\"Quadrante 4\""}
    end

    start --> X --> Y --> if1 -->|true| q0

    if1 --> |false| if2 --> |false| if3 --> |false| if4 --> |false| if5

    if2 -->|true| q1
    if3 -->|true| q2
    if4 -->|true| q3
    if5 -->|true| q4
    
    q0 --> conector
    q1 --> conector
    q2 --> conector
    q3 --> conector
    q4 --> conector

    conector --> fim
```
- [Código atividade 12: ](/Parte-2/atividade12.py)
    ```python

    ```

13. Escreva um algoritmo que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é acutângulo (possui 3 ângulos agudos), retângulo (possui um ângulo reto) ou obtusângulo (possui um ângulo obtuso).

- [Diagrama: ](/Parte-2/atividade13.png)<br>
![Diagrama atividade 13](/Parte-2/atividade13.png)
```mermaid
---
title: Atividade 13
---
flowchart LR
    start([start])
    fim([end])
    conector((" ")) --> fim
    subgraph " "
        a@{shape: manual-input}
        b@{shape: manual-input}
        c@{shape: manual-input}
    end
    subgraph Condições
        if1{"`(a < 180 && a > 90) ||<br>( b < 180 && b > 90) ||<br>(c< 180 && c > 90)`"}
        if2{"(a == 90) ||<br>(b == 90) ||<br>(c == 90)"}
        if3{" a > 0) ||b > 0) ||c > 0)"}
    end
    subgraph Displays
        no@{shape: display, label: "Não é triângulo"}
        agudo@{shape: display, label: "Acutângulo"} 
        reto@{shape: display, label: "Reto"} 
        obtuso@{shape: display, label: "Obtusângulo"}
    end
    start --> a --> b --> c --> if1
    if1 --> |false| if2 --> |false| if3 --> |false| no --> conector
    if1 --> |true| obtuso --> conector
    if2 --> |true| reto --> conector
    if3 --> |true| agudo --> conector
```
- [Código atividade 13: ](/Parte-2/atividade13.py)
    ```python

    ```

14. Escreva um algoritmo para ler o número de lados de um polígono regular. Calcular e imprimir o seguinte:
    a. Se o número de lados for igual a 3 escrever TRIÂNGULO.
    b. Se o número de lados for igual a 4 escrever QUADRADO.
    c. Se o número de lados for igual a 5 escrever PENTÁGONO.
    d. Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
    e. Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

- [Diagrama: ](/Parte-2/atividade14.png)<br>
![Diagrama atividade 14](/Parte-2/atividade14.png)
```mermaid
---
config:
  theme: neo-dark
title: Atividade 14
---
flowchart LR
    start([start])
    fim([end])
    conector@{shape: circle, label: " "} --> fim
    n@{shape: manual-input}
    subgraph Condições
        if3{"n == 3"}
        if4{"n == 4"}
        if5{"n == 5"}
        ifi3{"n < 3"}
        ifs5{"n > 5"}
    end
    subgraph Displays
        t@{shape: display, label: "TRIÂNGULO"}
        q@{shape: display, label: "QUADRADO"}
        p@{shape: display, label: "PENTÁGONO"}
        np@{shape: display, label: "NÃO É UM POLÍGONO"}
        ni@{shape: display, label: "POLÍGONO NÃO IDENTIFICADO"}
    end

    start --> n --> if3 -->|false| if4 -->|false| if5 -->|false| ifi3 -->|false| ifs5
    if3 -->|true| t --> conector
    if4 -->|true| q --> conector
    if5 -->|true| p --> conector
    ifi3 -->|true| np --> conector
    ifs5 -->|true| ni --> conector
```
- [Código atividade 14: ](/Parte-2/atividade14.py)
    ```python

    ```

15. Construir um algoritmo que leia uma nota na forma quantitativa e escreva sua correspondente qualitativa, de acordo com a tabela abaixo:
    - Nota Quantitativa / Nota Qualitativa
        - [0; 2] Sem rendimento
        - [2; 4] Mau
        - [4; 6] Regular
        - [6; 8.5] Bom
        - [8.5; 10] Excelente

- [Diagrama: ](/Parte-2/atividade15.png)<br>
![Diagrama atividade 15](/Parte-2/atividade15.png)
```mermaid
---
config:
  theme: neo-dark
  layout: elk  
title: Atividade 15
---
flowchart TB
    start([start]) --> nota@{shape: manual-input}
    nota --> if1{"nota < 2"}
    if1 --> |true| sr@{shape: display, label: "Sem rendimento"}
    sr --> conector((" ")) --> fim([end])
    if1 --> |false| if2{"nota < 4"}
    if2 --> |true| Mau@{shape: display} --> conector
    if2 --> |false| if3{"nota < 6"}
    if3 --> |true| Regular@{shape: display} --> conector
    if3 --> |false| if4{"nota < 8.5"}
    if4 --> |true| Bom@{shape: display} --> conector
    if4 --> |false| Excelente@{shape: display} --> conector
```
- [Código atividade 15: ](/Parte-2/atividade15.py)
    ```python

    ```
