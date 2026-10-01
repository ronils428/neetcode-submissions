class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init empty dictionary
        count = {}

        # set frequency of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # set empty frequency list
        freq = [[] for i in range(len(nums) + 1)]

        # using count as index, append number to list
        for n, c in count.items():
            freq[c].append(n)

        # descend through freq and append k items to result
        res = []
        for i in range(len(freq)-1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res