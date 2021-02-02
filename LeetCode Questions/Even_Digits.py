```
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5

```

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        length = []
        count = 0
        for i in range(0,len(nums)):
            n = str(nums[i])
            length.append(len(n))
            
        for i in range(0,len(length)):
            if(length[i]%2==0):
                count =count+1
        return count
