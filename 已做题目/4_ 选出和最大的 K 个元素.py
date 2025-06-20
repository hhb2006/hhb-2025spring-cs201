class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        import heapq

        n = len(nums1)
        if n == 1:
            return [0]

        res = [0] * n
        tops = [0] * k
        heapq.heapify(tops)
        addup, mini = 0, 0
        ascent = [(a, b) for a, b in enumerate(nums1)]
        ascent.sort(key = lambda x: x[1])
        ascent = [a[0] for a in ascent]
        nums2 = [nums2[i] for i in ascent]

        for i in range(n-1):
            if nums2[i] > mini:
                addup += nums2[i] - mini
                heapq.heappop(tops)
                heapq.heappush(tops, nums2[i])
                mini = tops[0]
            if nums1[ascent[i + 1]] > nums1[ascent[i]]:
                res[ascent[i + 1]] = addup
            else:
                res[ascent[i + 1]] = res[ascent[i]]

        return res
