import pandas
import numpy as np
from functools import partial

def get_data2(sval=10, N=20, rng=1000):
    np.random.seed(sval)
    return np.random.randint(0, rng, N)

def getdata():
    arr = []
    with open("../datasets/wk2/QuickSort.txt", "r") as f:
        for line in f.readlines():
            arr.append(int(line.strip().split()[0])) 
    return arr

 
def swap(arr, i, j):
    x = arr[j]
    arr[j] = arr[i]
    arr[i] = x

def get_median(arr, l, N):
    if (N -l == 2):
        mididx = l if (arr[l] <= arr[l +1]) else (l+1)
        return mididx
    elif (N-l == 1):
        return l

    first =  arr[l]
    last = arr[N-1]
    mididx = l + (N -l)/2
    mid = arr[mididx]
    avec  = [first, mid, last]
    aidx = np.argsort(avec)[1]
    xdict = {0:l, 1: mididx, 2:(N-1)}
    #print "Median"
    return xdict[aidx]

    mid = arr[mididx]
    print l, N, mididx
    if (first <=   mid <= last):
        return mididx
    elif (mid <= first <= last):
        return l
    elif (first <=   last <= mid):
        return N-1
    else:
        print "Nonvals", first, mid, last

def partition(ptype, arr, l, N):
    """ 
    pivot = arr[i]
    i+1 
    """
    if ptype == "FIRST":
        pass    
    elif ptype == "LAST":
        swap(arr, l, N-1) 
    
    elif ptype == "MEDIAN":
        #print "BF", l, N, len(arr[l:N])
        mididx = get_median(arr, l, N)
        if mididx != l:
            #print l, mididx, N, len(arr[l:N])
            swap(arr, l, mididx)
    pivot = arr[l]
    i = l + 1

    for j in xrange(l+1, N):
        if( arr[j] < pivot):
            swap(arr, i, j)
            i += 1
    swap(arr, l, i-1)
    return i-1



def CountCmp_Qsort(partition_func, arr, si, ei):
    """ si in inclusive , ei is exclusive """
    if( ei <= si):
        return 0 
    
    pivotidx  = partition_func(arr, si, ei)
    #print arr[si:ei]
    #print si, ei, pivotidx
    nl = CountCmp_Qsort(partition_func, arr, si, pivotidx)
    nr = CountCmp_Qsort(partition_func, arr, pivotidx+1, ei)
    return (ei -si-1) + nl + nr


def QuickSorter(arr, partition_type = "FIRST"):
    sarr = np.copy(arr)
    pfunc = partial(partition, partition_type )
    comparator = partial(CountCmp_Qsort, pfunc) 
    ncomp = comparator(arr, 0,  arr.size)
    print ncomp, np.array_equal(np.sort(sarr), arr)
    return  ncomp

if __name__ == "__main__":
    data = []
    arr = getdata()
    #arr = get_data2(sval=10, N=20, rng=1000):
    fc = QuickSorter(np.copy(arr), "FIRST")
    lc= QuickSorter(np.copy(arr), "LAST")
    mc = QuickSorter(np.copy(arr), "MEDIAN")
    
    # for i in np.arange(100):
    #     arr = get_data(sval=i,  N=10000, rng=100000 )
    #     w = np.copy(arr)
    #     fc = QuickSorter(np.copy(arr), "FIRST")
    #     lc= QuickSorter(np.copy(arr), "LAST")
    #     mc = QuickSorter(np.copy(arr), "MEDIAN")
    #     data.append( (fc, lc, mc)) 

    # pdf = pandas.DataFrame(data, columns =["fc", "lc", "mc"])
    # #print pdf
    # print pdf.mean()