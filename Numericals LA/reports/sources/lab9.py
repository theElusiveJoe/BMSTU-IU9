# %%
import numpy as np

from basic_ops import gen_matrix

# %%
def svd(C: np.ndarray, iters=100):
    CTC = C.T @ C
    eigen_values, eigen_vectors = np.linalg.eig(CTC)
    indxs = np.argsort(eigen_values)[::-1]
    eigen_values = eigen_values[indxs]
    eigen_vectors = eigen_vectors[:, indxs]

    SIGMA = np.diag(np.sqrt(eigen_values))
    SIGMA_INV = np.diag(1/np.sqrt(eigen_values))

    V = eigen_vectors

    for x in V:
        for y in V:
            if np.linalg.norm(x-y) < 0.001: 
                pass
            else: 
                assert x@y , 0.0001

    O = np.empty((len(V), len(V)))
    for i, x in enumerate(V):
        for j, y in enumerate(V):
            O[i][j] = x@y

    print(O)


    U = C @ V @ SIGMA_INV

    return U, SIGMA, V.T


def demo(n: int, m: int):
    A = gen_matrix(n, m)
    
    if n < m:
        A = A.T

    U, SIGMA, V = svd(A)
    u, sigma, v = np.linalg.svd(A, full_matrices=True)

    print(f'U: \n{U}')
    print(f'u: \n{u}')
    print(f'SIGMA: \n{SIGMA}')
    print(f'sigma: \n{sigma}')
    print(f'V: \n{V}')
    print(f'v: \n{v}')

    resA = U @ SIGMA @ V
    print(f'A:\n{A}')  
    print(f'resA:\n{resA}')

    assert np.linalg.norm(A - resA) < 0.001

    for x, y in zip(U.T, u.T):
        assert np.linalg.norm(x - y) < 0.001 or np.linalg.norm(x + y) < 0.001
    
    for x, y in zip(V, v):
        assert np.linalg.norm(x - y) < 0.001 or np.linalg.norm(x + y) < 0.001

    if n < m:
        V.T, SIGMA, U.T

    return U, SIGMA, V
    # assert np.linalg.norm(U - u) < 0.1
    # assert np.linalg.norm(np.diag(SIGMA) - sigma) < 0.001
    # assert np.linalg.norm(V - v) < 0.001


demo(4, 5)


