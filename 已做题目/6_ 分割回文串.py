from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]

        def find_palindrome(string, left, right):
            findings = []
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
                findings.append((left + 1, right))
            return findings

        from collections import defaultdict
        from functools import lru_cache


        heads = defaultdict(list)
        for i in range(len(s)):
            lis1 = find_palindrome(s, i, i)
            for l1, r1 in lis1:
                heads[l1].append((l1, r1))
            if i < len(s) - 1 and s[i] == s[i + 1]:
                lis2 = find_palindrome(s, i, i + 1)
                for l2, r2 in lis2:
                    heads[l2].append((l2, r2))

        @lru_cache(maxsize = None)
        def dfs(head):
            if head == len(s):
                return [[]]
            res = []
            for l, r in heads[head]:
                res.extend([[s[l: r]] + x for x in dfs(r)])
            return res

        return dfs(0)

if __name__ == '__main__':
    print(Solution().partition('aabaa'))