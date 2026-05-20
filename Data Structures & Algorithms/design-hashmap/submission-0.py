class MyHashMap:

    def __init__(self):
        self.my_map = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.my_map)):
            k,v = self.my_map[i]
            if k == key:
                self.my_map[i]=(key,value)
                return
        self.my_map.append((key,value))

    def get(self, key: int) -> int:
        for k,v in self.my_map:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.my_map)):
            k,v = self.my_map[i]
            if k == key:
                self.my_map.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)