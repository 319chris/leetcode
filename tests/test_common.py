from common import build_list, build_tree, list_to_array, tree_to_array


def test_linked_list_roundtrip():
    assert list_to_array(build_list([1, 2, 3])) == [1, 2, 3]
    assert build_list([]) is None


def test_tree_roundtrip():
    data = [3, 9, 20, None, None, 15, 7]
    assert tree_to_array(build_tree(data)) == data
    assert build_tree([]) is None
    assert tree_to_array(build_tree([1, None, 2, 3])) == [1, None, 2, 3]
