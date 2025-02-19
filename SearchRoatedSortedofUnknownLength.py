# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low = 0
        high = 1
        while reader.get(high) <= target:
            low = high
            high = high * 2
        return self.binarySearch(reader, target,low, high)
    
    def binarySearch(self, reader: 'ArrayReader', target: int, low : int,  high: int):
        while low <= high:
            mid = (high + low)//2
            if target == reader.get(mid):
                return mid
            elif target < reader.get(mid):
                high = mid - 1
            else:
                low = mid + 1
        return -1
                
        