class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        
        @lru_cache(maxsize = None)
        def is_prime(n):
            if n == 0 or n == 1:
                return False
            if n == 2:
                return True
            for i in range(2, int(n ** .5) + 1):
                if n % i == 0:
                    return False
            return True

        vis = set()
        res = 0
        primes = []
        for r in range(1, len(s) + 1):
            for l in range(r):
                num = int(s[l:r])
                if is_prime(num) and num not in vis:
                    primes.append(num)
                    vis.add(num)
        print(primes, vis)

        primes.sort()
        for _ in range(3):
            if primes:
                res += primes.pop()
            else:
                break
        return res


