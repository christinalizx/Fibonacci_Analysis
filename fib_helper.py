"""

Fibonacci Sequence Print Python Program
Author: Zixi Li
Semester: Spring 2023

"""
import Fib
import time

def main():
    """
        To print the nth/1 to nth Fibonacci number or execute without print.
    """
    choice = input("0: recursive; 1: iterative; 2: DP; 3: Execute without print\n")
    if int(choice) == 0:
        n = input("Enter your number: \n")
        question = input("0 for only N; 1 for 1 to N\n")
        if int(question) == 0:
            tbegin = time.time()
            recursiveFib(int(n))
            tend = time.time()
            print(f"{recursiveFib(int(n))}")
            print(f"The time used: {tend-tbegin:.10f}")
        if int(question) == 1:
            print("The results are: ")
            t1 = time.time()
            for i in range(1, int(n)+1):
                result = recursiveFib(i)
                print(result)
            t2 = time.time()
            print(f"The time used: {t2-t1:.10f}")
    elif int(choice) == 1:
        n = input("Enter your number: \n")
        question = input("0 for only N; 1 for 1 to N\n")
        if int(question) == 0:
            tbegin = time.time()
            iterativeFib(int(n))
            tend = time.time()
            print(f"{iterativeFib(int(n))}")
            print(f"The time used: {tend - tbegin:.10f}")
        if int(question) == 1:
            print("The results are: ")
            t1 = time.time()
            for i in range(1, int(n) + 1):
                result = iterativeFib(i)
                print(result)
            t2 = time.time()
            print(f"The time used: {t2 - t1:.10f}")
    elif int(choice) == 2:
        n = input("Enter your number: \n")
        question = input("0 for only N; 1 for 1 to N\n")
        if int(question) == 0:
            tbegin = time.time()
            dpFib(int(n))
            tend = time.time()
            print(f"{dpFib(int(n))}")
            print(f"The time used: {tend - tbegin:.10f}")
        if int(question) == 1:
            print("The results are: ")
            t1 = time.time()
            for i in range(1, int(n) + 1):
                result = dpFib(i)
                print(result)
            t2 = time.time()
            print(f"The time used: {t2 - t1:.10f}")

    elif int(choice) == 3:
        n = input("Enter your number: \n")
        recursiveFib(int(n))
        iterativeFib(int(n))
        dpFib(int(n))

if __name__ == "__main__":
    main()