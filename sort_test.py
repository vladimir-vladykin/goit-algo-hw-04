import timeit
import random
from sort_functions import all_sort_functions

# how many times we will test each pair of algo and dataset
NUMBER_OF_TEST_ITERATIONS = 5


def main():

    # generate test data
    data_sets = [
        ([random.randint(0, 1_000) for _ in range(10)], "Smallest"),
        ([random.randint(0, 1_000) for _ in range(100)], "Small"),
        ([random.randint(0, 1_000) for _ in range(1_000)], "Big"),
        ([random.randint(0, 10_000) for _ in range(10_000)], "Largest")
    ]

    
    # iteration for each sort function
    # on each step iterate through data sets, and perform testing multiple times
    # for each of them


    print("Perform testing of various sorting algorithms...\n")
    for sort_func, tag in all_sort_functions:
        print(f"Testing {tag} algorithm:")
        for data, data_tag in data_sets:
            average_time = measure_sort_func_exec_time(sort_func, data)
            print(f"Average execution time for {data_tag} is {average_time:.8f}")
        print("\n")


# runs sorting on data muiltiple times, and calculates average,
# to get more precise usual execution time of sort algo
def measure_sort_func_exec_time(func, data):
    all_measurments = []

    for i in range(NUMBER_OF_TEST_ITERATIONS):
        data_copy = data[:]
        start_time = timeit.default_timer()
        func(data_copy)
        execution_time = timeit.default_timer() - start_time
        all_measurments.append(execution_time)

    # calculate average time 
    return sum(all_measurments) / len(all_measurments)

if __name__ == "__main__":
    main()