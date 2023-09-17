import numpy as np
import pandas as pd

eps = 0.001
alpha, beta = 0.1*13, 0.1*13
N = 4
A = np.array([
    [10 + alpha, -1, 0.2, 2],
    [1, 12-alpha, -2, 0.1],
    [0.3, -4, 12-alpha, 1],
    [0.2, -0.3, -0.5, 8-alpha]
])
Adiag = np.diagonal(A)
B = np.array([1+beta, 2-beta, 3, 1])

F = np.copy(A)
for i in range(N):
    F[i,i] = 0
for i in range(N):
    for j in range(N):
        F[i,j] = F[i,j]/Adiag[i]
Fup = np.copy(F)
Fdown = np.copy(F)
for i in range(N):
    for j in range(N):
        if j > i:
            Fdown[i,j] = 0
        else:
            Fup[i,j] = 0
C = np.copy(B)
for i in range(N):
    C[i] = C[i]/Adiag[i]


def matrixMultByVector(A, x):
    return np.array([ 
        sum([ A[i,j]*x[j] for j in range(N) ]) for i in range(N)
    ])


def simpleNextIter(x):
    return C - matrixMultByVector(F, x)

def zeidelNextIter(x):
    res = np.zeros(N)
    for i in range(N):
        res[i] = C[i] - matrixMultByVector(Fdown, res)[i] - matrixMultByVector(Fup, x)[i] 
    return res

def norm(x):
    return np.max(np.abs(x))

def countDelta(xOld, xNew):
    deltaBig = findFNorm()/(1-findFNorm())*norm(xOld-xNew)
    deltaSmall = deltaBig/norm(xNew)
    return deltaBig, deltaSmall

def checkStop(xOld, xNew):
    return norm(xOld-xNew) < eps
        
def findFNorm():
    return max( np.sum(np.abs(F[i])) for i in range(N) )

def run(method):
    nextIter = simpleNextIter if method == 'simple' else zeidelNextIter
    df = pd.DataFrame({
        'DELTA': [],
        'delta': [],
    })
    xOld = C
    xNew = nextIter(xOld)
    i = 0
    DELTA, delta = countDelta(xOld = xOld, xNew = xNew)
    app = { 
        'delta': delta,
        'DELTA': DELTA
    }
    df = df.append(app, ignore_index=True)
    
    while not checkStop(xOld,xNew):
        i += 1
        xNew, xOld = nextIter(xNew), xNew
        DELTA, delta = countDelta(xOld = xOld, xNew = xNew)
        app = { 
            'delta': delta,
            'DELTA': DELTA
        }
        df = df.append(app, ignore_index=True)
        
    print(df)
    return xNew, delta

def showMethod(method):
    xNew, delta = run(method)
    check = matrixMultByVector(A, xNew) 
    print()
    print("CHECK:", check)
    print("WANT TO GET", B)
    print("DIFFERENCE", check - B)
    print("NORM F", findFNorm())

showMethod('simple')
showMethod('zeidel')




