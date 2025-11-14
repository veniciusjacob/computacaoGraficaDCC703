#include <iostream>
#include <cmath>

using namespace std;


void ligar_pixel(int x, int y){
    // cout << x << " " << y << "\n";
}

void metodo_analitico(int x1, int y1, int x2, int y2) {
    // se x1 == x2 linha vertical
    if( x1 == x2) {
          for(int y = y1; y <= y2; y++) {
            ligar_pixel(x1, y);
          }
    } else {

        // calcula coeficiente angular e linear
        float m, b;
        m = float(y2 - y1) / float(x2 - x1);
        b = y2 - m * x2;

        //  vai do x1 ao x2
        for (int x = x1; x <= x2; x++) {
            // calcula y e arredonda
            float y =  round(m * x + b);

            ligar_pixel(x, y);
        }
    }
}

int main () {
    metodo_analitico(0,0, 10000, 4123);
    return 0;
}
