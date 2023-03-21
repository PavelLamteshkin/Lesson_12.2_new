from utils import arrs
import pytest


@pytest.mark.parametrize("array, index, default, exp_result", [([1, 2, 3], 1, "test", 2),
                                                       ([], 0, "test", "test")
                                                   ])
def test_get(array, index, default, exp_result):
    assert arrs.get(array, index, default) == exp_result


@pytest.mark.parametrize("array, start, end, exp_result", [([1, 2, 3, 4], 1, 3, [2, 3]),
                                                               ([1, 2, 3], 1, None, [2, 3]),
                                                           ([], None, None, []),
                                                           ([1, 2, 3], -2, None, [2, 3]),
                                                           ([1, 2, 3,], -4, None, [1, 2, 3])
                                                           ])
def test_slice(array, start, end, exp_result):
    assert arrs.my_slice(array, start, end) == exp_result

