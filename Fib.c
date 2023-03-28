#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/** Dynamic Programming method
 *
 * returns the nth Fibonacci number
 */
unsigned long long int dp_fib(int n)
{
    unsigned long long int f[n+1];
    f[0] = 0;
    f[1] = 1;
    /// Loop from 2 to n
    for(unsigned long long int i = 2; i <= n; i++) {
        f[i] = f[i-1] + f[i-2]; /// Equals sum of previous 2
    }
    return f[n];
}

/** Recursive method
 *
 * returns the nth Fibonacci number
 */
unsigned long long int recursive_fib(int n)
{
    if (n<=1) {
        return n;
    } else {
        return recursive_fib(n-1) + recursive_fib(n-2);
    }
}

/** Iterative method
 *
 * returns the nth Fibonacci number
 */
unsigned long long int iterative_fib(int n){
    unsigned long long int a = 0, b = 1, c, i;
    if(n == 0)
        return a;
    if (n == 1)
        return b;
    for (i = 2; i <= n; i++){
        c = a + b;
        a = b;
        b = c;
  }
  return b;
}


void help() {
    printf("./fib.out N [Type] [Print Level]\n");
    printf("\tN is the number of rows in the Fibonacci Sequence, required.\n");
    printf("\t[Type] is either 2 for dynamic programming version, 1 for recursive version, 0 for iterative version.\n");

}

int main(int argc, char* argv[])
{
    if (argc < 2)
    {
        printf("at least two arguments needed!\n");
        help();
        return 1;
    }
    int n = atoi(argv[1]);
    int version = 0;
    if (argc >= 2) {
        version = atoi(argv[2]);
    }
    int print = 0;
    if(argc > 3) {
        print = atoi(argv[3]);
    }
    unsigned long long int result;
    struct timespec begin, end;
    double time_used;
    switch (version) {
        case 1:
            clock_gettime(CLOCK_MONOTONIC_RAW, &begin);
            result = recursive_fib(n);
            clock_gettime(CLOCK_MONOTONIC_RAW, &end);
            time_used = (end.tv_nsec - begin.tv_nsec) / 1000000000.0 +
           (end.tv_sec - begin.tv_sec);
            break;
        case 2:
            clock_gettime(CLOCK_MONOTONIC_RAW, &begin);
            result = dp_fib(n);
            clock_gettime(CLOCK_MONOTONIC_RAW, &end);
            time_used = (end.tv_nsec - begin.tv_nsec) / 1000000000.0 +
           (end.tv_sec - begin.tv_sec);
            break;
        case 0:
            clock_gettime(CLOCK_MONOTONIC_RAW, &begin);
            result = iterative_fib(n);
            clock_gettime(CLOCK_MONOTONIC_RAW, &end);
            time_used = (end.tv_nsec - begin.tv_nsec) / 1000000000.0 +
           (end.tv_sec - begin.tv_sec);
            break;
    }
    int i;
    switch(print){
        case 0: 
            printf("Fibonacci(%d) = %llu\n", n, result);
            printf("Time used: %f\n", time_used);
            break;
        case 1:
            if (version == 0) {
                for (i=1; i<=n; i++) {
                    printf("Fibonacci(%d) = %llu\n", i, result = iterative_fib(i));
                }
                printf("Time used: %f\n", time_used);
                break;
            } else if (version == 1) {
                for (i=1; i<=n; i++) {
                    printf("Fibonacci(%d) = %llu\n", i, result = recursive_fib(i));
                }
                printf("Time used: %f\n", time_used);
                break;
            } else if (version == 2) {
                for (i=1; i<=n; i++) {
                    printf("Fibonacci(%d) = %llu\n", i, result = dp_fib(i));
                }
                printf("Time used: %f\n", time_used);
                break;
            }
    }
    return 0;
}
