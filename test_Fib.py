"""

Fibonacci Sequence Diagram-drawing Python Program
Author: Zixi Li
Semester: Spring 2023

"""
import random
import time

import matplotlib.pyplot as plt

import Fib


def test_fib():
    """
        To draw line chart based on N and time used for each N.
    """
    x = []
    y = []
    for i in range(1, 20):
        n = random.randrange(1, 21)
        t1 = time.time()
        Fib.recursiveFib(n)
        t2 = time.time()
        tused = t2 - t1
        print(f"{tused:.10f}")
        print(n)
        y.append(tused)
        x.append(n)
    print("end")
    dict0 = {}
    for key in x:
        for value in y:
            dict0[key] = value
            y.remove(value)
            break
    dict0 = dict(sorted(dict0.items()))

    x1 = []
    y1 = []
    for j in range(1, 10000):
        n = random.randrange(1, 10001)
        t1 = time.time()
        Fib.iterativeFib(n)
        t2 = time.time()
        tused = t2 - t1
        print(f"{tused:.10f}")
        print(n)
        y1.append(tused)
        x1.append(n)
    print("end")
    dict1 = {}
    for key in x1:
        for value in y1:
            dict1[key] = value
            y1.remove(value)
            break
    dict1 = dict(sorted(dict1.items()))

    x2 = []
    y2 = []
    for k in range(1, 10000):
        n = random.randrange(1, 10001)
        t1 = time.time()
        Fib.dpFib(n)
        t2 = time.time()
        tused = t2 - t1
        print(f"{tused:.10f}")
        print(n)
        y2.append(tused)
        x2.append(n)
    print("end")
    dict2 = {}
    for key in x2:
        for value in y2:
            dict2[key] = value
            y2.remove(value)
            break
    dict2 = dict(sorted(dict2.items()))

    plt.plot(dict0.keys(), dict0.values())
    plt.title("Recursion Python")
    plt.xlabel("N")
    plt.ylabel("Time Used")
    plt.show()

    plt.plot(dict1.keys(), dict1.values())
    plt.title("Iteration Python")
    plt.xlabel("N")
    plt.ylabel("Time Used")
    plt.show()

    plt.plot(dict2.keys(), dict2.values())
    plt.title("DP Python")
    plt.xlabel("N")
    plt.ylabel("Time Used")
    plt.show()

    plt.plot(dict1.keys(), dict1.values(), label="Iteration")
    plt.plot(dict2.keys(), dict2.values(), label="DP")
    plt.title("Comparison Python")
    plt.xlabel("N")
    plt.ylabel("Time Used")
    plt.legend()
    plt.show()

def main():
    print(test_fib())


if __name__ == "__main__":
    main()
