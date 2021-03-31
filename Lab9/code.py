import lab9
import matplotlib.pyplot as plt
import time
import shortest_paths
import numpy as np


def exp1():
    y = []
    approxTimes = []
    accTimes = []
    perfTimes = []
    approxDistances = []
    accDistances = []
    perfDistances = []

    for i in range(1, 50):
        y.append(i)

        G = lab9.create_random_complete_graph(50, 1000)

        time1 = time.time()

        accDist = lab9.total_dist(lab9.bellman_ford(G, list(G.adj.keys())[0]))
        time2 = time.time()
        accTimes.append(time2-time1)
        accDistances.append(accDist)

        time3 = time.time()
        approxDist = lab9.total_dist(lab9.bellman_ford_approx(
            G, list(G.adj.keys())[0], i))
        time4 = time.time()
        approxTimes.append(time4-time3)

        approxDistances.append(approxDist)

        time5 = time.time()
        perfDist = lab9.total_dist(
            lab9.bellman_ford_perfect(G, list(G.adj.keys())[0]))
        time6 = time.time()
        perfDistances.append(perfDist)
        perfTimes.append(time6-time5)

        if (accDist - approxDist != 0):
            print("")
            print(accDist - approxDist)
            print("NO", i)
            print("")
        else:
            print("YES", i)

    plt.plot(y, accTimes, label="Actual Times")
    plt.plot(y, approxTimes, label="Approx. Times")
    plt.plot(y, perfTimes, label="Perf. Times")
    plt.xlabel("k")
    plt.ylabel("Time")
    plt.legend()
    plt.show()

    plt.plot(y, accDistances, label="Actual Distances")
    plt.plot(y, approxDistances, label="Approx. Distances")
    plt.plot(y, perfDistances, label="Perf. Distances")
    plt.xlabel("k")
    plt.ylabel("Distance")
    plt.legend()
    plt.show()

    print(approxDistances)


def exp2():

    G = lab9.create_random_complete_graph(10, 1000)
    # print(all_pairs_dijkstra(G))
    print(shortest_paths.all_pairs_bellman_ford(G))


def exp3():
    xAxis = []
    times = []
    for i in range(1, 30):
        xAxis.append(i)
        print(i)
        G = lab9.create_random_complete_graph(i, 1000)
        time1 = time.time()
        ans = lab9.mystery(G)
        time2 = time.time()
        times.append(time2-time1)

    slope, intercept = np.polyfit(
        np.array(np.log(xAxis)), np.array(np.log(times)), 1)
    print(slope)

    xAxis2 = []

    for i in xAxis:
        print(i)
        xAxis2.append(i**3)

    plt.plot(xAxis, times)
    plt.xlabel("Size of Graph")
    plt.ylabel("Time")
    plt.show()

    plt.loglog(xAxis, times)
    plt.xlabel("Log(Size of Graph(")
    plt.ylabel("Log(Time)")
    plt.show()



