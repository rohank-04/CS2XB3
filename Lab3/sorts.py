import random
import math

def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


def quicksort_inplace(L):
    if len(L) < 2:
        return L

    pivotCounter = len(L)-1
    sorted = False

    while sorted == False:
        pivot = L[pivotCounter]
        i = -1
        for j in range(len(L)):
            if L[j] < pivot:
                i += 1
                L[i],L[j] = L[j],L[i]

        pivotCounter -= 1
        if pivotCounter == -1:
            sorted = True
    return L
             
def dual_pivot_quicksort(L):

    if len(L) < 2:
        return L

    if L[len(L)-1] < L[0]:
        L[0],L[len(L)-1] = L[len(L)-1],L[0]

    if len(L) < 3:
        return L
    firstPivot = L[0]
    secondPivot = L[len(L)-1]
    firstArr = []
    middleArr = []
    lastArr = []

    for i in range(1,len(L)-1):
        if L[i] < firstPivot:
            firstArr += [L[i]]
        elif L[i] > secondPivot:
            lastArr += [L[i]]
        else:
            middleArr += [L[i]]
        

    return dual_pivot_quicksort(firstArr) + [firstPivot] + dual_pivot_quicksort(middleArr) + [secondPivot] + dual_pivot_quicksort(lastArr)



    

def tri_pivot_quicksort(L):

    if len(L) <= 2:
        return sorted(L)

    pivots = sorted(L[:3])

    firstPivot,secondPivot,thirdPivot = pivots[0],pivots[1],pivots[2]

    L = L[3:]

    firstArr,secondArr,thirdArr,fourthArr = [],[],[],[]

    for item in L:
        if item < firstPivot:
            firstArr += [item]
        elif firstPivot <= item < secondPivot:
            secondArr += [item]
        elif secondPivot <= item < thirdPivot:
            thirdArr += [item]
        else:
            fourthArr += [item]


    return tri_pivot_quicksort(firstArr) + [firstPivot] + tri_pivot_quicksort(secondArr) + [secondPivot] + tri_pivot_quicksort(thirdArr) + [thirdPivot] + tri_pivot_quicksort(fourthArr)


def quad_pivot_quicksort(L):

    if len(L) <= 3:
        return sorted(L)

    pivots = sorted(L[:4])

    firstPivot,secondPivot,thirdPivot,fourthPivot = pivots[0],pivots[1],pivots[2],pivots[3]

    L = L[4:]

    firstArr,secondArr,thirdArr,fourthArr,fifthArr = [],[],[],[],[]

    for item in L:
        if item < firstPivot:
            firstArr += [item]
        elif firstPivot <= item < secondPivot:
            secondArr += [item]
        elif secondPivot <= item < thirdPivot:
            thirdArr += [item]
        elif thirdPivot <= item < fourthPivot:
            fourthArr += [item]
        else:
            fifthArr += [item]


    return quad_pivot_quicksort(firstArr) + [firstPivot] + quad_pivot_quicksort(secondArr) + [secondPivot] + quad_pivot_quicksort(thirdArr) + [thirdPivot] + quad_pivot_quicksort(fourthArr) + [fourthPivot] + quad_pivot_quicksort(fifthArr)

def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(0,n-1):
            if L[j]>L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    return L

def insertion_sort(L):
    n = len(L)
    for i in range(1,n):
        k = L[i]
        j = i - 1
        while j>=0 and k<L[j]:
            L[j+1] = L[j]
            j-=1
        L[j+1]=k
    return L

<<<<<<< HEAD

def worst_case_performance():
    times1 = []
    x = []

    for i in range(1000):
        times1 += [nearSortListsOfSize(i,my_quicksort)]
        x += [i]

    plt.plot(x,times1)
    plt.xlabel("Length of List Sorted")
    plt.ylabel("Worst Case Performance")
    plt.title("Worst Case Experiment")
    plt.show()

worst_case_performance()
=======
def selection_sort(L):
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if L[min_index] > L[j]:
                min_index = j
        L[i],L[min_index] = L[min_index],L[i]
    return L
>>>>>>> c42590ed1d0aff0e0ef6faf9eb035fd4c0ad275e
