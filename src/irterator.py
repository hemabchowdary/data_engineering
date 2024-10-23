class CustomerRange:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        result = self.current
        self.current += 1
        return result


for num in CustomerRange(1, 5):
    print(num)

