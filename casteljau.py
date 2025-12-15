import matplotlib.pyplot as plt

# Funçãp para calcular o ponto médio entre dois pontos
def ponto_medio(p, q):
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)


def subdividir(pontos):
    # pontos = [P0, P1, P2, P3]
    P0, P1, P2, P3 = pontos

    M01 = ponto_medio(P0, P1)
    M12 = ponto_medio(P1, P2)
    M23 = ponto_medio(P2, P3)

    M012 = ponto_medio(M01, M12)
    M123 = ponto_medio(M12, M23)

    M0123 = ponto_medio(M012, M123)

    esquerda = [P0, M01, M012, M0123]
    direita  = [M0123, M123, M23, P3]

    return esquerda, direita


def subdividir_rec(pontos, nivel):
    if nivel == 0:
        return [pontos]   # ponto de parada

    esq, dir = subdividir(pontos)
    return subdividir_rec(esq, nivel - 1) + subdividir_rec(dir, nivel - 1)


#plotagem
def curva_por_subdivisao(pontos_controle, nivel):
    segmentos = subdividir_rec(pontos_controle, nivel)

    curva = []
    for seg in segmentos:
        curva.append(seg[0])      

    curva.append(segmentos[-1][-1])  
    
    xs = [p[0] for p in curva]
    ys = [p[1] for p in curva]

    # Curva aproximada
    plt.plot(xs, ys, '-', linewidth=2, label="Curva")

    # Polígono de controle
    cx = [p[0] for p in pontos_controle]
    cy = [p[1] for p in pontos_controle]
    plt.plot(cx, cy, 'o--', label="Ponto de controle")

    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

    return curva



if __name__ == "__main__":
    # Curva simples
    pontos = [(0, 0),(2, 4),(4, 4),(6, 0)]

    # Curva S
    #pontos = [(0, 0), (2, 6), (4, -2), (6, 4)]

    # Curva C
    # pontos = [(0, 0),(0, 5),(6, 5),(6, 0)]
    

    # Nivel indica a quantidade de subdivisões (maior valor = mais suave)
    curva = curva_por_subdivisao(pontos, nivel = 6)
