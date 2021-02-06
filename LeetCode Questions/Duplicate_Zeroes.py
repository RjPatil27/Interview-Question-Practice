'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example :
        Input: [1,0,2,3,0,4,5,0]
        Output: null
        Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
'''


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0 
        j = 0
        #Duplicate main array into another array so that we can avoid out of index array error
        arr2 = [i for i in arr]
        
        #use while loop becasue iterations are unkown.
        while i<len(arr):
            #if condition to check whether first element in copied array is 0 or not. 
            #if its 0 then we can make output as [0,0] using below code
            if not arr2[j]:
                arr[i] = 0
                i=i+1
                if(i<len(arr)):
                    arr[i]=0
            #else condition is for all the other elements except 0.
            else:
                arr[i]=arr2[j]
            #increamenting index so that we can add all other element into the array and last elements gets poped out.
            i = i+1
            j = j+1
