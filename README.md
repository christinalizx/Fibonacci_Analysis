# Midterm p1: Report on Analysis of Fibonacci  Series
* **Author**: Zixi Li
* **GitHub**: https://github.com/Spring23-CS5008-BOS-Lionelle/midterm-part-1-fib-series-christinalizx
* **Semester** Spring 2023
* **Languages Used**: c, python

## Overview
This report will focus on the runtime of computing Fibonacci Sequence using different algorithms. Fibonacci Sequence, in which each number is the sum of the two preceding ones[^1]. The first 10 fibonacci numbers are:
```text
1 1 2 3 5 8 13 21 34 55
```
The mathematical formula of Fibonacci Sequence is: 

$$F(n) = F(n-1) + F(n-2)$$

This is a classic recursive formula, therefore, recursion is one of the algorithms that will be discussed in this report. However, as illustrated below, recursion is a very time-consuming method of calculating fibonacci numbers, especially when the number gets really big. 

| Version |  Time Complexity | Space Complexity | 
| :-- | :-- |  :-- |
| Recursive | $O(2^n)$  | $O(n)$  |
| Iterative | $O(n)$ | $O(1)$ |
| Dynamic Programming | $O(n)$ | $O(n)$ |

As can be seen from the mathematical formula, each time the method generates two more recursive calls, resulting in an exponential growth in the number of function calls. As for space complexity, each recursive call adds a new stack frame to the call stack, which takes up memory. The maximum depth of the call stack is n, so the space complexity is proportional to n.

However, as demonstrated above, the iterative and dynamic programming (DP) methods, the runtime is significantly faster. This is when n=1, we set that F(1)=1, therefore, the loop runs only n-1 times, and each iteration takes constant time. As a result, the runtime of the algorithm grows linearly as n gets larger. The space complexity for these two methods are different. Because iterative method only needs to store three variables, the space complexity is $O(1)$, whereas DP method needs to store in the table, which has n+1 entries. Each entry takes up constant space, so the total space complexity is proportional to n.

For the purpose of this report, I chose Python as the second language. Other than being the language I am most familiar with, this language has built-in libraries such as time, matplotlib that can make the measures and diagrams more accurate to reflect the results of the computation.

[^1]: "Fibonacci numbers": https://en.wikipedia.org/wiki/Fibonacci_number


## Empirical Data & Discussion 

For the purpose of analysis, I used comparsion method for iterative and DP program. Because theoretically, the runtime of recursion is significantly higher than these two, hence it will be discussed separately.

I developed [test_script.py] to run my C program and draw diagrams accordingly, [test_Fib.py] is used to run my python program and draw line charts.

According to the empirical data, recursive method indeed runs slower than iterative and DP methods.

It is worth mentioning that when n gets to 94, due to the overflow issue, all the C programs started to generate wrong numbers. However, since it is a display issue, the calculation is still correct, I continued using the programs to compute data for this analysis.

### Recursive Method

![Recursive_C]

As can be seen from this chart and also the data in the [workbook], it takes almost 100 seconds for the program to compute the 50th Fibonacci number. The runtime is exponentially incremented.

![Recursive_P]

It seems like the runtime is significantly faster when using python. But, when the time gets bigger, the growth rate gets faster.

![Recursive_P_40]

Within 10 numbers, the scale of Y-axis rockets from 0.16 to 30. I tried to run it to the 50th Fibonacci number, but estimately it takes more than 10 minutes, and my equipment does not function well after the calculation gets too complicated, therefore I cut the program, hence the chart does not display the data to the 50th number.

It proves that when the number is lower, the difference between the runtime of C and python are not significant. However, when it comes to larger number, it is clear that C runs faster than python.

### Iterative and DP Methods

Since the runtime fastened using iterative and DP methods, it is possible to assess the data from a larger scale of number.

![IterationP]
![IterativeC1]

This diagram records the runtime of Iterative method in C every single N from 1 to 10000.

![IterationC]
This diagram records the runtime every 500 numbers.

As can be seen from the line charts, both languages show fluctuations in the iteration method's runtime as n gets larger.

![DP_P]
![DP_C1]
Note the diagram above runs all the N from 1 to 10000, we cannot see the scale clearly from the diagram, but it is illustrative of how the runtime fluctuates as N gets bigger.

![DP_C]
This is recorded every 200.

However, when it comes to comparison, hypothetically, because of the space complexity, iteration method can run faster than DP in certain cases because less it does not require as much space as DP approach.

![ComparisonP]

![ComparisonC]

The line charts here illustrates although DP and Iterative methods both follow the same shaking pattern, Iterative method runs faster than DP. Nevertheless, in Python, it seems like the iterative method fluctuate more than DP.

In conclusion, generally speaking, from the diplay of the above graphs, the iterative method runs faster than DP than recursive method.

### Between Two Languages

| n | Iterative C | Dynamic Programming  C | Iterative P | Dynamic Programming  P |
|--|:--:|:--:|:--:|:--:|
|5000|0.000017|0.000036|0.00935|0,01968|
|10000|0.000049|0.000090|0.00510|0.01048|
|15000|0.000048|0.00110|0.00935|0.01968|
|20000|0.000064|0.00121|0.01330|0.03092|
|25000|0.000080|0.00160|0.01973|0.03796|

Evidently from this table, C runs faster than python, and in both languages, iterative method works faster than DP method. It is worth noticing that when n gets larger, the difference in time gets smaller, this indicates that python may have a better scalability than C here. 


## Language Analysis

For this part of the discussion, I wrote the following codes:
- [Fib.c]: This is the main C file.

- [Fib.py]: This is the main python file.

- The rest of the codes in the repository are helper files used to draw graph or display the calculation results of the above two.

I started coding by developing C program first, as C is a more fundamental language, if I am able to comprehend how to compute Fibonacci Sequence in C well, then python should be easier for me.

Later as I finished developing both programs, I used both programs to as a mirror for each other to see if the calculations went wrong. Then I discovered that C has an overflow issue. However, after some research done, I found that it is only related to display, not the calculation, and solving this issue would be too hard for me now[^2]. Hence, I continued the program running to obtain data for this report without modify the code to correct the display.

[^2]: "Type declaration problem in C (fibonacci numbers)": https://stackoverflow.com/questions/68083581/type-declaration-problem-in-c-fibonacci-numbers


### Language 1: C

I started with the recursive method because it is the most straightforward method looking from the mathmetical formula.

We know that the 0th Fibonacci number is 0, the first is 1. Hence, the pseudocode would be:

```text
recursive_fib(n):

    n0 = 0

    n1 = 1

    return recursive_fib(n) = recursive_fib(n-1) + recursive_fib(n-2)
```
With this logic in mind, I wrote:

```c
unsigned long long int recursive_fib(int n)
{
    if (n<=1) {
        return n;
    } else {
        return recursive_fib(n-1) + recursive_fib(n-2);
    }
}
```
I initially started with:
```c
int recursive_fib(int n)
```
Then, I discovered that when the computation went above 46th Fibonacci number, the program starts to display the wrong number. I thoroughoutly tested and checked my method, I did think it is the method's fault. I did some research, the "int" is usually 32 bits wide, therefore, the largest integer I can get with data type int is 2147483647, which is $2^{31} - 1$. If I use the data type unsigned long int, the maximum I can reach is $2^{32} - 1$, which is below the 48th Fibonacci number[^3]. As a result, I changed the data type to unsigned long long int, that is 64 bits wide.

Next, when the index is not greater than 1, it is apparent in the pseudocode that the nth n has the same value with n. Therefore, I used an if-statement to assigned values to n0 and n1.

When it comes to DP method:
```c
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
```
The logic is developed from the recursive method, the difference is that this is done more iteratively rather than recursively. This is more commonly known as tabulation. Normally it is a bottom-up approach, but it can be conducted top-down. Developing bottom-up here seems more troublesome here, therefore I did not implement that. Because the data is stored in the list, the program ends up looking for every data stored within. However, since the underlying logic is the same with the recursive method, it would work out the correct result as well by developing it like:

```c
unsigned long long int dp_fib(int n) {
  if (f[n] < 0) {
    if (n==0) {
      f[n] = 0;
    }
    else if (n == 1) {
      f[n] = 1;
    }
    else {
      f[n] = dp_fib(n-1) + dp_fib(n-2);
    }
  }
  return f[n];
}
```

I ended up using the tabulation approach as I did not want to call the function recursively again. Theoretically, tabulation can be more efficient as it avoids the overhead of recursive function calls and the associated call stack.

The real "abnormal" one is the actual iterative method. The iterative method works by starting with the first two numbers in the sequence (0 and 1), and then repeatedly adding the previous two numbers to generate the next number in the sequence. In each iteration, the new value will be calculated by adding the current and previous number. Then, update the previous number's value to be the number current to now. It is actually not "abnormal" as the underlying logic is still adding the preceding two numbers to get the new one.

```c
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
```
The method is iterated n-1 times. 


[^3]: "Fibonacci number generator breaks for N>47": https://stackoverflow.com/questions/60018812/fibonacci-number-generator-breaks-for-n47

### Language 2: PYTHON
I chose python as the second language here not only because it is the language that I am most familiar with, also because there are a lot of libraries I can import to help my collection of data and diagram drawing. Especially I can actually write a script to run my C program using python.

Same as C, because the recursive method is more straightforward, I developed the recursive method first.

```python
def recursiveFib(n):
    if n <= 1:
        return n
    return recursiveFib(n - 1) + recursiveFib(n - 2)
```

Similarly, the difference between recursive and DP methods is DP method requires putting the previous results into a list.

```python
def dpFib(n):
    a = [0, 1]
    for i in range(2, n + 1):
        a.append(a[i - 1] + a[i - 2])
    return a[n]
```

I started by putting 0 and 1 into the list called "a". It is clear that 0 is the first element of the list, while 1 is the second. Therefore, we are starting from the third element, that is when the index number equals 2.
Note that since in python, the range does not include the number we indicate after the comma, therefore, if we want the program works out the nth number, the range needs to be till n+1.

After developing iterative method in C, despite successfully get the program to run, I found that using letters like abc to name the variable is easy to get lost for me. Therefore, when writing iterative method in python, I named the variable with clearer identification of them.

```python
def iterativeFib(n):
    previous = 0
    current = 1
    for i in range(n):
        new = previous + current
        previous = current
        current = new
    return previous
```

To test and print numbers from my python program, I developed two separate files to achieve different purposes, as I am afraid printing would interfere with the runtime of the function. [fib_helper.py] is used to print either Nth number alone or from the first to Nth number upon user's choice. Also it can execute without printing anything. [test_Fib.py], as mentioned above, imported matplotlib to plot the line charts for me. I used for-loop to work out all the Fibonacci number from 1st to nth, therefore, the diagram can reflect the runtime pattern more accurately. 

[test_script.py] is the program I developed separately to run my C program. The majority of my time in developing this project was spent on learning and writing this program. I imported os and used os.system() at the beginning, then I discovered that os.system() only runs the C program nth time (n is my input). What I had in mind is the same as [test_Fib.py], that is, using for-loop to calculate and put the results of each iteration into two lists, later draw the diagram using the lists. Then I tried os.popen(), and I picked integers from the printing results by importing the library re, and using re.findall(). As a result, the line charts were drawn as the way I expected.

### Comparison and Discussion Between Experiences

In General, I found using python easier because I did not face a problem of overflow. In fact, python would only face overflow issue if they use C-style fixed-precision integers[^4]. Consequently, I did not have the concern of which data type to use, and I could use my python program to check if my C program gave the correct result.

However, as mentioned above, the C program runs faster than the python program. This is because python is an interpreted language, it needs to be interpreted before it's performance, and these procedures all hapenning during the code's running. While C is a compiled language. This means that the C code is translated before it starts to run[^5]. Nevertheless, as our calculation here does not require a large number, the timing issue here is trivial. But, this result acts as an alert that if one day more complicated calculation is required, then C can be a better choice than python.

In terms of comparsion between methods, although the recursive method is the easiest to develop as it is basically translating the mathematical formula into the programming languages, it is too time consuming as evidently from both Big-O notation and emperical results. Iterative method is faster than DP in both languages. The reason could be the time saved with memory storage. There is a difference between space complexity of two methods. Even if I used tabulation to save some time, the space complexity is still $O(n)$ for DP method, whereas for iterative method, the space complexity is $O(1)$, as it only needs to store three variables.

The exploration I did for this report is limited. If more time is permitted, I may try to program the DP method using bottom-up tabulation, and record the data to compare with top-down tabulation and memoization. Also, despite from the program I computed, the iterative method is faster, hypothetically, when the number grows to a point, it is possible that DP method runs faster than iterative. This is because although the iterative method has a time complexity of O(n), the DP method has a time complexity of O(n) as well but with a lower constant factor. The DP method computes each Fibonacci number once and reuses the computed result for later computations, while the iterative method computes each Fibonacci number from scratch. But since when the number gets too large, I started to face the machine issue, I did not try to work out how large this turning number may be. This is something worth exploring in the future.


[^4]: "Can Integer Operations Overflow in Python?": https://mortada.net/can-integer-operations-overflow-in-python.html
[^5]: "Difference Between C and Python" : https://www.interviewbit.com/blog/difference-between-c-and-python/#:~:text=Q%3A%20Why%20is%20C%20faster,is%20called%20a%20Virtual%20Machine.

## Conclusions / Reflection
In summary, this report has compared the runtime and space complexity of three algorithms for computing the Fibonacci Sequence: recursive, iterative, and dynamic programming. The theoretical time complexity of the recursive method is $O(2^n)$, while the iterative and dynamic programming methods are both $O(n)$. The space complexity of the recursive method is $O(n)$, while the iterative and dynamic programming methods are both $O(1)$ and $O(n)$, respectively.

The empirical data shows that the recursive method has the slowest runtime, while the iterative and dynamic programming methods are significantly faster. The iterative method generally runs faster than the dynamic programming method, especially when space is a concern. 

Furthermore, the comparison between two languages, C and Python, shows that the runtime of the iterative and dynamic programming methods in C is generally faster than in Python. However, the runtime difference decreases as n gets larger, indicating that Python has better scalability under this circumstance.

Overall, the choice of algorithm depends on the specific problem and the resources available. When time is a concern and space is not, the iterative method is the best choice. When space is a concern and the problem can be solved by dynamic programming, it is better to use dynamic programming. If the problem cannot be solved by dynamic programming or the problem size is relatively small, iterative method is the best choice. If the problem is small and simplicity is more important than efficiency, the recursive method may be used.

I learned a lot thoroughout the research for this report. There are a lot of things I did not know about these two languages such as the C can be faster than python in running the same methods. I had to do some research to understand the reason behind it. As the studies proceed, I realized my coding skills were limited. I took a decent amount of time trying to write a C program that could allow me to get the correct number after the 93rd Fibonacci number, but later I realized it would be too time consuming for me. After this project, I would love to take more time to figure out how to get more integers into display in C. Also, I think the scale in the diagrams drawn for iterative and DP methods in C can be improved. Although I know because of the significant fluctuations, it needs more numbers to reflect the change in runtime, I think it can be optimized to show the trend clearer. Moreover, I did not dig into the issue of scalability as it requires more information and data to test, it would be an interesting topic to explore in the future.

## Reference
- "Fibonacci numbers": https://en.wikipedia.org/wiki/Fibonacci_number
- "Big O notation": https://en.wikipedia.org/wiki/Big_O_notation
- "Type declaration problem in C (fibonacci numbers)": https://stackoverflow.com/questions/68083581/type-declaration-problem-in-c-fibonacci-numbers
- "Python matplotlib library documentation": https://matplotlib.org/stable/contents.html
- "Fibonacci number generator breaks for N>47": https://stackoverflow.com/questions/60018812/fibonacci-number-generator-breaks-for-n47
- "Can Integer Operations Overflow in Python?": https://mortada.net/can-integer-operations-overflow-in-python.html
- "Difference Between C and Python" : https://www.interviewbit.com/blog/difference-between-c-and-python/#:~:text=Q%3A%20Why%20is%20C%20faster,is%20called%20a%20Virtual%20Machine.

<!-- auto references -->
[Recursive_C]: RecursiveC.png
[Recursive_P]: RecursionP.png
[Recursive_P_40]: RecursiveP.png
[ComparisonP]: ComparisonP.png
[ComparisonC]: ComparsionC.png
[workbook]: midterm_workbook.xlsx
[DP_C]: DP_C.png
[DP_P]: DP_P.png
[IterationC]: IterativeC.png
[IterationP]: IterationP.png
[Fib.c]: Fib.c
[Fib.py]: Fib.py
[DP_C1]: DP_C1.png
[IterativeC1]: IterativeC1.png
[test_script.py]: test_script.py
[test_Fib.py]: test_Fib.py
[fib_helper.py]: fib_helper.py