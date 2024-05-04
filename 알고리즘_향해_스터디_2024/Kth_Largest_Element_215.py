import heapq

def findKthLargest(nums, k):
    m_heap = []
    
    #  최소힙(최소 값이 우선순위인 큐)으로 정렬이 된다. 
    for num in nums:
        heapq.heappush(m_heap, num)
        
        if len(m_heap) > k:
            heapq.heappop(m_heap)
    
    return heapq.heappop(m_heap)