#include <iostream>
#include <cstdlib> 
#include <cmath>


void ligar_pixel(int x, int y){
    // std::cout << x << " " << y << "\n";
}

void metodo_DDA(int x1, int y1, int x2, int y2) {
    // calcular variações para encontrar variavel dominante
    int dx = x2 - x1;
    int dy = y2 -y1;

    // se dx > dy, incremeta x de 1 e calcula incremento de y
    if (abs(dx) > abs(dy)) {
        float incremento = float(dy) / float(dx);
        float y = y1; // iniciliza y com y1

        for(int x = x1; x <= x2; x++){
            ligar_pixel(x, round(y));
            y = y + incremento;
        }
    } else {
        //  se dy > dx, incrementa y de 1 e calcula incremento de x
        float incremento = float(dx) / float(dy);
        float x = x1;

        for(int y = y1; y <= y2; y++){
            ligar_pixel(round(x), y);
            x = x + incremento;
        }
    }
}

int main () {

    // metodo_DDA(0, 0, 5, 2);
    metodo_DDA(0,0, 10000, 4123);
    return 0;
}