#include <stdlib.h>
#include <stdio.h>

void printSpiral(int *matrix){}
void imprimirMatrizEnEspiral(int matriz[][100], int m, int n) {
    int i, k = 0, l = 0;
  
    while (k < m && l < n) {
        // Imprimir la primera fila de la submatriz restante
        for (i = l; i < n; ++i) {
            printf("%d ", matriz[k][i]);
        }
        k++;
  
        // Imprimir la última columna de la submatriz restante
        for (i = k; i < m; ++i) {
            printf("%d ", matriz[i][n - 1]);
        }
        n--;
  
        // Imprimir la última fila de la submatriz restante en orden inverso
        if (k < m) {
            for (i = n - 1; i >= l; --i) {
                printf("%d ", matriz[m - 1][i]);
            }
            m--;
        }
  
        // Imprimir la primera columna de la submatriz restante en orden inverso
        if (l < n) {
            for (i = m - 1; i >= k; --i) {
                printf("%d ", matriz[i][l]);
            }
            l++;
        }
        printf("\n");
    }
}

int main() {
    int m, n;
    printf("Ingrese el número de filas (m) de la matriz: ");
    scanf("%d", &m);
    printf("Ingrese el número de columnas (n) de la matriz: ");
    scanf("%d", &n);
    
    int matriz[100][100];
    printf("Ingrese los elementos de la matriz:\n");
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &matriz[i][j]);
        }
    }
  
    printf("La matriz en forma de espiral es:\n");
    imprimirMatrizEnEspiral(matriz, m, n);
  
    return 0;
}
