import numpy as np
np.set_printoptions(precision=30)


top = np.array([1,1,1,0], dtype=np.float128)
mid = np.array([4,4,4,4], dtype=np.float128)
low = np.array([0,1,1,1], dtype=np.float128)
res = np.array([5,6,6,5], dtype=np.float128)

def method(low,top,mid,res):
    n = len(mid)
    alpha = np.zeros((n), dtype=np.float128)
    beta = np.zeros((n), dtype=np.float128)

    alpha[0] = -top[0] / mid[0]
    beta[0] = res[0] / mid[0]

    for i in range(1, n):
        alpha[i] = -top[i]/(low[i]*alpha[i-1] + mid[i])
        beta[i] = (res[i] - low[i]*beta[i-1])/(low[i]*alpha[i-1] + mid[i])
    
    x = np.zeros((n), dtype=np.float128)
    x[n-1] = beta[n - 1]

    for i in range(n-1,0,-1):
        x[i-1] = alpha[i-1]*x[i] + beta[i-1]

    return x

def create_matrix(top, mid, low):
    mat = np.diag(mid)
    mat = mat.astype(np.float128)
    for i in range(1,4):
        mat[i-1, i] = top[i-1]
        mat[i, i-1] = low[i]
    return mat

def matmul(mat, vec):
    n = len(vec)
    vec = np.array(vec).reshape(n,1).astype(np.float128)
    d = np.matmul(mat, vec).reshape(1,n)[0].astype(np.float128)
    d = d.astype(np.float128)
    return d

# got x via lab method
x = method(top=top,mid=mid,low=low,res=res)
for t in x:
    print(t)
print(x, x- np.array([1,1,1,1]))
# create tape-matrix 
M = create_matrix(top,mid,low)
# res_start - result if we multiply M by our x 
res_star = matmul(M, x)
r = res - res_star
M = M.astype('float32')
inv = np.linalg.inv(M)
M = M.astype(np.float128)
e = np.matmul(inv, r)
print(e, e.dtype)