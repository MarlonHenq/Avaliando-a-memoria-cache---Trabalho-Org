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
            color[j][i].r=
            (
                color[j][i].r +
                color[j][i].g +
                color[j][i].b
            )/3;
        }
    return 0;
}