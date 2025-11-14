#include <iostream>

void ligar_pixel(int x, int y){
    // std::cout << x << " " << y << "\n";
}

void bresenhamLine(int x1, int y1, int x2, int y2){
    // calcular diferenças
    int dx = x2 - x1;
    int dy = y2 - y1;

    // paramentro de decisão
    // decide se o proximo pixel será (x+1, y) ou (x+1, y+1) ou seja, mover na horizontal ou diagonal
    int p = 2 * dy - dx;

    int y = y1;

    for(int x = x1; x <= x2; x++) {
        

        ligar_pixel(x, y);

        // se p >= 0, próximo pixel é (x+1, y+1) - mover na diagonal, o novo pixel está acima da reta
        if(p >= 0) {
            // x = x + 1; não precisa porque x já é incrementado no for
            y = y + 1;
            p = p + 2 * (dy - dx);

        } else { // se p < 0, próximo pixel é (x+1, y) - mover na horizontal, o novo pixel está abaixo da reta
            // x = x + 1; não precisa porque x já é incrementado no for, só atualiza p
            p = p + 2 * dy;

        }
    }

}

int main () {
    bresenhamLine(0,0, 10000, 4123);
    return 0;
}