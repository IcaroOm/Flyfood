# Projeto FlyFood - Otimização de Rotas para Entregas com Drones

## Descrição do Projeto

O **FlyFood** é um projeto feito para a cadeira de Projetos Interdiciplinares para Sistemas da Informaçao 2. O desafio visa otimizar as rotas de drones para entregas em uma cidade, minimizando a distância percorrida e, consequentemente, o tempo e o consumo de bateria. O drone parte de um ponto de origem (R), realiza entregas em vários pontos da cidade e retorna ao ponto de origem. O problema é modelado como uma variação do **Problema do Caixeiro Viajante (TSP)**, utilizando a **distância de Manhattan** para calcular o custo das rotas.

Este repositório contém o código-fonte do algoritmo de otimização de rotas, que lê uma matriz de entrada com os pontos de entrega e calcula a rota mais curta para o drone.

---

## Funcionalidades

- **Leitura da Matriz de Entrada:** O algoritmo lê uma matriz que representa a cidade, identificando o ponto de origem (R) e os pontos de entrega (A, B, C, etc.).
- **Cálculo de Distâncias:** Utiliza a distância de Manhattan para calcular o custo de movimentação entre os pontos.
- **Geração de Rotas:** Gera todas as permutações possíveis dos pontos de entrega.
- **Avaliação de Rotas:** Calcula o custo total de cada rota, incluindo a partida, as entregas e o retorno ao ponto de origem.
- **Seleção da Rota Ótima:** Identifica e retorna a rota com o menor custo total.

---

## Como Usar

### Pré-requisitos

- Python 3.x instalado.

### Executando o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/IcaroOm/Flyfood.git
   cd Flyfood
   ```

2. Crie um arquivo de entrada no formato especificado (veja abaixo).

3. Execute o script Python:
   ```bash
   python main.py < arquivo_de_entrada.txt
   ```

   O script lerá a matriz de entrada do arquivo e exibirá a rota ótima no terminal.

---

### Formato do Arquivo de Entrada

O arquivo de entrada deve conter uma matriz que representa a cidade, onde:
- `R` é o ponto de origem e retorno do drone.
- `A`, `B`, `C`, etc., são os pontos de entrega.
- `0` representa espaços vazios (sem pontos de entrega).

Exemplo de arquivo de entrada (`entrada.txt`):
```
4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
```

- A primeira linha contém as dimensões da matriz (linhas e colunas).
- As linhas seguintes representam a matriz da cidade.

---

### Saída Esperada

O programa retornará a sequência de pontos de entrega que forma a rota mais curta. Por exemplo:
```
A D C B
```

---

## Explicação do Código

### Estrutura do Código

1. **Leitura da Entrada:**
   - O código lê a matriz de entrada e identifica as coordenadas do ponto de origem (R) e dos pontos de entrega.

2. **Cálculo de Distâncias:**
   - A função `get_distance` calcula a distância de Manhattan entre dois pontos.

3. **Geração de Permutações:**
   - Todas as permutações possíveis dos pontos de entrega são geradas usando `itertools.permutations`.

4. **Avaliação de Rotas:**
   - Para cada permutação, o custo total da rota é calculado usando a função `get_distance`.

5. **Seleção da Rota Ótima:**
   - A rota com o menor custo total é selecionada e exibida como resultado.

---
