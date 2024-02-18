# %%
import numpy as np
import matplotlib.pyplot as plt

import basic_ops, eigenvalues

# %%
def vec_norm(x):
    return max(abs(x))

def mat_norm(x):
    return max(
        abs((sum(abs(row))-abs(row[i])) \
        / 
        abs(row[i]))
        for i, row in enumerate(x)
    )

# %%
def gen_matrix(n,m,dd=None, symmetric=False):
    A = np.random.rand(n,m)
    if symmetric:
        A = (A+A.T)

    if dd is None:
        return A

    if n != m:
        raise RuntimeError(f'диагональное преобладание возможно только у квадратных матриц')

    # генерируем коэффициенты для диагонального преобладания
    dd_coefs = [dd * np.random.random() for _ in range(n)]
    dd_coefs[np.random.randint(0.3, n)] = 1 * dd
    for i in range(n):
        A[i,i] = (sum(abs(A[i])) - abs(A[i,i])) + dd_coefs[i]

    return A

# %%
def gen_slae(N):
    A = gen_matrix(N,N, dd=N/2, symmetric=True)
    print(A)
    x = np.random.rand(N)
    b = A@x
    return A, x, b

# %%
def one_param(A, f, tao, true_x, eps=0.0001, Aiv=None):
    N = len(A)

    # x = Px + g
    P = np.eye(N) - tao*A
    g = tao*f

    # проверим, что ||P|| < 1
    if Aiv is None:
        Aiv = eigenvalues.get_eigenvalues_and_eigenvectors(A)
    Piv = 1 - tao*np.array(Aiv)
    
    print(f'tao: {tao}, norm P: {max(abs(Piv))}', end=' ')

    try:
        assert max(abs(Piv))< 0.999
    except:
        print(f'iters: -1, norm P is too big')
        return None ,-1
    
    max_lambda = max(Piv)

    x_old = np.array([A[i,i] * f[i] for i in range(N)])
    # x_old = np.zeros(N)
    diff = np.ones(N)*9999
    iters_num = 0

    while vec_norm(diff) > eps:
        if iters_num > 1000:
            print(f'iters: {iters_num}, too many iters')   
            return None, -1

        x_new = P@x_old + g

        e1 =  np.linalg.norm(x_new - true_x)
        e2 = abs(max_lambda) * np.linalg.norm(x_old - true_x)
       
        # try:
        assert(np.linalg.norm(true_x - x_new) < max(Aiv) * np.linalg.norm(true_x - x_old))
        #     assert ((e2 - e1) >= 0) or (abs(e1-e2) < 0.0001)
        # except:
        #     print(f'iters: {iters_num}, bad covergence', e1, e2)
        #     return None, -1
        
        diff = x_old - x_new
        x_old=x_new
        iters_num+=1
    
    print(f'iters: {iters_num}')

    return x_new, iters_num

# %%
np.random.seed()

def analysis(N):
    # генерируем систему
    A = gen_matrix(N,N, dd=60, symmetric=True)
    x = np.random.rand(N)
    b = A@x

    # проверяем A
    assert mat_norm(A) < 1
    eigvals = eigenvalues.get_eigenvalues_and_eigenvectors(A, method=2)
    # eigvals = np.linalg.eigvals(A)
    assert all(map(lambda x: x>0, eigvals))

    # запускаем на разных тао
    taos = np.linspace(0.05, 2/max(eigvals), 50, True)
    res = [
        one_param(A, b, tao, true_x=x, Aiv=eigvals, eps=0.0001) 
        for tao in taos]
    
    # зависимость количества итераций от тао
    iters_num = list(map(lambda x: x[1], res))
    plt.plot(taos, iters_num)

    # нахдим оптимальное тао
    tao_opt = 2/(min(eigvals) + max(eigvals))
    iters_opt = one_param(A,b, tao_opt, x)[1]
    plt.scatter(tao_opt, iters_opt)

    print(f'tao optimal = {tao_opt}')
    print(f'iters optimal:', iters_opt)

    
analysis(5)

# %%


# %%



