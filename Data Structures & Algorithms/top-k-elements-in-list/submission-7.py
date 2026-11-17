import heapq

class Item:
    def __init__(self, value, count):
        self.value = value
        self.count = count

    def __lt__(self, other):
        return self.count < other.count # heap-min -> max count at the root

    def __str__(self):
        return f"{self.value}, {self.count}"

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums: # O(n)
            if n in d:
                d[n]+=1
            else:
                d[n]=1

        heap = []

        dim = 0
        for n in d: # O(n*log(k))
            heapq.heappush(heap, Item(n, d[n]))
            dim += 1
            if dim > k:
                heapq.heappop(heap)
                dim -=1
                
        return [e.value for e in heap]