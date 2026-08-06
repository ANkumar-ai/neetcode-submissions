from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        # for every ele if that ele-another ele which can be yielded by k-that ele exists ctr=1 

        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        count = 0
        currsum = 0

        for num in nums:
            currsum += num

            if currsum - k in prefix_count:
                count += prefix_count[currsum - k]

            prefix_count[currsum] += 1

        return count