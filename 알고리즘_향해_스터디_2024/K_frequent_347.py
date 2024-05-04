from collections import Counter
import heapq

class Solution:

    def topKFrequent(self, nums, k):
        freq_map = Counter(nums)

        min_heap = [(-freq, num) for num, freq in freq_map.items()]
        heapq.heapify(min_heap)

        result = []
        for _ in range(k):
            if min_heap:
                freq, num = heapq.heappop(min_heap)
                result.append(num)
            else:
                break

        return result