#pivoted.py
import ast

def bin_search(nums,target,left,right):
    
    if left>right:
        return -1

    mid=(left+right)//2
    if nums[mid]==target:
        return mid
    if nums[left] < nums[mid]:
        if nums[left] <= target < nums[mid]:
            return bin_search(nums,target,left,mid-1)
        else:
            return bin_search(nums,target,mid+1,right)
    if nums[mid] < nums[right]:
        if nums[mid] < target <= nums[right]:
            return bin_search(nums,target,mid+1,right)
        else:
            return bin_search(nums,target,left,mid-1)



nums=input("enter nums array: ")
nums=ast.literal_eval(nums)
target=int(input("enter the target: "))

print(bin_search(nums,target,0,len(nums)-1))