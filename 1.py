


def sum_(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError('a and b must be int')

print(sum_(1, 2))

def test_sum_():
    assert sum_(1,2) == 3, "Error message"



test_sum_()