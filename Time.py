import time
from Fibonacci import Fibonacci
from Tri import *

def iteratif_lineair_time():
    f, times, iterations = Fibonacci(), [], []
    for i in range(1, 500, 5):
        start = time.time()
        for j in range(0, 10000):
            f.iteratif_lineair(i)
        end = time.time()
        e_time = end-start
        times.append(e_time)
        iterations.append(i)
    return (times, iterations)

def recursif_time():
    f, times, iterations = Fibonacci(), [], []
    for i in range(1, 35):
        begin = time.time()
        f.recursif(i)
        end = time.time()
        e_time = end - begin
        times.append(e_time)
        iterations.append(i)
    return (times, iterations)

def iteratif_super_time():
    f, times, iterations = Fibonacci(), [], []
    for i in range(1, 500, 5):
        begin = time.time()
        for j in range(0, 10000):
            f.iteratif_super(i)
        end = time.time()
        e_time = end - begin
        times.append(e_time)
        iterations.append(i)
    return (times, iterations)

def tri_time():
    time_b = []
    time_i = []
    time_c = []
    nb = 50
    numbers = range(10, 1000, 50)
    tri = Tri()
    for nb in numbers:
        time_e = [0, 0, 0]
        for i in range(1, nb):
            random.seed(i)
            liste_b = random.sample(range(1, nb), (nb - 1))
            liste_i = liste_b
            liste_c = liste_b

            begin_b = time.time()
            tri.bulle(liste_b)
            end_b = time.time()
            time_e[0] = time_e[0] + (end_b - begin_b)

            begin_i = time.time()
            tri.insertion(liste_i)
            end_i = time.time()
            time_e[1] = time_e[1] + (end_i - begin_i)

            begin_c = time.time()
            tri.comptage(liste_c)
            end_c = time.time()
            time_e[2] = time_e[2] + (end_c - begin_c)

        time_b.append(time_e[0] / nb)
        time_i.append(time_e[1] / nb)
        time_c.append(time_e[2] / nb)
    return (time_b, time_i, time_c, numbers)