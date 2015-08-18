from hypothesis import given, assume, Settings
from hypothesis.strategies import text, integers

def Levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]

with Settings(max_examples=1000):
    @given(text())
    def test_distance_between_string_and_itself(string):
        assert Levenshtein(string, string) == 0

    @given(text(), text())
    def test_distance_between_two_strings(a, b):
        assume(a != b)
        assert Levenshtein(a, b) > 0

    @given(text(), text())
    def test_commutative(a, b):
        assume(a != b)
        assert Levenshtein(a, b) == Levenshtein(b, a)

    @given(text(), text())
    def test_concatenation(a, b):
        assert Levenshtein(a, a+b) == len(b)
