# %%
import numpy as np
from basic_ops import  gen_matrix

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
def solve(A, f):
    N = len(A)
    L, U = lu(A)
    y = [f[0]]

    for i in range(1, N):
        y.append(f[i] - L[i, :i]@y[:i])
    
    x = np.zeros(N)
    x[N-1] = y[N-1]/U[N-1,N-1]

    for i in range(N-2, -1, -1):
        x[i] = (y[i] - U[i,i+1:]@x[i+1:])/U[i,i]

    return x

# %%
N = 100
a, b = -1, 1
A = gen_matrix(N,N, a, b)
A = A@A.T

x = np.random.random(N)

f = A @ x

x_my = solve(A, f)
print(np.linalg.norm(x - x_my))
print(np.linalg.norm(f - A@x_my))




