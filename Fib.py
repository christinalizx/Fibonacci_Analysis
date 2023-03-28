"""

Fibonacci Sequence Python Program
Author: Zixi Li
Semester: Spring 2023

"""


def recursiveFib(n):
    """
        Calculates the nth Fibonacci number using recursion.
        Parameter:
            int: n
        Returns:
            The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return recursiveFib(n - 1) + recursiveFib(n - 2)


def iterativeFib(n):
    """
        Calculates the nth Fibonacci number using iteration.
        Parameter:
            int: n
        Returns:
            The nth Fibonacci number.
    """
    previous = 0
    current = 1
    for i in range(n):
        new = previous + current
        previous = current
        current = new
    return previous


def dpFib(n):
    """
        Calculates the nth Fibonacci number using dynamic programming method.
        Parameter:
            int: n
        Returns:
            The nth Fibonacci number.
    """
    a = [0, 1]
    for i in range(2, n + 1):
        a.append(a[i - 1] + a[i - 2])
    return a[n]



