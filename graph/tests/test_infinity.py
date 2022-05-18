import pytest
import sys
from .._infinity import inf
from operator import add, lt, gt, le, ge


@pytest.mark.parametrize(
    'op, digit, expected',
    (
        (add, sys.maxsize, inf),
        (lt, 0, False),
        (le, sys.maxsize, False),
        (gt, sys.maxsize, True),
        (ge, 123, True),
    ),
)
def test_infinity(op, digit, expected):
    assert op(inf, digit) == expected
