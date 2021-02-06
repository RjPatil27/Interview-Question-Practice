class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0 
        j = 0
        arr2 = [i for i in arr]

        while i<len(arr):
            if not arr2[j]:
                arr[i] = 0
                i=i+1
                if(i<len(arr)):
                    arr[i]=0
            else:
                arr[i]=arr2[j]
            i = i+1
            j = j+1
