#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def ler_pontos_de_programa(comando, entrada_para_programa=None):
    if entrada_para_programa is None:
        proc = subprocess.Popen(comando, stdout=subprocess.PIPE, text=True)
    else:
        proc = subprocess.Popen(
            comando,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
        )
        proc.stdin.write(entrada_para_programa)
        proc.stdin.close()

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
    x_min = min(xs) - margem
    x_max = max(xs) + margem
    y_min = min(ys) - margem
    y_max = max(ys) + margem
    return x_min, x_max, y_min, y_max


def desenhar_grade(ax, x_min, x_max, y_min, y_max):
    for x in range(math.floor(x_min), math.ceil(x_max) + 1):
        ax.axvline(x, linewidth=0.8, color="#7aa6c2", zorder=0)
    for y in range(math.floor(y_min), math.ceil(y_max) + 1):
        ax.axhline(y, linewidth=0.8, color="#7aa6c2", zorder=0)

    ax.set_xlim(x_min, x_max + 1)
    ax.set_ylim(y_min, y_max + 1)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def desenhar_pixels_borda(ax, pontos):
    for (x, y) in pontos:
        ax.add_patch(
            Rectangle((x, y), 1, 1,
                      facecolor="black",
                      edgecolor="none",
                      zorder=10)
        )


def desenhar_pixels_fill(ax, pontos):
    for (x, y) in pontos:
        ax.add_patch(
            Rectangle((x, y), 1, 1,
                      facecolor="red",
                      edgecolor="none",
                      zorder=5)
        )


def set_ticks(ax, x_min, x_max, y_min, y_max):
    xticks = range(math.floor(x_min), math.ceil(x_max) + 1)
    yticks = range(math.floor(y_min), math.ceil(y_max) + 1)
    ax.set_xticks([x + 0.5 for x in xticks])
    ax.set_yticks([y + 0.5 for y in yticks])
    ax.set_xticklabels([str(x) for x in xticks])
    ax.set_yticklabels([str(y) for y in yticks])
    ax.tick_params(axis="both", labelsize=8)


def main():
    if len(sys.argv) < 5:
        print("Uso: python3 teste.py <prog_circ> <prog_fill> <xc> <yc>")
        return

    prog_circ = sys.argv[1]
    prog_fill = sys.argv[2]
    xc = int(sys.argv[3])
    yc = int(sys.argv[4])

    # 1) borda
    pontos_borda = ler_pontos_de_programa([prog_circ])
    if not pontos_borda:
        print("Nenhum ponto da circunferência recebido.")
        return

    x1_min, x1_max, y1_min, y1_max = limites_cartesianos(pontos_borda)
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    desenhar_grade(ax1, x1_min, x1_max, y1_min, y1_max)
    desenhar_pixels_borda(ax1, pontos_borda)
    set_ticks(ax1, x1_min, x1_max, y1_min, y1_max)
    ax1.set_title("Circunferência (borda)")

    # 2) preenchimento
    borda_str = "\n".join(f"{x} {y}" for (x, y) in pontos_borda) + "\n"
    pontos_fill = ler_pontos_de_programa(
        [prog_fill, str(xc), str(yc)],
        entrada_para_programa=borda_str,
    )

    if pontos_fill:
        todos = pontos_fill + pontos_borda
        x2_min, x2_max, y2_min, y2_max = limites_cartesianos(todos)
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        desenhar_grade(ax2, x2_min, x2_max, y2_min, y2_max)
        desenhar_pixels_fill(ax2, pontos_fill)
        desenhar_pixels_borda(ax2, pontos_borda)
        set_ticks(ax2, x2_min, x2_max, y2_min, y2_max)
        ax2.set_title("Circunferência Preenchida (FloodFill)")
    else:
        print("Nenhum ponto preenchido recebido do floodfill.")

    plt.show()

if __name__ == "__main__":
    main()
