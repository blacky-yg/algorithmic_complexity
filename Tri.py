import random
import time

class Tri(object):
    def insertion(self, array):
        for i in range(1, len(array)):
            j = i - 1
            tmp = array[i]
            while (tmp < array[j] and j >= 0):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = tmp

    def bulle(self, array):
        length = len(array)
        for i in range(length):
            for j in range(0, length - i - 1):
                if (array[j] > array[j + 1]):
                    array[j], array[j + 1] = array[j + 1], array[j]

    def comptage(self, array):
        length = len(array)
        maxi = max(array)
        result = length * [0]
        container = (maxi + 1) * [0]
        for i in array:
            container[i] += 1
        for i in range(1, maxi + 1):
            container[i] += container[i - 1]
        i = length - 1
        while (i >= 0):
            result[container[array[i]] - 1] = array[i]
            container[array[i]] -= 1
            i -= 1
        return (result)