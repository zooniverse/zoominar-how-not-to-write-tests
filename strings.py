from hypothesis import given, assume, Settings
from hypothesis.strategies import text

def test_manually():
    assert "foo".upper() == "FOO"
    assert "123".upper() == "123"
    assert "CamelCase!".upper() == "CAMELCASE!"

# {{{
#@given(text())
#def test_idempotent(string):
    #assert string.upper() == string.upper().upper()
# }}}

# {{{
#@given(text())
#def test_up_down(string):
    #assert string.upper() == string.lower().upper()
# }}}