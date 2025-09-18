
def reverse(nums,left,right):
    if left>=right:
        return nums
    nums[left],nums[right]=nums[right],nums[left]
    return reverse(nums,left+1,right-1)


nums=[5,8,5,6,4,27,1,3]
left=0
right=len(nums)-1

print(reverse(nums,left,right))
