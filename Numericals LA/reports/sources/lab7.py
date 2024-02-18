# %%
import numpy as np

from basic_ops import  gen_matrix

# %%
def holetsky(A: np.ndarray):
    N = len(A)

    L = np.zeros((N,N))

    L[0,0] = np.sqrt(A[0,0])

    for j in range(1, N):
        L[j,0] = A[j,0]/L[0,0]

    for i in range(1, N):
        for j in range(1, i):
            L[i,j] = (A[i,j] - L[i,:j]@L[j,:j]) / L[j,j]
        L[i,i] = np.sqrt(A[i,i] - np.sum(L[i,:i+1]**2))

    return L


# %%
def lu(A: np.ndarray):
    N = len(A)

    L = np.identity(N)
    U = np.zeros((N,N))

    for i in range(N):
        for j in range(N):
            if i <= j:
                U[i,j] = A[i,j] - L[i,:i]@U[:i,j].T
            else:
                L[i,j] = (A[i,j] - L[i,:j]@U[:j,j])/U[j,j]

    return L, U

# %%
N = 5
a,b = -1, 1
A = gen_matrix(N,N, a, b)
A = A@A.T

L = holetsky(A) 
LT = L.T

print(f'Holetsky euclid diff norm: {np.linalg.norm(A - L@LT)}; N = {N}')

L,U = lu(A)

print(f'LU euclid diff norm: {np.linalg.norm(A - L@U)}; N = {N}')

# %%



