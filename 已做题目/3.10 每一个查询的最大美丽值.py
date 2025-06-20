class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        import bisect 


        dic = dict()
        for p, b in items:
            dic[p] = max(dic.get(p, 0), b)
        pre_max = 0
        keys = sorted(dic.keys())
        for k in keys:
            pre_max = max(pre_max, dic[k])
            dic[k] = pre_max
        res = []
        for q in queries:
            i = bisect.bisect(keys, q)
            if i == 0:
                res.append(0)
            else:
                res.append(dic[keys[i-1]])
        return res