def mergening_sort(alist, n):
    if n > 1:
        #splitting alist -> blist, clist
        
        mid = n // 2
        blist = alist[:mid]
        clist = alist[mid:]

        mergening_sort(blist, mid)
        mergening_sort(clist, n - mid)

        #mergening
        
        i = 0 # How many objects from 1list have already transported to alist
        j = 0 # -||- 2list
        k = 0 
        while i < mid and j < n - mid:
            if blist[i] < clist[j]:
                alist[k] = blist[i]
                i += 1
            else:
                alist[k] = clist[j]
                j += 1
            k += 1
        while i < mid:
            alist[k] = blist[i]
            i += 1
            k += 1
        while j < n - mid:
            alist[k] = clist[j]
            j += 1
            k += 1
a = [1, 100, 52, 566, 2, 6, 1, 55, 3]
mergening_sort(a, len(a))
print(a)
    
