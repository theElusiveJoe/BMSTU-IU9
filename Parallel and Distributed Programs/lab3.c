#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

#define N 32768

double* mult_m_v(double** m, double* v) {
  double* res;
  res = (double*)malloc(sizeof(double) * N);
  int i;

  #pragma omp parallel for shared(m, v, res) private(i)
  for (i = 0; i < N; i++){
      res[i] = 0;
      for (int j = 0; j < N; j ++) {
        res[i] += (m[i][j] * v[j]);
      }
  }
  return res;
}


void mult_v_s(double* v, double s) {
    int i;
    #pragma omp parallel for shared(v) private(i)
    for (i = 0; i < N; i++){
        v[i] *= s;
    }
}


void v1_ravno_v1_minus_v2(double* v1, double* v2) {
    int i;
    #pragma omp parrallel for shared(self, v) private(i) 
    for (i = 0; i < N; i ++){
        v1[i] -= v2[i];
    }
}


double norm(double* v) {
    int i;
    int len = 0;
    #pragma omp parrallel for shared(v) privare(i) reduction (+:len)
    for (i = 0; i < N; i++){
        len += (v[i]*v[i]);
    }

    len = sqrt(len);
    return len;
}

double scalar_product(double* v1, double* v2) {
    int i;
    double len = 0;
    #pragma omp parallel for shared(v1, v2) private(i) reduction (+:len)
    for (i = 0; i < N; i++){
        len += (v1[i]*v2[i]);
    }

    return len;
}


int main(){  
    #ifdef _OPENMP
        printf("OpenMP is supported!\n");
    #endif

    double eps = 0.0000001;
    double tao;
    
    double **A;
    A = (double**)malloc(sizeof(double*) * N);
    for (int i = 0; i < N; i++) {
        A[i] = (double*)malloc(sizeof(double)*N);
        for (int j = 0; j < N; j++) {
            if (i == j){
                A[i][j] = 2.0;
            } else { 
                A[i][j] = 1.0;
            }
        }
    }

    double* x;
    double* b;
    x = (double*)malloc(sizeof(double) * N);
    b = (double*)malloc(sizeof(double) * N);
    for (int i = 0; i < N; i ++){
        x[i] =  0;
        b[i] =  N+1;
    }

    double* y;
    double* ay;
    while(1) {
        // y = Ax-b
        y = mult_m_v(A, x);
        v1_ravno_v1_minus_v2(y, b);

        if ((norm(x)/norm(y)) < eps) {
            printf("Сошлось");
            free(y);
            break;
        };

        // ay = A * y 
        ay = mult_m_v(A, y);

        tao = scalar_product(y, ay) / scalar_product(ay, ay);
        // x = x - tao*y
        mult_v_s(y, tao);
        v1_ravno_v1_minus_v2(x, y);

        free(y);
        free(ay);
    }
    
    free(x);
    free(b);
    for (int i = 0; i < N; i++) {
        free(A[i]);
    }
    free(A);
    
    return 0;
}