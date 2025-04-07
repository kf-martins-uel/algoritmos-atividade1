# Parte 1 - Entrada/Saída, Variáveis, Operadores, Atribuição

1. Elaborar um algoritmo para calcular a média aritmética de 2 notas escolares de um
aluno e escrever as notas e a média calculada.

   - [Diagrama:](/Parte-1/atividade1.png)  
   ![Diagrama  atividade 1](/Parte-1/atividade1.png)  
   - [Código atividade 1:](/Parte-1/atividade1.py)  

   ```python
   n1 = float(input("Nota 1: "))
   n2 = float(input("Nota 2: "))
   
   media = (n1 + n2) / 2
   
   print(f"Nota 1: {n1}, nota 2: {n2}, média: {media}")
   ```

2. Elaborar um algoritmo para calcular a área de uma circunferência, e apresentar a
medida da área calculada. Sabendo-se que: A= πr2 , onde A é a variável que conterá
o cálculo da área π é o valor de pi (3,14159) e r é o valor do raio.

    - [Diagrama:](/Parte-1/atividade2.png)  
    ![Diagrama atividade 2](/Parte-1/atividade2.png)
    - [Código atividade 2:](/Parte-1/atividade2.py)

    ```python
    import math

    r = float(input("Digite o raio: "))

    A = math.pi*r*r

    print(f"Área: {A:.2f} unidades de medida")
    ```

3. Elaborar um algoritmo para calcular e apresentar o volume de uma lata de óleo,
utilizando a fórmula: VOLUME = 3,14159 *(R2)* ALTURA.

    - [Diagrama:](/Parte-1/atividade3.png)  
    ![Diagrama atividade 3](/Parte-1/atividade3.png)
    - [Código atividade 3:](/Parte-1/atividade3.py)

    ```python
    import math

    raio = float(input("Digite o raio: "))
    altura = float(input("Digite a altura: "))

    volume = math.pi*raio**2*altura

    print(f"Volume: {volume:.2f} unidades de medida")
    ```

4. Dado o comprimento dos lados de um triângulo retângulo (b e c, que são valores
reais), calcule o comprimento da sua hipotenusa (h = raiz de (b2 + c2)).

    - [Diagrama:](/Parte-1/atividade4.png)  
    ![Diagrama atividade 4](/Parte-1/atividade4.png)
    - [Código atividade 4:](/Parte-1/atividade4.py)

    ```python
    b = float(input("Digite o valor de b:"))
    c = float(input("Digite o valor de c:"))

    h = (b**2 + c**2)**(1/2)

    print(f"Hipotenusa: {h:.2f}")
    ```

5. Elaborar um algoritmo para efetuar o cálculo de uma prestação em atraso, utilizando
a fórmula: PRESTAÇÃO = VALOR + (VALOR*(TAXA/100)*TEMPO).

    - [Diagrama:](/Parte-1/atividade5.png)  
    ![Diagrama atividade 5](/Parte-1/atividade5.png)
    - [Código atividade 5:](/Parte-1/atividade5.py)

    ```python
    valor = float(input("Diigte o valor: "))
    taxa = float(input("Diigte a taxa (em %): "))
    tempo = float(input("Diigte o tempo (dias): "))

    prestacao = valor + (valor * (taxa/100) * tempo)

    print(f"A prestação será {prestacao:.2f} unidades de dinheiro")
    ```

6. Elaborar um algoritmo para ler dois valores inteiros (variáveis A e B) e efetuar as
operações de adição, subtração e multiplicação de A por B, apresentando ao final
os três resultados obtidos.

   - [Diagrama:](/Parte-1/atividade6.png)  
   ![Diagrama atividade 6](/Parte-1/atividade6.png)
   - [Código atividade 6:](/Parte-1/atividade6.py)

    ```python
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))

    sum1 = A+B
    sub = A-B
    times = A*B

    print(f"Soma: {sum1}")
    print(f"Subtração: {sub} ")
    print(f"Multiplicação: {times}")
    ```

7. Fazer um algoritmo para ler o raio de um círculo, calcular e imprimir o perímetro
(perímetro ← 2 *pi* raio) e a área (área ← pi * raio2) do círculo.

   - [Diagrama:](/Parte-1/atividade7.png)  
   ![Diagrama atividade 7](/Parte-1/atividade7.png)
   - [Código atividade 7:](/Parte-1/atividade7.py)

    ```python
    import math

    r = float(input("Digite o raio: "))

    P = 2 * math.pi * r
    A = math.pi * r**2

    print(f"Perímetro: {P:.2f}\nÁrea: {A:.2f}")
    ```

8. O cardápio de uma casa de hambúrguer é dado abaixo. Preparar um algoritmo para
ler a quantidade de cada item comprado e calcular a conta final do cliente.  
Cardápio BCC Burgers:

    | Item           | Preço   |
    |----------------|---------|
    | Hamburguer     | R$ 3,50 |
    | Cheeseburguer  | R$ 4,10 |
    | MilkShake      | R$ 6,00 |
    | Coca-cola      | R$ 2,50 |

   - [Diagrama:](/Parte-1/atividade8.png)  
   ![Diagrama atividade 8](/Parte-1/atividade8.png)  
   - [Código atividade 8:](/Parte-1/atividade8.py)  

   ```python
   hamburguer = int(input("Quantidade de hamburguer: "))
   cheeseburguer = int(input("Quantidade de cheeseburguer: "))
   milkshake = int(input("Quantidade de milkshake: "))
   cocacola = int(input("Quantidade de coca-cola: "))
   
   total = 3.5*hamburguer + 4.1*cheeseburguer + 6.0*milkshake + 2.5*cocacola
   
   print(f"Conta final: R$ {total}")
   ```
