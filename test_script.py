import re
import os
import matplotlib.pyplot as plt

"""

Fibonacci Sequence Test Script.
Author: Zixi Li
Semester: Spring 2023

"""

def run_program(n):
    """
        This functions used three libraries to run Fib.c in Python
        and draw line charts accordingly.
        Parameter:
            int: n
    """

    step = 500 # The step can change to reflect different patterns.
    x = []
    y = []
    for i in range(step, n+step, step):
        cmd = ['./fib.out', str(i), "0", '0']  # the arguments needed when running ./fib.out "0" is iterative method.
        result = os.popen(' '.join(cmd)).read()
        result = re.findall(r'[\d\.\d]+', result)
        x.append(result[0])
        y.append(result[2])

    x1 = []
    y1 = []
    for j in range(step, n+step, step):
        cmd = ['./fib.out', str(j), "2", '0'] # the arguments needed when running ./fib.out "2" is DP method.
        result = os.popen(' '.join(cmd)).read()
        result = re.findall(r'[\d\.\d]+', result)
        x1.append(result[0])
        y1.append(result[2])

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, y)
    plt.title("Iteration C")
    plt.xlabel("N")
    plt.ylabel("Time Used")
    plt.show()

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x1, y1)
    plt.title("DP C")
    plt.xlabel("N")
    plt.ylabel("Time Used")
    plt.show()

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, y, label="Iterative C")
    plt.plot(x1, y1, label = "DP C")
    plt.title("Comparison C")
    plt.xlabel("N")
    plt.ylabel("Time Used")
    plt.show()


def main():
    """
        Driver
    """
    print(run_program(20000)) # N can be changed to suit my needs.

if __name__ == "__main__":
    main()



