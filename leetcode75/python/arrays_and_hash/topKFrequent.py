class Solution(object):
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        sHeap = [None] * (len(nums) + 1)
        for num, freq in freqMap.items():
            if sHeap[freq] is None:
                sHeap[freq] = []
            
            sHeap[freq].append(num)

        output = []
        idx = 0
        while(len(output) < k and idx < len(sHeap)):
            itm = sHeap[len(sHeap) - idx - 1]
            if itm is None or len(itm) == 0:
                idx += 1
            else:
                output.append(itm.pop(0))
        
        return output