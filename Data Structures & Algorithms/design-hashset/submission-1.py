class MyHashSet:

    def __init__(self):
        self.hash_map = []

    def add(self, key: int) -> None:
        # for i in self.hash_map:
        #     if i == key :
        #         return None
        # self.hash_map.append(key)
        # return None
        if key not in self.hash_map:
            self.hash_map.append(key)

    def remove(self, key: int) -> None:
        # for i in self.hash_map:
        #     if i == key :
        #         self.hash_map.remove(key)
        #         return
        if key in self.hash_map:
            self.hash_map.remove(key)

    def contains(self, key: int) -> bool:
        # for i in self.hash_map:
        #     if i == key :
        #         return True
        # return False
        return key in self.hash_map


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)