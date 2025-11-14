#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def ler_pontos_de_programa(comando):
    proc = subprocess.Popen(comando, stdout=subprocess.PIPE, text=True)
    pts = []
    for linha in proc.stdout:
        linha = linha.strip()
        if not linha:
            continue
        partes = linha.split()
        if len(partes) != 2:
            continue
        x, y = map(int, partes)
        pts.append((x, y))
    proc.wait()
    return pts


def limites_cartesianos(pontos, margem=1):
    xs = [x for x, _ in pontos]
    ys = [y for _, y in pontos]
    x_min = min(min(xs), 0) - margem
    x_max = max(max(xs), 0) + margem
    y_min = min(min(ys), 0) - margem
    y_max = max(max(ys), 0) + margem
    return x_min, x_max, y_min, y_max


def desenhar_grade(ax, x_min, x_max, y_min, y_max):
    # grade leve em cada inteiro (fica por BAIXO dos pixels)
    for x in range(math.floor(x_min), math.ceil(x_max) + 1):
        ax.axvline(x, linewidth=0.8, color="#7aa6c2", zorder=0)
    for y in range(math.floor(y_min), math.ceil(y_max) + 1):
        ax.axhline(y, linewidth=0.8, color="#7aa6c2", zorder=0)

    ax.set_xlim(x_min, x_max + 1)   # cobre a última célula
    ax.set_ylim(y_min, y_max + 1)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def desenhar_pixels(ax, pontos):
    # cada ponto ocupa exatamente a célula [x,x+1]×[y,y+1]
    for (x, y) in pontos:
        ax.add_patch(
            Rectangle(
                (x, y), 1, 1,
                facecolor="black",
                edgecolor="none",
                antialiased=False,   # evita “vazar”/blur de bordas
                snap=True,           # alinha ao pixel da tela
                zorder=5             # acima da grade
            )
        )


def ticks_centrados(ax, x_min, x_max, y_min, y_max, alvo=12):
    kx0 = math.floor(x_min)
    kx1 = math.ceil(x_max)
    ky0 = math.floor(y_min)
    ky1 = math.ceil(y_max)

    xs_centros = np.arange(kx0, kx1) + 0.5
    ys_centros = np.arange(ky0, ky1) + 0.5
    xlabs = list(map(str, range(kx0, kx1)))
    ylabs = list(map(str, range(ky0, ky1)))

    def passo(n, alvo):
        from math import ceil
        return max(1, ceil(n / alvo))

    sx = passo(len(xs_centros), alvo)
    sy = passo(len(ys_centros), alvo)

    ax.set_xticks(xs_centros[::sx])
    ax.set_yticks(ys_centros[::sy])
    ax.set_xticklabels(xlabs[::sx])
    ax.set_yticklabels(ylabs[::sy])
    ax.tick_params(axis="both", labelsize=8)


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 plotar_grade.py ./seu_programa [args...]")
        sys.exit(1)

    cmd = sys.argv[1:]
    pontos = ler_pontos_de_programa(cmd)
    if not pontos:
        print("Nenhum ponto recebido do algoritmo.")
        return

    x_min_g, x_max_g, y_min_g, y_max_g = limites_cartesianos(pontos, margem=1)

    fig, ax = plt.subplots(figsize=(6, 8))  # ajuste livre
    desenhar_grade(ax, x_min_g, x_max_g, y_min_g, y_max_g)
    desenhar_pixels(ax, pontos)
    ticks_centrados(ax, x_min_g, x_max_g, y_min_g, y_max_g)

    plt.show()


if __name__ == "__main__":
    main()
