from hypothesis import given, assume, Settings
from hypothesis.strategies import text, integers

class Queue:
    def __init__(self, size):
        self.read_index = 0
        self.write_index = 0
        self.size = size
        self.buffer = [None] * size

    def put(self, item):
        self.buffer[self.write_index] = item
        self.write_index = (self.write_index + 1) % self.size

    def get(self):
        item = self.buffer[self.read_index]
        self.read_index = (self.read_index + 1) % self.size
        return item

    def size(self):
        return (self.write_index - self.output_index) % self.size



