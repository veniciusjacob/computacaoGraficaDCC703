#include <iostream>
#include <vector>
#include <limits>
using namespace std;

// img[y][x]: 0 = fundo, 1 = borda, 2 = preenchido
int LARG = 0, ALT = 0;
vector<vector<int>> img;

int getPixel(int X, int Y) {
    if (X < 0 || X >= LARG || Y < 0 || Y >= ALT) return -1;
    return img[Y][X];
}

void setPixel(int X, int Y, int cor) {
    if (X < 0 || X >= LARG || Y < 0 || Y >= ALT) return;
    img[Y][X] = cor;
}

// FloodFill(X, Y, cor, novaCor)
void FloodFill(int X, int Y, int cor, int novaCor) {
    if (getPixel(X, Y) == cor) {
        setPixel(X, Y, novaCor);
        FloodFill(X + 1, Y,     cor, novaCor);
        FloodFill(X,     Y + 1, cor, novaCor);
        FloodFill(X - 1, Y,     cor, novaCor);
        FloodFill(X,     Y - 1, cor, novaCor);
    }
}

int main(int argc, char* argv[]) {
    if (argc < 3) return 1;         // uso: ./floodfill xc yc
    int xc = stoi(argv[1]);
    int yc = stoi(argv[2]);

    vector<pair<int,int>> borda;
    int x, y;
    int minx = numeric_limits<int>::max();
    int maxx = numeric_limits<int>::min();
    int miny = numeric_limits<int>::max();
    int maxy = numeric_limits<int>::min();

    while (cin >> x >> y) {
        borda.push_back({x, y});
        if (x < minx) minx = x;
        if (x > maxx) maxx = x;
        if (y < miny) miny = y;
        if (y > maxy) maxy = y;
    }
    if (borda.empty()) return 1;

    int minxExp = minx - 1;
    int minyExp = miny - 1;
    int maxxExp = maxx + 1;
    int maxyExp = maxy + 1;

    LARG = (maxxExp - minxExp) + 1;
    ALT  = (maxyExp - minyExp) + 1;
    img.assign(ALT, vector<int>(LARG, 0));      // tudo fundo

    for (auto &p : borda) {                     // borda = 1
        int X = p.first  - minxExp;
        int Y = p.second - minyExp;
        setPixel(X, Y, 1);
    }

    int Xc = xc - minxExp;
    int Yc = yc - minyExp;
    FloodFill(Xc, Yc, 0, 2);                    // preenche só fundo (0 -> 2)

    for (int Y = 0; Y < ALT; Y++)               // imprime só interior (2)
        for (int X = 0; X < LARG; X++)
            if (img[Y][X] == 2) {
                int realX = X + minxExp;
                int realY = Y + minyExp;
                cout << realX << " " << realY << "\n";
            }

    return 0;
}
