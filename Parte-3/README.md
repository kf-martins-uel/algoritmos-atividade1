# Parte 3 - Estrutura de Repetição

Faça um único programa com um menu para que se possa escolher qual questão executar.

1. Leia cinco números quaisquer e imprima o quadrado de cada número.

    - [Diagrama:](/Parte-3/atividade1.png)  
    ![Diagrama atividade 1](/Parte-3/atividade1.png)
    - [Código atividade 1:](/Parte-3/atividade1.py)

    ```python
    for i in range(5): 
        i = int(input(f"{i+1}. Digite um número: "))
        print(f"Quadrado de {i} = {i**2}")
    ```

2. Leia 10 números quaisquer e imprima a metade de cada número.

    - [Diagrama:](/Parte-3/atividade2.png)  
    ![Diagrama atividade 2](/Parte-3/atividade2.png)
    - [Código atividade 2:](/Parte-3/atividade2.py)

    ```python
    for i in range(10): 
        i = int(input(f"{i+1}. Digite um número: "))
        print(f"Metade de {i} = {i/2}")  
    ```

3. Imprima todos os números pares no intervalo entre 1 e 10.

    - [Diagrama:](/Parte-3/atividade3.png)  
    ![Diagrama atividade 3](/Parte-3/atividade3.png)
    - [Código atividade 3:](/Parte-3/atividade3.py)

    ```python
    n = 1
    while n <= 10:
      resto = n%2
      if not resto: # resto != 0
         print(n)
      n+=1 
    ```

4. Receba 15 números quaisquer e imprima a raiz quadrada de cada número.

    - [Diagrama:](/Parte-3/atividade4.png)  
    ![Diagrama atividade 4](/Parte-3/atividade4.png)
    - [Código atividade 4:](/Parte-3/atividade4.py)

    ```python
    i = 0 
    while i < 15:
       n = int(input(f"{i+1}. Digite um número: "))
       print(f"Raiz de {n} = {n**(1/2)}")
       i+=1
    ```

5. Escrever a tabela de conversão de polegadas para centímetros. Deseja-se que na tabela constem valores desde 1 polegada até 20 polegadas inteiras. (1pol = 2,54cm).

    - [Diagrama:](/Parte-3/atividade5.png)  
    ![Diagrama atividade 5](/Parte-3/atividade5.png)
    - [Código atividade 5:](/Parte-3/atividade5.py)

    ```python
    print(f"{'Polegadas':<15}{'Centímetros':<20}")
    for p in range(1, 21):
       cm = 2.54*p
       print(f"{p:<15}{cm:<20}")
    ```

6. Entrar com um nome, idade e sexo de 10 pessoas. Imprimir o nome se a pessoa for do sexo masculino e tiver mais de 21 anos.

    - [Diagrama:](/Parte-3/atividade6.png)  

    ```mermaid
    flowchart TB
            start([start]) --> contador["contador = 1"] --> for{{contador <= 10}} -->|true| nome@{shape: manual-input} --> idade@{shape: manual-input} --> sexo@{shape: manual-input} --> i["contador += 1"]
            i --> if{"sexo == masculino && idade >= 21"} -->|true| dnome@{shape: display, label:"nome"}
            for -->|false| fim([end])
    ```

    - [Código atividade 6:](/Parte-3/atividade6.py)

    ```python
    for i in range(10):
        nome = input("Digite o nome: ") 
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo [M, F]: ")

        if sexo.lower() == 'm' and idade >= 21:
            print(nome)
    ```

7. Ler um número que será o limite superior de um intervalo e o incremento do intervalo(1, 2, 3, etc.). Escrever todos os números naturais no intervalo de 0 até limite superior. Suponha que os dois números lidos são maiores do que zero.

    - [Diagrama:](/Parte-3/atividade7.png)  

    ```mermaid
    flowchart TB
        start([start]) --> n@{shape: manual-input} --> i@{shape: manual-input} --> contador["c = 0"] --> for{{"c <= n"}}
        for -->|false| fim([end])
        for -->|true| display@{shape: display, label:contador} --> inc["contador += i"]
    ```

    - [Código atividade 7:](/Parte-3/atividade7.py)

    ```python
    n = int(input("Digite o limite superior: "))
    i = int(input("Digite o incremento: "))
    for i in range(0, n+1, i):
        print(i)
    ```

8. Ler um número que será o limite superior de um intervalo e imprimir todos os números ímpares menores que esse número.

    - [Diagrama:](/Parte-3/atividade8.png)  

    ```mermaid
    flowchart TB
        start([start]) --> n@{shape: manual-input} --> contador["c = 1"] --> for{{"c <= n"}}
        for -->|false| fim([end])
        for -->|true| if{"contador % 2 == 1"} --> display@{shape: display, label:contador} --> inc["contador += 1"]
    ```

    - [Código atividade 8:](/Parte-3/atividade8.py)

    ```python
    n = int(input("Digite o limite superior: "))
    for i in range(n+1):
        print(i if i%2 else ' ', end='')
    ```

9. Ler um número e imprimir todos os números de 1 até o número lido e o seu fatorial.

    - [Diagrama:](/Parte-3/atividade9.png)  
    ![Diagrama atividade 9](/Parte-3/atividade9.png)
    - [Código atividade 9:](/Parte-3/atividade9.py)

    ```python
    n = int(input("Digite um número: "))
    print(f"{'Número':<10}{'Fatorial':<13}")
    for i in range(1, n+1):
        fat = 1
        for f in range(i):
            fat *= (f+1)
        print(f"{i:<10}{fat:<13}")
    ```

10. Escrever a soma dos números pares entre 25 e 201.

    - [Diagrama:](/Parte-3/atividade10.png)  
    ![Diagrama atividade 10](/Parte-3/atividade10.png)
    - [Código atividade 10:](/Parte-3/atividade10.py)

    ```python
    # Soma de PA - s = (a1 +a2)*n/2
    # (201-25)/2 = n
    # soma = (25+201)*n/2
    soma = 0
    for i in range(26, 202, 2):
        soma += i
    print(soma)
    ```

11. Ler um número que será o limite superior e um número que será o limite inferior de um intervalo. Imprimir todos os números naturais no intervalo fechado.

    - [Diagrama:](/Parte-3/atividade11.png)  
    ![Diagrama atividade 11](/Parte-3/atividade11.png)
    - [Código atividade 11:](/Parte-3/atividade11.py)

    ```python
    s = int(input("Digite o limite superior: "))
    i = int(input("Digite o limite inferior: "))

    while i <= s:
        print(i)
        i+=1
    ```

12. Calcular e escrever uma tabela de graus centígrados em função de graus fahrenheit que variem de 50 a 150 de 1 em 1. A conversão de graus fahrenheit para centígrados é obtida pela equação C = 5/9*(F-32).

    - [Diagrama:](/Parte-3/atividade12.png)  
    ![Diagrama atividade 12](/Parte-3/atividade12.png)
    - [Código atividade 12:](/Parte-3/atividade12.py)

    ```python
    print(f"{'Fahrenheit':<12}{'Celsius':<15}")
    f = 50
    while f<=150:
        c = ((f-32)*5)/9
        print(f"{f:.<12}{c:.2f}")
        f+=1

    ```

13. Gerar o número H, sendo H = 1 + 1/2 + 1/3 + ... + 1/N. O número N é informado pelo usuário.

    - [Diagrama:](/Parte-3/atividade13.png)  
    ![Diagrama atividade 13](/Parte-3/atividade13.png)
    - [Código atividade 13:](/Parte-3/atividade13.py)

    ```python
    n = int(input("Digite um número: "))
    h = 0
    while n>=1:
        h+= 1/n
        n-=1
    print(h)
    ```  

14. Faça um algoritmo que leia o nome, altura, sexo (M – masculino, F – feminino) e cor dos olhos (A – azuis, V – verdes, C – castanhos) para um conjunto de 15 pessoas. O algoritmo deve calcular e escrever:
    - Total de homens que possuem olhos castanhos.
    - Total de mulheres com altura inferior a 1,60m.
    - Total de mulheres.

    - [Diagrama:](/Parte-3/atividade14.png)  
    ![Diagrama atividade 14](/Parte-3/atividade14.png)
    - [Código atividade 14:](/Parte-3/atividade14.py)

    ```python
    n = hc = mi = m = 0
    for i in range(15):
        nome = input("Digite o nome: ")
        altura = float(input("Digite a alura: "))
        sexo = input("Digite o sexo [m,f]: ")
        olhos = input("Digite a cor dos olhos (c - castanhos; a - azuis; v - verdes): ")
        if sexo.lower() == 'm' and olhos.lower() == 'c':
            hc+=1
        elif sexo.lower() == 'f':
            m+=1
            mi += 1 if altura<1.6 else 0
    print(f"Total de homens com olhos castanhos: {hc}\nTotal de mulheres: {m}\nTotal de mulheres com altura menor que 1.60m: {mi}")
    ```
