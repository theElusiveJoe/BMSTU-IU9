import threading
import time
import random
import os

s = []
r = []

maxi = 20

lock = threading.Lock()

def a():
    global s
    i = 1
    while i < maxi + 1:
        lock.acquire()
        s.append(i)
        lock.release()
        print('A Добавил' ,i)
        i += 1
        time.sleep(0.3)


def b():
    global s, r
    while True:
        lock.acquire()
        if len(s) == 0:
            lock.release()
            time.sleep(1)
            continue
        el, s = s[-1], s[:-1]
        lock.release()

        print('B вытащил', el)
        lock.acquire()
        if random.choice([True, False]):
            raise RuntimeError()
        r.append(el**2)
        lock.release()


def c():
    global s, r
    while True:
        lock.acquire()
        if len(s) == 0:
            lock.release()
            time.sleep(1)
            continue
        el, s = s[-1], s[:-1]
        lock.release()

        print('C вытащил', el)
        lock.acquire()
        r.append(el**2)
        lock.release()


def d():
    global s, r
    while True:
        lock.acquire()
        if len(r) == 0:
            lock.release()
            print('Список R пуст, жду одну секунду')
            time.sleep(1)
            continue
        el, r = r[-1], r[:-1]
        lock.release()
        
        print('D вытащил', el)
        if el == maxi//3 or el == maxi**2:
            os._exit(0)


ths = [
    threading.Thread(target=a),
    threading.Thread(target=b),
    threading.Thread(target=c),
    threading.Thread(target=d)
]
for t in ths:
    t.start()
for t in ths:
    t.join()
