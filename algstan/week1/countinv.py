# We will try to implement a merrge sort algorithm
# and then use the algorithm to also comput the 
# number of inversion in the array

import copy
import sys
def getdata():
    arr = []
    with open("IntegerArray.txt", "r") as f:
        for line in f.readlines():
            arr.append(int(line.strip().split()[0])) 
    return arr

def SortingHelper():
    arr = getdata()
    #print arr, len(arr)
    li = 0 
    hi = len(arr)
    w = countInv(arr,  li, hi-1)
    print "NumInvs", w
    print len(arr)

def countInv(arr, si, ei):
    if( ei <= si):
        return 0
    mid = si + (ei - si)/2
    lcnt = countInv(arr, si, mid)
    rcnt = countInv(arr, mid+1, ei)
    scnt = mergeSplitCount(arr, si, mid, ei)    
    #print si, ei, lcnt, rcnt
    return lcnt + rcnt + scnt

def mergeSplitCount(arr, li, mid,  hi):
    D = copy.copy(arr)
    bi = copy.copy(li)
    ci = copy.copy(mid) + 1
    #print "merging", arr[bi:ci], arr[mid+1:hi+1] , li, mid, hi
    # bi, ci are inclusive, hi is also inclusive
    numsplitInvs = 0
    for i in xrange(li , hi+1):
        #print i, bi, ci, mid, arr[i], D[bi], D[ci]
        if (bi > mid): 
            arr[i] = D[ci]
            ci  += 1
        elif (ci > hi):
            arr[i] = D[bi]
            bi += 1
        elif (D[bi] <= D[ci] ):
            arr[i] = D[bi]
            bi += 1
        else:
            arr[i] = D[ci]
            ci += 1
            numsplitInvs =  (numsplitInvs + (mid - bi + 1)) if (bi <=mid) else numsplitInvs
    return numsplitInvs 
    #print "merged", arr[li:hi+1]

if __name__ == "__main__":
    SortingHelper()
