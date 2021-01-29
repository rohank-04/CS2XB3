import timeit
import random
import math
import time
import matplotlib.pyplot as plt
import numpy as np

# Copy Timer

# Helper function for copy timer eperiment 1
def create_number_list():
    return [random.randint(0,10) for _ in range (0,10)]

# Main function for copy timer experiment 1
def copy_expt_1():
    L = create_number_list()
    X = list(range(1,101))
    A = [None] * 100
    for i in range (0,100):
        start = timeit.default_timer()
        x = L
        y = x.copy()
        end = timeit.default_timer()
        A [i] = end - start
    plt.plot(X,A)
    plt.xlabel("Number of times copied")
    plt.ylabel("Time")
    plt.title("Experiment 1")
    plt.show()

# Main function for copy timer experiment 2
def copy_expt_2():
    L = {'ABC','DEF','GHI','JKL','XYZ'}
    X = list(range(1,101))
    A = [None] * 100
    for i in range (0,100):
        start = timeit.default_timer()
        x = L.copy()
        end = timeit.default_timer()
        A [i] = end - start
    plt.plot(X,A)
    plt.xlabel("Number of times copied")
    plt.ylabel("Time")
    plt.title("Experiment 2")
    plt.show()

# Lookup timer

# Helper function for look up timer  
def create_list():
    return [random.randint(0,1000000) for _ in range (1000000)]

# Main function for loop up timer
def lookup_timer_test():
    L = create_list()
    X = list(range(1,1000001))
    Y = [None] * 1000000
    for i in range (0,1000000):
        start = timeit.default_timer()
        x = L[i]
        end = timeit.default_timer()
        Y[i] =  end -start
    plt.plot(X,Y)
    plt.xlabel("Lookups")
    plt.ylabel("Time")
    plt.title("Lookups vs Time")
    plt.show()

# Append timer

# First experiment for append
def appendExperiment(n):
    runs = []
    times = []
    empty = []
    for i in range(n):
        print(i)
        runs += [i+1]
        start = timeit.default_timer()
        empty.append(0)
        end = timeit.default_timer()
        times += [end-start]
    print(runs)
    print(times)
    plt.plot(runs,times)
    plt.xlabel("Runs")
    plt.ylabel("Time")
    plt.title("Experiment 2")
    plt.show()
    return (runs,times)

# Second experiment for append
def appendExperiment2(n):
    empty = []
    runs = []
    times = []
    for i in range(n):
        empty = [1]
        runs += [i+1]
        appender = [0] * i
        print(i)
        start = timeit.default_timer()
        empty.append(appender)
        end = timeit.default_timer()
        times += [end-start]
    print(runs)
    print(times)
    plt.plot(runs,times)
    plt.xlabel("Runs")
    plt.ylabel("Time")
    plt.title("Time vs Runs")
    plt.show()
    return (runs,times)

# Helper function for append experiment 3
def appendHelper(n):
    empty = []
    appendee = [n] * n
    start = timeit.default_timer()
    empty.append(appendee)
    end = timeit.default_timer()
    appendTime = (end - start)
    empty = []
    start2 = timeit.default_timer()
    empty += appendee
    end2 = timeit.default_timer()
    appendTime2 = (end2 - start2)
    return(appendTime,appendTime2)

# Third experiment for append
def appendExperiment3(n):
    time1 = []
    time2 = []
    ns = []
    for i in range(n):
        times = appendHelper(i)
        time1 += [times[0]]
        time2 += [times[1]]
        ns += [i + 1]
    plt.plot(ns,time1, label=".append()",color="red")
    plt.plot(ns,time2, label="+=[]",color="blue")
    plt.xlabel("Runs")
    plt.ylabel("Time")
    plt.title("Experiment 3")
    plt.show()
