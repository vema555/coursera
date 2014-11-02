# We will try to implement a merrge sort algorithm
# and then use the algorithm to also comput eht 
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
    msort(arr,  li, hi-1)
    print arr, len(arr)

def msort(arr, si, ei):
    #print "S: ", si, ei
    if( ei <= si):
        return
    mid = si + (ei - si)/2
    msort(arr, si, mid)
    #print si, ei, mid
    #sys.exit()
    msort(arr, mid+1, ei)
    merge(arr, si, mid, ei)    

def merge(arr, li, mid,  hi):
    D = copy.copy(arr)
    bi = copy.copy(li)
    ci = copy.copy(mid) + 1
    #print "merging", arr[bi:ci], arr[mid+1:hi+1] , li, mid, hi
    # bi, ci are inclusive, hi is also inclusive
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
    #print "merged", arr[li:hi+1]

if __name__ == "__main__":
    SortingHelper()