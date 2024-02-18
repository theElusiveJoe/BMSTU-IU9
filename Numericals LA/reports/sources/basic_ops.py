import numpy as np
from copy import deepcopy as dc


def norm(x: np.array):
    return np.sqrt(sum([xi**2 for xi in x]))

def scalar_product(x,y):
    return (sum([xi*yi for xi, yi in zip(x,y)]))

def mat_vec_product(a, x):
    assert len(a[0]) == len(x)

    return np.array([
        scalar_product(y,x)
        for y in a
    ])

def matrix_product(a, b):
    k, l = len(a), len(a[0])
    l2, m = len(b), len(b[0])
    assert l == l2

    return np.array(
        [
            [
                sum(a[i][t]*b[t][j] for t in range(l))
                for j in range(m)
            ]
            for i in range(k)
        ]
    )

def transpose(a):
    return np.array([
        [a[j][i]for j in range(len(a))]
        for i in range(len(a[0]))
    ])


def gen_matrix(n,m,a=-1, b=1, dd=None):
    A = np.random.rand(n,m)
    A *= b-a
    A += a

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


