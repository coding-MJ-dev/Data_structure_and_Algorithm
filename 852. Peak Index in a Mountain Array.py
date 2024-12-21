# 852. Peak Index in a Mountain Array

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1
        
        while l <= r:
            m = l + (r - l) //2

            if  (m == 0 or arr[m] > arr[m-1]) and (m == n-1 or arr[m] > arr[m+1]) :
                return m 
            
            elif arr[m] < arr[m+1]:
                l = m + 1
            else:
                r = m - 1
        
        return -1

