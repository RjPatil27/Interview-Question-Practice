'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Constraints:
  1 <= nums.length <= 104
  -104 <= nums[i] <= 104
  nums is sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortarr= []
        for i in range(len(nums)):
            num = nums[i] * nums[i]
            sortarr.append(num)
        sortarr.sort()
        return sortarr
