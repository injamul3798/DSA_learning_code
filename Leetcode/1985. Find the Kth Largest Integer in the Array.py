class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        integerList = []
        for num in nums:
            integerList.append(int(num))

        integerList.sort()
        
        findKlargestIndex = len(integerList) - k
        return str(integerList[findKlargestIndex])
    
        # complexity is O(n log n)

       

       # Another Approch using Min Heap better than above one
        def kthLargestNumber(self, nums, k):
            """
            :type nums: List[str]
            :type k: int
            :rtype: str
            """
            integerList = []
            for num in nums:
                integerList.append(int(num))

            minHeap = []
            for val in integerList:
                heappush(minHeap,val)
                if len(minHeap)>k:
                    heappop(minHeap)
            return str(minHeap[0])

        