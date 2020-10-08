#include <stdio.h>
#include<omp.h>
#include <time.h>
#include <stdlib.h>
#define n 4
int main()
{
	int i, j;
	srand(time(NULL)); //---hace uso del reloj interno de la computadora para controlar la elección
	int A[n][n], B[n][n], C[n][n];
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			A[i][j] = (rand() % 4) + 1;
			B[i][j] = (rand() % 4) + 1;
			C[i][j] = 0;
		}
	}
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			for (int x = 0;x < n;x++) {
				C[i][j]= C[i][j] + (A[i][x] * B[x][j]);
			}
		}
	}
  for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			printf("%d ", C[i][j]);
		}
    printf("\n");
  }
}
