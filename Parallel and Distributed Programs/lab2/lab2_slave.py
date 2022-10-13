import time
from mpi4py import MPI
import numpy as np
from numpy.linalg import norm, det
import sys
np.random.seed(42)


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


MATRIX_SIZE = 2**13
MATRIX_SPLIT = int(sys.argv[1])

a = np.zeros((MATRIX_SIZE, MATRIX_SIZE), dtype=np.single)
for i in range(MATRIX_SIZE):
    # print('initing a. row', i, rank),
    for j in range(MATRIX_SIZE):
        a[i, j] = 2 if i == j else np.random.random()
ans = np.zeros((MATRIX_SIZE), dtype=np.single)
for i in range(MATRIX_SIZE):
    ans[i] = np.random.random()
b = np.matmul(a, ans[:, None]).T[0]

x = np.zeros((MATRIX_SIZE), dtype=np.single)

epsilon = 0.00001


def mult_matrix_by_vector(m, v):
    v = v[:, None]
    # создаем буфер для вычислений
    part_a = np.empty(shape=(MATRIX_SIZE//MATRIX_SPLIT,
                      MATRIX_SIZE), dtype=np.single)
    # забираем свой кусочек
    comm.Scatter(m, part_a, root=0)
    # перемножили
    part_a = part_a @ v
    # выделяем место под результат
    res = None
    if rank == 0:
        res = np.empty(shape=(MATRIX_SIZE, 1), dtype=np.single)
    # отдаем свой кусочек
    comm.Gather(part_a, res, root=0)

    # в любом случае возвращаем то, что в нулевом
    return comm.bcast(res, root=0).T[0]


def main():
    global x

    old_crit = 0
    i = 0
    while True:
        i += 1
        y = mult_matrix_by_vector(a, x) - b
        ay = mult_matrix_by_vector(a, y)
        # y = a@x-b
        # ay = a@y
        flag = False
        if rank == 0:
            crit = norm(y)/norm(b)
            if norm(y)/norm(b) < epsilon or crit == old_crit:
                flag = True
            else:
                old_crit = crit
                tao = (y.dot(ay)) / (ay.dot(ay))
                # print('tao:\n', tao)
                x = x - tao*y
            # print(i, 'tao', tao, 'crit', norm(y)/norm(b), epsilon)

        if comm.bcast(flag, root=0):
            break

        # во все потоки закилываем новый x
        x = comm.bcast(x, root=0)


if __name__ == '__main__':
    t = time.time()
    if rank == 0:
        print('go', MATRIX_SPLIT)
    main()
    if rank == 0:
        print(MATRIX_SPLIT, time.time() - t)
