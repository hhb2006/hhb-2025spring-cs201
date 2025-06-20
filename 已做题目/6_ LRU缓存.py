class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        val = self.dic.pop(key, -1)
        if val != -1:
            self.dic[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        self.dic.pop(key, -1)
        self.dic[key] = value
        if len(self.dic) <= self.capacity:
            return
        for k, v in self.dic.items():
            self.dic.pop(k)
            return



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)