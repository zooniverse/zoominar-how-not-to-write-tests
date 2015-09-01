class Queue:
    def __init__(self, maxsize):
        self.read_index = 0
        self.write_index = 0
        self.maxsize = maxsize
        self.buffer = [None] * maxsize

    def put(self, item):
        self.buffer[self.write_index] = item
        self.write_index = (self.write_index + 1) % self.maxsize

    def get(self):
        item = self.buffer[self.read_index]
        self.read_index = (self.read_index + 1) % self.maxsize
        return item

    def size(self):
        return (self.write_index - self.read_index) % self.maxsize

    def __str__(self):
        return "Queue<buffer=%s read=%s write=%s>" % (self.buffer, self.read_index, self.write_index)










from hypothesis import given, assume, Settings
from hypothesis.strategies import text, integers
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule

class QueueRules(RuleBasedStateMachine):
    queues = Bundle("QueueStates")

    @rule(target=queues, size=int)
    def initialize(self, size):
        assume(size > 0)
        assume(size < 10)
        return (Queue(size), [])

    @rule(target=queues, state=queues, item=int)
    def add(self, state, item):
        queue, elements = state
        queue.put(item)
        elements.append(item)
        return (queue, elements)

    @rule(target=queues, state=queues)
    def remove(self, state):
        queue, elements = state
        queue.get()
        if len(elements) > 0:
            elements.reverse()
            elements.pop()
            elements.reverse()
        return (queue, elements)

    @rule(state=queues)
    def test_size(self, state):
        queue, elements = state
        assert queue.size() == len(elements)

TestQueues = QueueRules.TestCase
