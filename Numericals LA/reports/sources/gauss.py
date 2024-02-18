import numpy as np
import pandas as pd
# pd.set_option('float_format', '{:f}'.format)
import matplotlib.pyplot as plt

from sympy.combinatorics import Permutation
from sympy import init_printing
init_printing(perm_cyclic=False, pretty_print=False)
from copy import deepcopy as dc

from collections import namedtuple
from tqdm import tqdm

from basic_ops import *



NORMAL = 1
SWAP_ROWS = 2
SWAP_COLS = 3
SWAP_ALL = 4

def max_elem_in_matrix(A, iter_num):
    m = 0
    mi, mj = -1,-1
    for i in range(iter_num, len(A)):
        for j in range(iter_num, len(A)):
            if abs(A[i][j]) > m:
                m = abs(A[i][j])
                mi, mj = i,j
    return mi, mj

def max_elem_in_row(A, iter_num):
    m = 0
    mi, mj = -1,-1
    i = iter_num
    for j in range(iter_num, len(A)):
        if abs(A[i][j]) > m:
            m = abs(A[i][j])
            mi, mj = i,j

    return mi, mj


def max_elem_in_column(A, iter_num):
    m = 0
    mi, mj = -1,-1
    j = iter_num
    for i in range(iter_num, len(A)):
        if abs(A[i][j]) > m:
            m = abs(A[i][j])
            mi, mj = i,j
    return mi, mj

def permute_rows(A, f, i, j):
    for t in range(len(A)):
        A[i][t], A[j][t] = A[j][t], A[i][t]
    f[i], f[j] = f[j], f[i]
    return A, f

def permute_cols(A, f, i, j):
    for t in range(len(A)):
        A[t][i], A[t][j] = A[t][j], A[t][i]
    return A, f

def gaussian(A, f, mode=NORMAL):
    assert len(A) == len(A[0]) == len(f)
    A, f = dc(A), dc(f)
    N = len(A)
    p = Permutation()

    # прямой ход
    for iter_num in range(N-1):
        # находим максимальный элемент
        mi, mj = None, None
        match mode:
            case 1:
                mi, mj = iter_num, iter_num
            case 2:
                mi,mj = max_elem_in_column(A, iter_num)
                A,f = permute_rows(A, f, mi, iter_num)
            case 3:
                mi,mj = max_elem_in_row(A, iter_num)
                A,f = permute_cols(A, f, mj, iter_num)
            case 4:
                mi,mj = max_elem_in_matrix(A, iter_num)
                A,f = permute_rows(A, f, mi, iter_num)
                A,f = permute_cols(A, f, mj, iter_num)
            case _:
                raise RuntimeError(f'unknown gauss mode: {mode}')

        if mj != iter_num:
            p = p * Permutation(mj+1, iter_num+1)

        if A[iter_num, iter_num] == 0:
            raise RuntimeError(f'матрица вырожденая: {A}')

        for t in range(iter_num+1, N):
            c = A[t, iter_num]/A[iter_num, iter_num]
            A[t] = A[t] - c*A[iter_num]
            f[t] = f[t] - c*f[iter_num]

    # обратный ход
    x = np.zeros(N)
    for iter_num in range(N-1, -1, -1):
        x[iter_num] = (f[iter_num] - scalar_product(x, A[iter_num])) / A[iter_num, iter_num]

    # перестановка элементов x
    for i,j in p.transpositions():
        i,j = i-1, j-1
        x[i], x[j] = x[j], x[i]

    return x