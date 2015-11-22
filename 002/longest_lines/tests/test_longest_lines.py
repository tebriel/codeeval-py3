from longest_lines import LongestLines


class TestLongestLines():
    def test_create(self):
        """Creates a Longest Line Object"""
        ll = LongestLines("abc")
        assert(ll is not None)
