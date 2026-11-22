from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_score_pair():
    expected = 10
    actual = Yatzy.score_pair(2, 3, 5, 5, 1)
    assert expected == actual