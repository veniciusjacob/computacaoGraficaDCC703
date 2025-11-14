#include <iostream>
#include <cmath>

const double PI = 3.14159265358979323846;

inline void ligar_pixel(int x, int y) {
    // std::cout << x << " " << y << "\n";
}

void parametrica(int xc, int yc, int r) {
    // x = xc + r.cos(t)
    // y = yc + r.sen(t)

    int x = xc + r; // ponto inicial xc, t = 0 -> cos(0) = 1 
    int y = yc; // ponto inicial yc, t = 0 -> sen(0) = 0

    for (int t = 1; t <= 360; t++){

        ligar_pixel(x, y);

        double rad = (PI * t) / 180; // converter graus para radianos

        x = round(xc + r * cos(rad));
        y = round(yc + r * sin(rad)); 


    }
}



int main() {
    // parametrica(0, 0, 10);  
    parametrica(0, 0, 1000);
    return 0;
}