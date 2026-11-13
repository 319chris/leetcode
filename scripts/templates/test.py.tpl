import pytest

from {module} import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        # ((input...), expected),
    ],
)
def test_solution(args, expected):
    assert Solution().solve(*args) == expected
