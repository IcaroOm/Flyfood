import sys

def read_input():
    rows, cols = map(int, sys.stdin.readline().split()) # Input do grid

    # Dict para armazenar os pontos de entrega (chave: caractere, valor: coordenadas)
    delivery = {}
    start = None

    for row in range(rows):
        line = sys.stdin.readline().strip().split()
        for col, char in enumerate(line):
            if char == 'R':
                start = (row, col)
            elif char != '0':  # Ignora células com '0'
                delivery[char] = (row, col)
    return delivery, start

def permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for p in permutations(elements[1:]):
            for i in range(len(elements)):
                yield p[:i] + elements[0:1] + p[i:]

def main():
    """Função principal que calcula o caminho ótimo para as entregas."""

    # Lê o input
    delivery, start = read_input()
    
    # Caso não haja pontos de entrega, imprime string vazia e retorna
    if not delivery:
        print("")
        return
    
    # Define a lista com a chave todos os pontos no grid (ex: ['A', 'B', 'C'])
    points = list(delivery.keys())

    # Dicionário para armazenar distâncias calculadas e evitar repetição
    distance_cache = {}

    def get_distance(a, b):
        """Calcula a distância entre dois pontos (com cache)."""

        # Verifica se a distância já foi calculada anteriormente
        if (a, b) in distance_cache:
            return distance_cache[(a, b)]
        
        # Obtém coordenadas do ponto 'a' (pode ser 'R' ou um ponto de entrega)
        if a == 'R':
            x1, y1 = start
        else:
            x1, y1 = delivery[a]
        
        # Obtém coordenadas do ponto 'b' (pode ser 'R' ou um ponto de entrega)
        if b == 'R':
            x2, y2 = start
        else:
            x2, y2 = delivery[b]
        
        # Calcula a distância(soma das diferenças absolutas)
        dist = abs(x1 - x2) + abs(y1 - y2)
        # Armazena a distância no cache para ambas as direções (a->b e b->a)
        distance_cache[(a, b)] = dist
        distance_cache[(b, a)] = dist
        return dist

    # Variáveis para rastrear a menor distância total e o melhor caminho
    min_total = float('inf')
    best_path = None

    # Gera todas as permutações possíveis dos pontos de entrega
    for perm in permutations(points):
        # Calcula a distância total para a permutação atual
        total = get_distance('R', perm[0])  # Do ponto inicial ao primeiro ponto
        
        if total >= min_total: # Verifica se a distacia parcial ja ultrapassou o minimo conhecido
            continue

        for i in range(len(perm) - 1):
            total += get_distance(perm[i], perm[i+1])
            if total >= min_total: # Verifica novamente se a distancia ja ultrapassou o minimo conhecido
                break

        total += get_distance(perm[-1], 'R')  # Do último ponto de volta ao início
        
        # Atualiza o melhor caminho se encontrar uma distância menor
        if total < min_total:
            min_total = total
            best_path = perm
        # Em caso de empate, considera a primeira permutação encontrada
        elif total == min_total and best_path is None:
            best_path = perm

    # Imprime o melhor caminho como uma string separada por espaços
    print(' '.join(best_path))


if __name__ == "__main__":
    main()
