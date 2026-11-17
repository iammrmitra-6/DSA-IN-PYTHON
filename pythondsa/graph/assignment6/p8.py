CAP = 2


class Bucket:
    def __init__(self, local_depth):
        self.local_depth = local_depth
        self.keys = []


class ExtendibleHash:
    def __init__(self):
        self.depth = 1
        self.directory = [Bucket(1), Bucket(1)]

    def index(self, key):
        return key & ((1 << self.depth) - 1)

    def insert(self, key):
        while True:
            i = self.index(key)
            bucket = self.directory[i]
            if key in bucket.keys:
                return
            if len(bucket.keys) < CAP:
                bucket.keys.append(key)
                return

            old_depth = bucket.local_depth
            if old_depth == self.depth:
                self.directory.extend(self.directory)
                self.depth += 1

            new_depth = old_depth + 1
            zero_bucket = Bucket(new_depth)
            one_bucket = Bucket(new_depth)
            for directory_index, directory_bucket in enumerate(self.directory):
                if directory_bucket is bucket:
                    if (directory_index >> old_depth) & 1:
                        self.directory[directory_index] = one_bucket
                    else:
                        self.directory[directory_index] = zero_bucket

            for old_key in bucket.keys:
                target = one_bucket if (old_key >> old_depth) & 1 else zero_bucket
                target.keys.append(old_key)

h = ExtendibleHash()
for x in map(int, input().split()):
    h.insert(x)
print("Global depth:", h.depth)
for i, bucket in enumerate(h.directory):
    print(format(i, f"0{h.depth}b"), ":", bucket.keys)