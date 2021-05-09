import numpy as np

class Fibonacci(object):
    nb = 0

    def __init__(self):
        self.nb += 1

    def iteratif_lineair(self, n):
        a, b = 0, 1
        for i in range(0, n):
            a = a + b
            b = a - b
        return (a)

    def iteratif_super(self, n):
        f = np.array([[0, 1], [1, 1]])
        f_0 = np.array([[0], [1]])
        result = np.array([[0], [0]])
        if (n == 1):
            result[0][0] = 1
        else:
            result = np.dot(np.linalg.matrix_power(f, n), f_0)
        return (result[0][0])

    def recursif(self, n):
        if (n >= 2):
            return (self.recursif(n - 1) + self.recursif(n - 2))
        else:
            return (n)