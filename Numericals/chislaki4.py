import numpy as np
import pandas as pd
pd.options.display.float_format = '{:.10f}'.format

p = -4
q = 0 

c1 = (3.56+301/1024)/4

def analytic_answer(x):
    return -1/28 * x**7 - \
            1/16 * x**6 - \
            3/32 * x**5 - \
            15/128 * x**4 - \
            15/128 *  x**3 - \
            45/512* x**2 - \
            301/1024 *x + \
            c1* np.e**(4*x) + \
            (-c1)
def f(x):
    return x**6+1

x0 = 0
y0 = analytic_answer(x0)
xn = 1
yn = analytic_answer(xn)
y0, yn

def create_diagonals():
    top = []
    mid = []
    low = []
    res = []
    
    mid.append(h*h*q-2)
    top.append(1+h/2*p)
    
    x1 = x0 + (xn-x0)*h*1
    f1 = analytic_answer(x1)
    res.append(h*h*f1 - y0*(1-h/2*p))
    
    for i in range(2, n-1):
        low.append(1-h/2*p)
        mid.append(h*h*q-2)
        top.append(1+h/2*p)
        
        xi = x0 + (xn-x0)*h*i
        fi = f(xi)
        res.append(h*h*fi)
    
    low.append(1-h/2*p)
    mid.append(h*h*q-2)
    
    xn_1 = x0 + (xn-x0)*h*(n-1)
    fn_1 = analytic_answer(xn_1)
    res.append(h*h*fn_1 - yn*(1+h/2*p))
    
    return [0] + low, mid, top + [0], res
    
def solve_stripe(low, mid, top, res):
    n = len(mid)
    low = np.array(low)
    mid = np.array(mid)
    top = np.array(top)
    res = np.array(res)
    
    alpha = np.zeros((n,))
    beta = np.zeros((n,))
    alpha[0] = -top[0] / mid[0]
    beta[0] = res[0] / mid[0]

    for i in range(1, n):
        alpha[i] = -top[i]/(low[i]*alpha[i-1] + mid[i])
        beta[i] = (res[i] - low[i]*beta[i-1])/(low[i]*alpha[i-1] + mid[i])

    x = np.zeros((n,))
    x[n-1] = beta[n - 1]

    for i in range(n-1,0,-1):
        x[i-1] = alpha[i-1]*x[i] + beta[i-1]

    return list(x)

def create_matrix(low, mid, top):
    mat = np.diag(mid)
    for i in range(1,len(mid)):
        mat[i-1, i] = top[i-1]
        mat[i, i-1] = low[i]
    return mat


low, mid, top, res = create_diagonals()
m = create_matrix(low,mid,top)
res_my = np.array(
    [y0] + list(solve_stripe(low, mid, top, res)) + [yn]
)


res_true = np.array(
    [y0] + list(np.vectorize(analytic_answer)(np.linspace(0.1,1,9,False))) + [yn]
)
def shooting(Oh):
    y_0 = np.empty(n+1)
    y_1 = np.empty(n+1)
    
    y_0[0] = y0
    y_0[1] = y0 + Oh
    y_1[0] = 0
    y_1[1] = Oh

    for i in range(1, n):
        y_0[i+1] = (f(x0+i*h)*h**2 + (2-q*h**2)*y_0[i] - (1-p*h/2)*y_0[i-1]) / (1 + p*h/2)
        y_1[i+1] = ((2-q*h**2)*y_1[i] - (1-p*h/2)*y_1[i-1]) / (1 + p*h/2)

    if abs(y_1[n]) < 0.001:
        return gun(Oh+1)
    else:
        c1 = (yn - y_0[n]) / y_1[n]
    return [y_0[i] + c1 * y_1[i] for i in range(n+1)]
