import matplotlib.pyplot as plt


def intersecao(pontoA, pontoB, janela, lado):
    xA, yA = pontoA
    xB, yB = pontoB
    xmin, ymin, xmax, ymax = janela

    # Lados verticais: x = xmin ou x = xmax
    if lado == "esquerda":
        x = xmin
        if xB == xA:  # aresta vertical, evita divisão por zero
            return (x, yA)
        t = (x - xA) / (xB - xA)
        y = yA + t * (yB - yA)
        return (x, y)

    if lado == "direita":
        x = xmax
        if xB == xA:  # aresta vertical, evita divisão por zero
            return (x, yA)
        t = (x - xA) / (xB - xA)
        y = yA + t * (yB - yA)
        return (x, y)

    # Lados horizontais: y = ymin ou y = ymax
    if lado == "baixo":
        y = ymin
        if yB == yA:  # aresta horizontal, evita divisão por zero
            return (xA, y)
        t = (y - yA) / (yB - yA)
        x = xA + t * (xB - xA)
        return (x, y)

    if lado == "cima":
        y = ymax
        if yB == yA:  # aresta horizontal, evita divisão por zero
            return (xA, y)
        t = (y - yA) / (yB - yA)
        x = xA + t * (xB - xA)
        return (x, y)



# recebe uma lista de pontos do polígono original, as coordenadas da janela e o lado que será recortado
def recortar_lado(poligono, janela, lado):
    novo_poligono = []

    # coordenadas da janela
    xmin, ymin, xmax, ymax = janela

    for i in range(len(poligono)):  #  loop que percorre todas as arestas

        ponto_anterior = poligono[i - 1]  # S
        ponto_atual    = poligono[i]      # P

        # Separa as coordenadas de S e P
        xS, yS = ponto_anterior
        xP, yP = ponto_atual


        # Verifica se S e P estão dentro da área de recorte
        if lado == "esquerda":
            # para o lado esquerdo um ponto está dentro se ele estiver a direita do xmin ou na borda
            s_dentro = xS >= xmin # então S está dentro? true se Xs for maior ou igual a xmin
            p_dentro = xP >= xmin # P está dentro? true se Xp for maior ou igual a xmin

        elif lado == "direita": 
            # para o lado direito um ponto está dentro se ele estiver a esquerda do xmax ou na borda    
            s_dentro = xS <= xmax # S está dentro? true se Xs for menor ou igual a xmax
            p_dentro = xP <= xmax # P está dentro? true se Xp for menor ou igual a xmax

        elif lado == "baixo":
            # para o lado de baixo um ponto está dentro se ele estiver acima do ymin ou na borda
            s_dentro = yS >= ymin # S está dentro? true se Ys for maior ou igual a ymin
            p_dentro = yP >= ymin # P está dentro? true se Yp for maior ou igual a ymin

        elif lado == "cima":   
            # para o lado de cima um ponto está dentro se ele estiver abaixo do ymax ou na borda      
            s_dentro = yS <= ymax # S está dentro? true se Ys for menor ou igual a ymax
            p_dentro = yP <= ymax # P está dentro? true se Yp for menor ou igual a ymax


        # Quatro casos possíveis:

        # 1) Dentro -> Dentro
        if s_dentro and p_dentro:
            novo_poligono.append(ponto_atual)

        # 2) Dentro -> Fora
        elif s_dentro and not p_dentro:
            inter = intersecao(ponto_anterior, ponto_atual, janela, lado)
            novo_poligono.append(inter)

        # 3) Fora -> Fora  (não faz nada)
        elif not s_dentro and not p_dentro:
            pass

        # 4) Fora -> Dentro
        elif not s_dentro and p_dentro:
            inter = intersecao(ponto_anterior, ponto_atual, janela, lado)
            novo_poligono.append(inter)
            novo_poligono.append(ponto_atual)

    return novo_poligono




def sutherland_hodgman(poligono, janela):
    for lado in ["esquerda", "direita", "baixo", "cima"]:
        poligono = recortar_lado(poligono, janela, lado)
    return poligono


def plotar(poligono, recortado, janela):
    xmin, ymin, xmax, ymax = janela

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Coordenadas da janela
    wx = [xmin, xmax, xmax, xmin, xmin]
    wy = [ymin, ymin, ymax, ymax, ymin]

    # --------- ANTES DO RECORTE ---------
    ax = axs[0]

    xs = [p[0] for p in poligono] + [poligono[0][0]]
    ys = [p[1] for p in poligono] + [poligono[0][1]]

    # desenha as bordas
    ax.plot(xs, ys, "o-", label="Original", color="blue")

    # preenche o polígono original
    ax.fill(xs, ys, color="blue", alpha=0.2)

    # janela
    ax.plot(wx, wy, "--", label="Janela", color="orange")

    ax.set_title("Antes do recorte")
    ax.set_aspect("equal")
    ax.grid(True)
    ax.legend(loc="upper left", bbox_to_anchor=(1.05, 1))

    ax = axs[1]

    if recortado:
        xs_r = [p[0] for p in recortado] + [recortado[0][0]]
        ys_r = [p[1] for p in recortado] + [recortado[0][1]]

  
        ax.plot(xs_r, ys_r, "o-", label="Recortado", color="green")

        ax.fill(xs_r, ys_r, color="green", alpha=0.25)

    ax.plot(wx, wy, "--", label="Janela", color="orange")

    ax.set_title("Depois do recorte")
    ax.set_aspect("equal")
    ax.grid(True)
    ax.legend(loc="upper left", bbox_to_anchor=(1.05, 1))

    plt.tight_layout()
    plt.show()






if __name__ == "__main__":
    # poligono 1
    #poligono = [(2, 8), (2, 5), (3, 5), (3, 6.5), (6, 6.5), (6, 5), (7, 5), (7, 8)]

    # poligono 2
    #poligono = [(3,7), (3, 3), (9,3)]

    # poligono 3
    #poligono = [(2,3),(3,3),(3,4),(5,4),(5,3),(6,3),(6,1.5),(5,1.5),(5,0.5),(3,0.5),(3,1.5),(2,1.5)]

    # poligono 4
    poligono = [(1,7),(3,5),(2,3),(0,3),(-1,5)]


    janela   = (1, 2, 8, 6)  

    recortado = sutherland_hodgman(poligono, janela)

    plotar(poligono, recortado, janela)
