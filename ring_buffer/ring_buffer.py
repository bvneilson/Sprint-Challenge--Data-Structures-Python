class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest = 0

    def append(self, item):
        if self.data:
            if len(self.data) == self.capacity:
                self.data.pop(self.oldest)
                self.data.insert(self.oldest, item)
                self.oldest += 1
                if self.oldest == self.capacity:
                    self.oldest = 0
            else:
                self.data.append(item)
        else:
            self.data.append(item)

    def get(self):
        return self.data
