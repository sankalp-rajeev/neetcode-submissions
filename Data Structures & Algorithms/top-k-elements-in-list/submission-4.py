class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        def get_freq(x):
            return count[x]
        listNew = sorted(count.keys(),key = get_freq, reverse = True)
        return listNew[:k]
        