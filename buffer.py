class Queue:
    def __init__(self, maxsize):
        self.read_index = 0
        self.write_index = 0
        self.maxsize = maxsize
        self.buffer = [None] * maxsize
        # {{{
        #self.maxsize = maxsize + 1
        #self.buffer = [None] * (maxsize + 1)
        # }}}

    def put(self, item):
        self.buffer[self.write_index] = item
        self.write_index = (self.write_index + 1) % self.maxsize

    def get(self):
        item = self.buffer[self.read_index]
        self.read_index = (self.read_index + 1) % self.maxsize
        return item

    def __len__(self):
        return (self.write_index - self.read_index) % self.maxsize










from hypothesis import given, assume, Settings
from hypothesis.strategies import text, integers
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule

class QueueRules(RuleBasedStateMachine):
    states = Bundle("statestates")

    @rule(target=states, size=int)
    def initialize(self, size):
        assume(size > 0)
        assume(size < 1000)
        return {'queue': Queue(size), 'elements': [], 'size': size}

    @rule(target=states, state=states, item=int)
    def add(self, state, item):
        assume(len(state['elements']) < state['size'])
        state['queue'].put(item)
        state['elements'].append(item)
        return state

    @rule(target=states, state=states)
    def remove(self, state):
        assume(len(state['elements']) > 0)
        retrieved = state['queue'].get()
        state['elements'].reverse()
        expected = state['elements'].pop()
        state['elements'].reverse()
        assert retrieved == expected
        return state

    # {{{
    #@rule(state=states)
    #def test_size(self, state):
        #assert len(state['queue']) == len(state['elements'])
    # }}}

Teststates = QueueRules.TestCase
Teststates.settings.max_examples = 100
Teststates.settings.stateful_step_count = 100
