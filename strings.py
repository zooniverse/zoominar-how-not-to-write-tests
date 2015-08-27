from hypothesis import given, assume, Settings
from hypothesis.strategies import text

with Settings(max_examples=1000):
    @given(text())
    def test_idempotent(string):
        assert string.upper() == string.upper().upper()

    @given(text())
    def test_up_down(string):
        assert string.upper() == string.lower().upper()