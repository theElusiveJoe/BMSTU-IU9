import threading
import time
import random
import os

s = []
r = []

maxi = 20

lock = threading.Lock()
lock2 = threading.Lock() 

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
        time.sleep(0.1)
        lock2.acquire()
        if len(s) == 0:
            lock2.release()
            time.sleep(0.1)
            lock.release()
            time.sleep(1)
            continue
        el, s = s[-1], s[:-1]
        print('B вытащил', el)
        r.append(el**2)
        lock2.release()
        time.sleep(0.1)
        lock.release()


def c():
    global s, r
    while True:
        lock2.acquire()
        time.sleep(0.1)
        lock.acquire()
        if len(s) == 0:
            lock.release()
            time.sleep(0.1)
            lock2.release()
            time.sleep(1)
            continue
        el, s = s[-1], s[:-1]
        print('C вытащил', el)
        r.append(el**2)
        lock.release()
        time.sleep(0.1)
        lock2.release()


def d():
    global s, r
    while True:
        lock2.acquire()
        if len(r) == 0:
            lock2.release()
            print('Список R пуст, жду одну секунду')
            time.sleep(1)
            continue
        el, r = r[-1], r[:-1]
        lock2.release()
        
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
