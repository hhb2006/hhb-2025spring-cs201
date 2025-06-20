class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        trie = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def combinations(nums):
            if not nums:
                return ['']
            res = []
            lis = combinations(nums[1:])
            for s in trie[nums[0]]:
                res += [s + x for x in lis]
            return res

        if not digits:
            return []
        return combinations(digits)