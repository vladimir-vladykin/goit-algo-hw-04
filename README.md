# goit-algo-hw-04
Algo homework 04
Comparasion of some sort algorithms

## Files:
1. sort_test.py -> code for testing sort algorithms performance
2. sort_functions.py -> implementation of sort functions


## Raw measurements:
Tested on M3 pro. 
For each combination of sort algo and dataset we did 5 test and calculated average execution time.

    Testing Insert sort algorithm:
    Average execution time for Smallest is 0.00000231
    Average execution time for Small is 0.00018992
    Average execution time for Big is 0.01526534
    Average execution time for Largest is 1.50779254


    Testing Merge sort algorithm:
    Average execution time for Smallest is 0.00003176
    Average execution time for Small is 0.00011904
    Average execution time for Big is 0.00129679
    Average execution time for Largest is 0.01727544


    Testing Timsort algorithm:
    Average execution time for Smallest is 0.00000061
    Average execution time for Small is 0.00000391
    Average execution time for Big is 0.00004224
    Average execution time for Largest is 0.00063833

## Results:
Insert sort is not bad for small numbers. Actually, for the smallest data set it even slighly faster than Merge sort.
But it very quickly degrade as amount of data grows, which is actually expected since it has O(n^2) complexity.
So usage of this algo is limited to some cases.

Merge sort is quite good, it fast enough for every size of dataset, and it slows down not so fast as Insert sort.
It proves that algo has O(n⋅log n) complexity, which is OK, and algo can be used for most cases.

However, built-in Timsort still the fastest, it beats every other algorithm on every dataset.
It has O(n+ n log ρ) complexity, plus it's probably have the most optimal implementation under-the-hood,
so it's usually the best choise for almost every situation.