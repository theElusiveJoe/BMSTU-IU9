# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

from copy import deepcopy as dc
from collections import namedtuple

import gauss
from basic_ops import *

# %%
def vec_norm(x):
    return max(abs(x))

def mat_norm(x):
    return max(
        (sum(abs(row))-abs(row[i]))/abs(row[i]) 
        for i, row in enumerate(x)
    )

# %%
def jacobi(A, f, eps=0.05):
    N = len(A)
    A, f = dc(A), dc(f)

    D = np.diag(np.diag(A))
    Dm = np.diag(1/np.diag(A))
    LU = A - D

    x = np.array([A[i,i] * f[i] for i in range(N)])
    diff = np.ones(N)*9999
    i = 0
    while vec_norm(diff) > eps:
        i+=1
        x_new = Dm @ (f - LU@x)
        diff = abs(x_new - x)
        x = x_new
    print(f'ITERS: {i}')
    return x_new

# %%
def zeidel(A, f, eps=0.05):
    N = len(A)
    A, f = dc(A), dc(f)

    # x = np.array([A[i,i] * f[i] for i in range(N)])
    x = np.random.random(N)
    diff = np.ones(N)*9999
    c = 0
    while vec_norm(diff) > eps:
        c+=1
        x_new = np.empty(N)
        
        for i in range(N):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i+1, N))
            x_new[i] = (f[i] - s1 - s2) / A[i,i]

        diff = abs(x_new - x)
        x = x_new
        
    print(f'ITERS: {c}')
    return x_new

# %%
for N in [5,10,100,200]:
    for dd in [100]:
        A = gen_matrix(N,N, dd=100)
        x = np.random.rand(N)
        b = mat_vec_product(A, x)

        print(f'size: {N}, dd: {dd}')
        print('    jacobi', end = ' ')
        jacobi(A, b, 0.0005)
        print('    zeidel', end = ' ')
        zeidel(A, b, 0.0005)
    

# %%


# %%



