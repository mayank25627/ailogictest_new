# Coding Q1 - Search in Rotated Sorted Array

# Problem Statement
# You are given an integer array nums that was originally sorted in strictly ascending order but has been rotated at some unknown pivot index k. For example, [0, 1, 2, 4, 5, 6, 7] rotated at pivot index 4 becomes [4, 5, 6, 7, 0, 1, 2].
# Write a function search(nums, target) that returns the index of target in nums, or -1 if target is not present.
# Your solution must achieve O(log n) time complexity.

# Constraints
# •	1 <= nums.length <= 5000
# •	-10^4 <= nums[i] <= 10^4
# •	All values in nums are unique
# •	nums is guaranteed to have been rotated at least once
# •	-10^4 <= target <= 10^4

# Open Test Cases (Visible to Candidate)
# Input:  nums = [4, 5, 6, 7, 0, 1, 2],  target = 0
# Output: 4
 
# Input:  nums = [4, 5, 6, 7, 0, 1, 2],  target = 3
# Output: -1

# Solution

def searchElem(nums, target):
    l = 0
    r = len(nums) - 1

    while(l <= r):
        mid = (l+r) // 2

        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid-1

    return -1


nums = list(map(int, input().split()))
target = int(input())

print(searchElem(nums,target))
