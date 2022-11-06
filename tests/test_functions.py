import pytest
import copy


def _right(coll, path, value):
    length = len(path)
    last_index = length - 1
    index = 0
    nested = coll

    while index < length:
        key = path[index]
        new_value = value
        if index != last_index:
            obj_value = nested[key] if key in nested else None
            new_value = obj_value if isinstance(obj_value, dict) else {}
        nested[key] = new_value
        nested = nested[key]
        index += 1
    return coll


@pytest.fixture
def coll():
    return {'a': {'b': {'c': 0}}}


def first_test_set_():
    copy_coll = copy.deepcopy(coll)
    _right(copy_coll, ['a', 'b', 'c'], 1)
    print(copy_coll['a']['b']['c'] == 1)
    assert copy_coll['a']['b']['c'] == 1


def second_test_set_():
    copy_coll = copy.deepcopy(coll)
    _right(copy_coll, ['x', 'y', 'z'], 2)
    print(copy_coll['x']['y']['z'] == 2)
    assert copy_coll['x']['y']['z'] == 2


def three_test_set_():
    copy_coll = copy.deepcopy(coll)
    _right(copy_coll, ['a'], 3)
    print(copy_coll['a'] == 3)
    assert copy_coll['a'] == 3


def four_test_set_():
    copy_coll = copy.deepcopy(coll)
    _right(copy_coll, ['a', 'b'], 4)
    print(copy_coll['a']['b'] == 4)
    assert copy_coll['a']['b'] == 4


def five_test_set_():
    copy_coll = copy.deepcopy(coll)
    _right(copy_coll, [], 5)
    print(copy_coll['a']['b']['c'] == 0)
    assert copy_coll['a']['b']['c'] == 0
