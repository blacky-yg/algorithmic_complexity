import matplotlib.pyplot as pyplot
from Fibonacci import *
from Time import *

def complexity_iterative(times, iterations):
    pyplot.figure()
    pyplot.title("Evolution du temps de calcul en fonction du nombre de termes")
    pyplot.plot(iterations, times)
    pyplot.ylabel("Temps pour 10000 calcul")
    pyplot.xlabel("Nombre de termes calculé")
    pyplot.grid()
    pyplot.show()

def complexity_recursive(times, iterations):
    pyplot.figure()
    pyplot.title("Evolution du temps de calcul en fonction du nombre de termes")
    pyplot.plot(iterations, times)
    pyplot.ylabel("Temps pour 1 calcul")
    pyplot.xlabel("Nombre de termes calculé")
    pyplot.grid()
    pyplot.show()

def complexity_iterative_super(times, iterations):
    pyplot.figure()
    pyplot.title("Evolution du temps de calcul en fonction du nombre de termes")
    pyplot.plot(iterations, times)
    pyplot.ylabel("Temps pour 10000 calcul")
    pyplot.xlabel("Nombre de termes calculé")
    pyplot.grid()
    pyplot.show()

def complexity_fib():
    times, iterations = iteratif_lineair_time()
    complexity_iterative(times, iterations)
    times, iterations = recursif_time()
    complexity_recursive(times, iterations)
    times, iterations = iteratif_super_time()
    complexity_iterative_super(times, iterations)

def complexity_tri_insertion(times, numbers):
    pyplot.figure(1)
    pyplot.title("Evolution du temps de tri en fonction de la taille du tableau à trier (tri_insertion")
    pyplot.plot(numbers, times)
    pyplot.ylabel("Temps (s)")
    pyplot.xlabel("Taille du tableau")
    pyplot.grid()
    pyplot.show()

def complexity_tri_bulles(times, numbers):
    pyplot.figure(2)
    pyplot.title("Evolution du temps de tri en fonction de la taille du tableau à trier (tri_bulle)")
    pyplot.plot(numbers, times)
    pyplot.ylabel("Temps (s)")
    pyplot.xlabel("Taille du tableau")
    pyplot.grid()
    pyplot.show()

def complexity_tri_comptage(times, numbers):
    pyplot.figure(3)
    pyplot.title("Evolution du temps de tri en fonction de la taille du tableau à trier (tri_comptage)")
    pyplot.plot(numbers, times)
    pyplot.ylabel("Temps (s)")
    pyplot.xlabel("Taille du tableau")
    pyplot.grid()
    pyplot.show()

def complexity_tri():
    time_b, time_i, time_c, numbers = tri_time()
    complexity_tri_bulles(time_b, numbers)
    complexity_tri_insertion(time_i, numbers)
    complexity_tri_comptage(time_c, numbers)