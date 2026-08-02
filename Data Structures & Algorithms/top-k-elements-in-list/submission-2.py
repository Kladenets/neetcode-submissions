class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        buckets = defaultdict(list)

        for num, freq in freqs.items():
            buckets[freq].append(num)
        
        print(sorted(buckets))
        res = []
        for freq, nums in reversed(sorted(buckets.items())):
            for num in nums:
                if len(res) < k:
                    res.append(num)
        
        return res
        