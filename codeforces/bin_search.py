#bin_search.py
import ast

def bin_search(counts,left,right):
    mid=(left+right)//2
    print(left,mid,right)
    if left==right:
        return left
    else:
        if (mid+1 <= len(counts)-1 and mid-1 >= 0):
            if counts[mid-1] < counts[mid] > counts[mid+1]:
                return mid
            elif counts[mid-1] <= counts[mid] < counts[mid+1]:
                return bin_search(counts,mid+1,right)
            elif counts[mid-1] > counts[mid] >= counts[mid+1]:
                return bin_search(counts,left,mid-1)
        else:
            if mid+1 > len(counts)-1:
                if counts[mid] > counts[mid-1]:
                    return mid
                else:
                    return mid-1
            if mid-1 < 0:
                if counts[mid] > counts[mid+1]:
                    return mid
                else:
                    return mid-1

counts=input("enter the array: ")
counts=ast.literal_eval(counts)

print(bin_search(counts,0,len(counts)-1))