#include <iostream>
#include <cmath>


using namespace std;

inline void ligar_pixel(int x, int y) {
    // std::cout << x << " " << y << "\n";
}

void incremental_simetria(int x_c, int y_c, int r) {
    double x = r;  //cos(0) =  x / r -> x = r.cos(0) =  r
    double y = 0; //sen(0) = y / r -> y = r.sen(0) =  0

    // incremento do angulo entre um ponto e o próximo
    double theta = 1.0 / r;

    // valores de cos e sen fixos
    double c = cos(theta);
    double s = sin(theta);
    
    // variável temporária para armazenar o valor de x antigo0 na hora de atualizar (x, y)
    double xt; 
    
    // percorre o primeiro octante
    while (y <= x){
        ligar_pixel(round(x_c + x), round(y_c + y)); //1
        ligar_pixel(round(x_c + y), round(y_c + x)); // 2
        ligar_pixel(round(x_c - y), round(y_c + x)); // 3
        ligar_pixel(round(x_c - x), round(y_c + y)); // 4
        ligar_pixel(round(x_c - x), round(y_c - y)); // 5
        ligar_pixel(round(x_c - y), round(y_c - x)); // 6
        ligar_pixel(round(x_c + y), round(y_c - x)); // 7
        ligar_pixel(round(x_c + x), round(y_c - y)); // 8
        
    
        // guarda valor antigo de x
        xt = x;

        // atualiza x e y
        x = (x * c - y * s);
        y = (y * c + xt * s);
        
    }
    
}

int main()
{
    incremental_simetria(0, 0, 1000);
    return 0;
}
