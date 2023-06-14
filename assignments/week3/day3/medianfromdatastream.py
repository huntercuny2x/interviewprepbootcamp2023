from heapq import *
# input 7, 8, 9
# 1 2 3 4 5 6 7 8 9 10 11 
# max heap  #min heap 
#[-6,-5,-4,-3,-2,-1]   [7,8,9,10,11,12]
# 3+4 / 2 = 3.5
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

medianFinder = MedianFinder();
medianFinder.addNum(1)   # arr = [1]
medianFinder.addNum(2)   # arr = [1, 2]
medianFinder.findMedian() # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)   # arr[1, 2, 3]
print(medianFinder.findMedian()) # return 2.0
