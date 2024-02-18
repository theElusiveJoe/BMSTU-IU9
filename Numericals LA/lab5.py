# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

from copy import deepcopy as dc
from collections import namedtuple

import gauss

# %%
def vec_norm(x):
    return max(abs(x))

def mat_norm(x):
    return max(
        (sum(abs(row))-abs(row[i]))/abs(row[i]) 
        for i, row in enumerate(x)
    )

# %%
def gen_matrix(n,m,dd=None):
    A = np.random.rand(n,m)

    if dd is None:
        return A

    if n != m:
        raise RuntimeError(f'диагональное преобладание возможно только у квадратных матриц')

    # генерируем коэффициенты для диагонального преобладания
    dd_coefs = [dd * np.random.random() for _ in range(n)]
    dd_coefs[np.random.randint(0, n)] = 1 * dd
    for i in range(n):
        A[i,i] = (sum(abs(A[i])) - abs(A[i,i])) + dd_coefs[i]

    return A



# %%
def jacobi(A, f, eps=0.05):
    N = len(A)
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
    print(f'ITERS: {i}, EPS = {eps}')
    return x_new

# %%
TestMat = gen_matrix(10, 10, dd=1)

f = np.random.rand(10)
x = jacobi(TestMat, f, eps=0.00001)
print('diff:', np.linalg.norm(TestMat@x - f))

print(f'{mat_norm(TestMat)} <= q < 1')

# %%
HyperParams = namedtuple('HyperParams', ['diag_dom', 'N'])
Test = namedtuple('Test', ['name', 'func'])

def run_tests(hyperparams, tests):
    '''
    вычисляет значения для всех тестов и наборов гиперпараметров
    '''

    # создаем табличку для результатов
    res_df = pd.DataFrame(columns = ['method', 'res', 'N', 'diag_dom', 'x_true'])

    # заполняем табличку
    for hp in tqdm(hyperparams, position=0, leave=True):
        # создаем тестовые данные
        print('generated')
        A = gen_matrix(hp.N,hp.N,hp.diag_dom)
        x = np.random.rand(hp.N)
        b = A@x
        for test in tests:
            # вычисляем и сохраняем
            res_x = test.func(A,b)
            res_df.loc[len(res_df)] = [test.name, res_x, hp.N, hp.diag_dom, x]

    return res_df

def process_results(res_df):
    res_df['abs_diff'] = (res_df['res'] - res_df['x_true']).map(vec_norm)
    res_df = res_df.drop(['res', 'x_true'], axis=1)
    return res_df

def combo(hps, tsts):
    res_df = run_tests(hps, tsts)
    res_df = process_results(res_df)
    return res_df

# %%
HP_LIST = []
for N in [100]:
    for dd in [10, 100]:
        HP_LIST.append(HyperParams(dd,N))

TESTS = [
    Test('normal', lambda x,y: gauss.gaussian(x,y, gauss.NORMAL)),
    Test('jacobi', lambda x,y: jacobi(x,y)),
]

# %%
print(combo(HP_LIST, TESTS))

# %%



