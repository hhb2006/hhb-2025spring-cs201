class Heap:
    def __init__(self):
        self.heap = []

    def _shift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _shift_down(self, i):
        while i < len(self.heap):
            left, right = i * 2 + 1, i * 2 + 2
            min_idx = i
            if left < len(self.heap) and self.heap[left] < self.heap[min_idx]:
                min_idx = left
            if right < len(self.heap) and self.heap[right] < self.heap[min_idx]:
                min_idx = right
            if min_idx != i:
                self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
                i = min_idx
            else:
                break

    def push(self, num):
        self.heap.append(num)
        self._shift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        num = self.heap.pop()
        self._shift_down(0)
        return num


def main():
    hp = Heap()
    n = int(input())
    for _ in range(n):
        lis = list(map(int, input().split()))
        if lis[0] == 1:
            hp.push(lis[1])
        elif lis[0] == 2:
            print(hp.pop())


if __name__ == '__main__':
    main()