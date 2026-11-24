def selectionsort(a):
    length = len(a)
    for i in range(length-1):
        minimumpos = i
        for j in range(i,length):
            if a[j] < a[minimumpos]:
                minimumpos = j
        a[i], a[minimumpos] = a[minimumpos], a[i]
    return a

def bubblesort(a):
    swapped = True
    swappedcounter = 0
    while swapped:
        swapped = False
        for i in range(0,len(a)-1-swappedcounter):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        swappedcounter += 1
    return a
print(bubblesort([1,5,7,8,54,2,4]))