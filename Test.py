import time
from Fibonacci import *
from Time import *

def fibonacci_test():
    fib = Fibonacci()
    # ITERATIF 35
    begin = time.time()
    fib.iteratif_lineair(35)
    end = time.time()
    print("Temps iteratif pour 35 éléments: %d s" % (end - begin))
    # RECURSIF 35
    begin = time.time()
    fib.recursif(35)
    end = time.time()
    print("Temps récursif pour 35 éléments: %d s" % (end - begin))
    # SUPER_ITERATIF 35
    begin = time.time()
    fib.iteratif_super(35)
    end = time.time()
    print("Temps itératif super linéaire pour 35 éléments: %d s" % (end - begin))
    # ITERATIF 100000
    begin = time.time()
    fib.iteratif_lineair(100000)
    end = time.time()
    print("Temps iteratif pour 100000 éléments: %d s" % (end - begin))
    # SUPER_ITERATIF 100000
    begin = time.time()
    fib.iteratif_super(100000)
    end = time.time()
    print("Temps itératif superlinéaire pour 100000 éléments: %d s" % (end - begin))

def tri_test():
    tri = Tri()
    random.seed(10)
    liste_b = random.sample(range(1, 10000), 10000 - 1)
    liste_i = liste_b
    liste_c = liste_b
    # TRI INSERTION
    begin = time.time()
    tri.insertion(liste_i)
    end = time.time()
    print("Temps iteratif pour 10000 éléments [tri_insertion]: %d s" % (end - begin))
    # TRI COMPTAGE
    begin = time.time()
    tri.comptage(liste_c)
    end = time.time()
    print("Temps iteratif tri_comptage: %d s" % (end - begin))
    # TRI BULLE
    begin = time.time()
    tri.bulle(liste_b)
    end = time.time()
    print("Temps iteratif tri_bulle: %d s" % (end - begin))