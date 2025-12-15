import math
import matplotlib.pyplot as plt

# i representa o indice do ponto de controle
# n representa o grau do polinomio (numero de pontos de controle - 1)
# t é o parametro que varia de 0 a 1

def fatorial(n: int) -> int:
    resultado = 1
    for k in range(2, n +1):
        resultado = resultado * k
    return resultado


def binomio(n: int, i: int) -> int:
    numerador = fatorial(n)
    denominador = fatorial(i) * fatorial(n - i)
    return numerador // denominador

def bernstein(n: int, i: int, t: float) -> float:
    binomio_newton = binomio(n, i) # BN(n, i)
    t_elevado_a_i = math.pow(t, i) # t^i
    um_menos_t = (1.0 - t) # (1 - t)
    um_menos_t_elevado_a_n_menos_i = math.pow(um_menos_t, n - i) # (1 - t)^(n - i)
    return binomio_newton * t_elevado_a_i * um_menos_t_elevado_a_n_menos_i



def bezier(pontos_controle, t: float):

    # n é o grau do polinomio 
    n = len(pontos_controle) - 1

    cx = 0.0
    cy = 0.0

    for i in range(0, n + 1):
        # pega as coordenadas do ponto de controle atual
        px, py = pontos_controle[i]

        # calcula o polinomio de Bernstein
        b = bernstein(n, i, t)

        # acumula o valor das coordenadas x e y, multiplicando o polinomio pelo ponto de controle
        # igual a notação reduzida da fórmula
        cx = cx + b * px
        cy = cy + b * py
    return (cx, cy)



def plot_bezier(pontos_controle, steps):

    curva_x = []
    curva_y = []

    #cacular t de 0 a 1 automaticamente
    for k in range(steps + 1):
        t = k / steps

        #chamar bezier
        x, y = bezier(pontos_controle, t)
        curva_x.append(x)
        curva_y.append(y)


    ctrl_x = [p[0] for p in pontos_controle]
    ctrl_y = [p[1] for p in pontos_controle]

    # ---- Plotagem ----
    plt.figure(figsize=(8, 6))

    # Polígono de controle
    plt.plot(ctrl_x, ctrl_y, "o--", label="Pontos de controle")

    # Curva
    plt.plot(curva_x, curva_y, "-", linewidth=2, label="Curva de Bézier")

    plt.title("Curva de Bézier")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")  # mantém escala real (evita distorção)

    plt.show()

if __name__ == "__main__":

    pontos_controle = [(0.0, 0.0),(1.0, 2.0),(3.0, 2.0),(4.0, 0.0)]   
    #pontos_controle = [(0, 0), (2, 4),(4, -2),(6, 3)]   

    plot_bezier(pontos_controle, 1000)




     