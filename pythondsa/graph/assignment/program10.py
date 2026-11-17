class HashTable:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.count = 0

    def insert_without_resize(self, key):
        index = key % self.capacity
        self.table[index].append(key)
        self.count += 1

    def rehash(self):
        old_items = [key for bucket in self.table for key in bucket]
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.count = 0
        for key in old_items:
            self.insert_without_resize(key)

    def insert(self, key):
        self.insert_without_resize(key)
        if self.count / self.capacity > 0.75:
            self.rehash()

    def display(self):
        print("Capacity:", self.capacity)
        print("Number of keys:", self.count)
        print("Load Factor:", round(self.count / self.capacity, 2))
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket if bucket else "None")

# Main execution
ht = HashTable()
keys = list(map(int, input().split()))
for key in keys:
    ht.insert(key)
ht.display()