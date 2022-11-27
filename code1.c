#include <stdio.h>

struct pix{
    unsigned int r, g, b;
};

#define TAM 9999

struct pix color [TAM][TAM];

int main(){
    int i, j;
    for (i = 0; i<TAM; i++)
        for (j=0; j<TAM; j++){
            color[i][j].r=
            (
                color[i][j].r +
                color[i][j].g +
                color[i][j].b
            )/3;
        }
    return 0;
}