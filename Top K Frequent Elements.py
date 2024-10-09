class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencyMap = {}
        for num in nums:
            if num not in numFrequencyMap: 
                numFrequencyMap[num] = 1
            else: 
                numFrequencyMap[num] += 1

        maxFrequency = max(numFrequencyMap.values())

        frequencyNumMap = {i: [] for i in range(1, maxFrequency + 1)}

        for num in numFrequencyMap:
            frequencyNumMap[numFrequencyMap[num]].append(num)

        result = []
        for frequency in range(maxFrequency, 0, -1):
            if len(result) >= k: 
                break
            if len(frequencyNumMap[frequency]) > 0:
                result += frequencyNumMap[frequency]

        return result
