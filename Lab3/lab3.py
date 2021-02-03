import random
import math
import time

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
            if L[j] >= pivot:
                x = 0
            else:
                i += 1
                L[i],L[j] = L[j],L[i]

        pivotCounter -= 1
        if pivotCounter == -1:
            sorted = True
    return L

L = create_random_list(10)
print(L)
print(quicksort_inplace(L))
            
L = create_random_list(10)

             
def dual_pivot_quicksort(L):

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
        
    
    middleArr = [firstPivot] + middleArr
    lastArr = [secondPivot] + lastArr
    
    if len(firstArr) > 2:
        firstArr = dual_pivot_quicksort(firstArr)
    if len(middleArr) > 2:
        middleArr = [firstPivot] + dual_pivot_quicksort(middleArr[1:])
    if len(lastArr) > 2:
        lastArr = [secondPivot] + dual_pivot_quicksort(lastArr[1:])

    # print("First Pivor",firstPivot)
    # print("Second Pivot",secondPivot)
    # print("First Arr",firstArr)
    # print("Middle Arr",middleArr)
    # print("Last Arr",lastArr)
    finalArr = firstArr + middleArr + lastArr

    return finalArr


print("<__________________________________>")
for i in range(0,50):
    time.sleep(1)

    L = create_random_list(10)
    initialL = L
    Lsorted = dual_pivot_quicksort(L)
    L.sort()
    if L == Lsorted:
        print(True)
    else:
        print("FALSE!!!!")
        print(initialL)
        print(L)
        time.sleep(1)
        print(dual_pivot_quicksort(initialL))
        print(Lsorted)
    
print(dual_pivot_quicksort([2, 2, 2, 3, 4, 5, 6, 6, 9, 10]))
L = [1, 2, 4, 6, 7, 7, 8, 10, 10, 10]
L.sort()
print(L == dual_pivot_quicksort(L))