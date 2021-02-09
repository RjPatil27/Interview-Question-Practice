'''
Chapter Introduction
Problem : Max consecutive Ones

Given a binary array, Find the maximum number of consecutive one's from the binary array.

Input : [1,1,0,1,1,1]
Output : 3

Note :
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for i in range(0,len(nums)):
            #if loop to check nums[i] is zero or not.
            if(nums[i] == 0):
                count = 0
            #else find one's, increase a count by one and return max value between result and count.
            else:
                count = count + 1
                result = max(result,count)
        return result
