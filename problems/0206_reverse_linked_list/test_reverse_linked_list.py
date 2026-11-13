import pytest

from common import build_list, list_to_array
from reverse_linked_list import Solution


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_reverse_list(values, expected):
    assert list_to_array(Solution().reverseList(build_list(values))) == expected
