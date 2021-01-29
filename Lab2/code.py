import matplotlib.pyplot as plt
import numpy as np
import timeit
import time
import random
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

