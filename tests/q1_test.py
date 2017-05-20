import q1


def test_sum_for():
    assert q1.sum_for(range(1, 11)) == 55


def test_sum_while():
    assert q1.sum_while(range(1, 11)) == 55


def test_sum_rev():
    assert q1.sum_rec(range(1, 11)) == 55
