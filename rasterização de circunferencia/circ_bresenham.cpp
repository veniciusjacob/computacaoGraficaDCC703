#include <iostream>

using namespace std;

inline void ligar_pixel(int x, int y) {
    std::cout << x << " " << y << "\n";
}

void bresenham(int xc, int yc, int r) {
    // começa com coordenadas do ponto (0, 0)
    // para x = 0 -> x² + y² = r² -> 0 + y² = r² 
    // logo -> y = r
    
    int x = 0; 
    int y = r;

    int p = 1 - r; // parâmetro de de decisão

    // só calculamos o primeiro octante do topo até a diagonal x = y
    while (x <= y){
        ligar_pixel(xc + x, yc + y);
        ligar_pixel(xc + y, yc + x);
        ligar_pixel(xc - x, yc + y);
        ligar_pixel(xc - y, yc + x);
        ligar_pixel(xc - x, yc - y);
        ligar_pixel(xc - y, yc - x);
        ligar_pixel(xc + x, yc - y);
        ligar_pixel(xc + y, yc - x);

        //x sempre incrementa x + 1. O proximo pixel será (x + 1, y) ou (x + 1, y - 1)

        // se p >=0, fora da circunferência, indica que o ponto médio está muito acima, fora da circunferência, decrementar y
        if (p >= 0) {
            y = y - 1;
            p = p + 2*x - 2*y + 5;
            x++;
        } else { // se p < 0, ponto médio está dentro da circunferência, manter y
            p = p + 2*x + 3;
            x++;
        }

    }
    
}

int main() {
    bresenham(0, 0, 10);
    return 0;
}