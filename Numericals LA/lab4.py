# %%
import numpy as np
import pandas as pd
from copy import deepcopy as dc

# %% [markdown]
# #### приведение к нормальной форме Фробениуса

# %%
def to_frob_nf(A, log=False):
    A = dc(A)
    N = len(A)
    Bs = np.eye(N)
    for k in range(N-1, 0, -1):
        B, Bi = np.eye(N), np.eye(N)
        B[k-1] = -A[k]/A[k,k-1]
        B[k-1,k-1] = 1/A[k, k-1]
        Bi[k-1] = A[k]
        A = Bi @ A @ B
        Bs = Bs @ B
        if log:
            print('-'*30)
            print('B')
            print(B)
            print('Bi')
            print(Bi)
            print('new A')
            print(A)

    return A, Bs

# %% [markdown]
# #### применение теоремы Гершгольма

# %%
def check_gersh(A):
    assert not (A - A.T).any()
    print('Проверка на симметричность пройдена')

# %%
class Interval:
    a: float
    b: float
    i: int

    def __init__(self, a, b, i) -> None:
        self.a, self.b ,self.i = a, b, i

    def __repr__(self):
        return f'({self.a}<-{self.i}->{self.b})'

    def len(self):
        return self.b - self.a
    
    def __add__(self, o):
        return Interval(
            min(self.a, o.a),
            max(self.b, o.b), 
            self.i + o.i)

    def __hash__(self) -> int:
        return self.i

    def inter(self, o):
        return self.a <= o.a <= self.b or o.a <= self.a <= o.b 
    
    @staticmethod
    def from_row(row, i):
        c = row[i]
        r = abs(row).sum() - abs(row[i])
        return Interval(c-r, c+r, 1)
    
    def __eq__(self, o) -> bool:
        return self.a == o.a and self.b == o.b and self.i == o.i


# %%
def find_gersh(A):
    N = len(A)
    intervals = set

# %%
def find_gersh(A):
    N = len(A)
    intervals = set(Interval.from_row(A[i], i) for i in range(N))

    while True:
        to_remove = set()
        to_add = set()
        for x in intervals:
            for y in intervals - {x}:
                if x.inter(y):
                    to_remove |= {x,y}
                    to_add |= {x+y}
                    break
            else:
                continue
            break

        if to_remove == to_add == set():
            break

        intervals -= to_remove
        intervals |= to_add

    return intervals

# %% [markdown]
# #### построение полиномиальной функции

# %%
class Poly:
    def __init__(self, coefs) -> None:
        self.coefs = coefs[::-1]

    def __call__(self, x) -> float:
        return sum([ x**i * c for i, c in enumerate(self.coefs)])

# %% [markdown]
# #### поиск нулей функции на интервале

# %%
def lin_search(p, a, b, delta = 0.05):
    linsp = np.arange(a, b+delta, delta)
    search_here = []
    for ai, bi in zip(linsp, linsp[1:]):
        if p(ai) * p(bi) < 0:
            search_here.append((ai, bi))

    return search_here

def binary_search(p, a, b, delta = 0.001):
    c = (a+b)/2
    if b-a < delta:
        return c
    if p(c) == 0:
        return c
    try:
        if p(a)*p(c) < 0:
            return binary_search(p, a, c, delta)
        return binary_search(p, c, b, delta)
    except RecursionError:
        return c

# %% [markdown]
# #### метод Крылова

# %%
def krylov_find_ps(A):
    N = len(A)

    # генерируем y_k - е
    y0 = np.zeros(N)
    y0[0] = 1
    Yks = [y0]
    # Yks = [np.random.rand(N)]
    for _ in range(N-1):
        Yks.append(A@Yks[-1])

    # составляем СЛАУ для нахождения p_i
    b = A@Yks[-1]
    Ymat = np.array(dc(Yks[::-1])).T
    
    # находим p_i
    ps = np.linalg.solve(Ymat, b)
    return ps, np.array(Yks[::-1])

# %%
def krylov_eigenvecs(A, Yks, ps, lambdas):
    N = len(A)

    # составляем матрицу кожффициентов многочленов Q_i
    Q = np.empty((N,N))
    for i in range(N):
        for j in range(N):
            Q[j,i] = 1 if j == 0 else (lambdas[i]*Q[j-1,i] + ps[j-1])

    eigenvecs = []
    for i in range(N):
        x = np.zeros(N)
        for j in range(N):
            x += Q[j,i]*Yks[j]
        eigenvecs.append(x/np.linalg.norm(x))
    
    return eigenvecs


# %% [markdown]
# #### проверки результатов

# %%
def find_eigenvector(B, alpha):
    vec = np.array([alpha**i for i in range(len(B))][::-1])
    eigv = B.dot(vec)
    return eigv / np.linalg.norm(eigv)

def check_orthogonality(vecs):
    A = np.array([[v1@v2 for v2 in vecs] for v1 in vecs])
    print('ОРТОГОНАЛЬНОСТЬ:')
    print(A)

def check_eigenvalues(A, eigenvalues):
    print('|tr(A) - sum(eigenvalues)| =', abs(sum(eigenvalues) - np.trace(A)))

# %% [markdown]
# #### все вместе

# %%
DANYLEVSKY = 1
KRYLOV = 2

# %%
def main(TestMat, method=DANYLEVSKY):
    print(f'method: {method}')
    # проверяем симметричность
    check_gersh(TestMat)

    # ищемм коэффициенты характерристического многочлена
    if method == DANYLEVSKY:
        P, B = to_frob_nf(TestMat)
        P = P[0]
    elif method == KRYLOV:
        P, Yks = krylov_find_ps(TestMat)
    else: 
        raise RuntimeError(f'unknown method {method}')

    # строим хар. мн-н
    p = Poly([1] + list(-P))
    print(p.coefs)

    # ищем интервалы Гершгорина
    intervals = find_gersh(TestMat)

    # ищем нули полинома
    eigenvalues = []
    for inter in intervals:
        eigenvalues += [binary_search(p, *sh) for sh in lin_search(p, inter.a, inter.b)]


    print('СОБСТВЕННЫЕ ЗНАЧЕНИЯ:\n', eigenvalues)
    print()
    check_eigenvalues(TestMat, eigenvalues)
    print()

    if method == DANYLEVSKY:
        eigenvectors = np.array([find_eigenvector(B, alpha) for alpha in eigenvalues ])
    elif method == KRYLOV:
        eigenvectors = np.array(krylov_eigenvecs(TestMat, Yks, -P, eigenvalues))
    
    
    print('СОБСТВЕННЫЕ ВЕКТОРЫ:\n', eigenvectors)
    check_orthogonality(eigenvectors)

    return eigenvalues

# %% [markdown]
# ### Тестирование

# %%
TestMat = np.array([2.2, 1, 0.5, 2, 1, 1.3, 2, 1, 0.5, 2, 0.5, 1.6, 2, 1, 1.6, 2]).reshape((4,4))

# %%
main(TestMat, method=DANYLEVSKY)

# %% [markdown]
# ##### произвольной размерности

# %%
random_mat = np.random.rand(10,10)
random_mat += random_mat.T
random_mat
main(random_mat, method=DANYLEVSKY)

# %%



