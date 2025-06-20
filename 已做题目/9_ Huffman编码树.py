import heapq


def min_route_sum(nums):
    res = 0
    heapq.heapify(nums)
    while nums:
        num1 = heapq.heappop(nums)
        if not nums:
            return res
        num2 = heapq.heappop(nums)
        res += num1 + num2
        heapq.heappush(nums, num1 + num2)


def main():
    n = int(input())
    lis = list(map(int, input().split()))
    print(min_route_sum(lis))

if __name__ == '__main__':
    main()