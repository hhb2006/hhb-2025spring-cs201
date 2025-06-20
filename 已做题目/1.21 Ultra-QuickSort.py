from bisect import bisect

# 1.自己的朴素办法
def methodA():
    while True:
        n = int(input())
        if n == 0:
            break
        nums = []
        res = 0
        for i in range(n):
            num = int(input())
            p = bisect(nums, num)
            res += i - p
            nums.insert(p, num)
        print(res)

# 2.归并排序方法
def methodB():
    def merge(nums, low, medium, high):
        nonlocal cnt
        i, j = low, medium + 1
        tmpl = []
        while i <= medium and j <= high:
            if nums[i] <= nums[j]:
                tmpl.append(nums[i])
                i += 1
            else:
                tmpl.append(nums[j])
                j += 1
                cnt += medium - i + 1
        while i <= medium:
            tmpl.append(nums[i])
            i += 1
        while j <= high:
            tmpl.append(nums[j])
            j += 1
        nums[low:high + 1] = tmpl

    def merge_sort(nums, low, high):
        if low < high:
            medium = (low + high) // 2
            merge_sort(nums, low, medium)
            merge_sort(nums, medium + 1, high)
            merge(nums, low, medium, high)

    while True:
        cnt = 0
        n = int(input())
        if n == 0:
            break
        lis = [int(input()) for _ in range(n)]
        merge_sort(lis, 0, n - 1)
        print(cnt)

methodB()

# http://cs101.openjudge.cn/25dsapre/02299/