import pytest
from splay_tree_map import SplayTreeMap


def test_insert_and_retrieve():
    tree = SplayTreeMap()
    tree[10] = 'ten'
    tree[20] = 'twenty'
    tree[5] = 'five'
    
    assert tree[10] == 'ten'
    assert tree[20] == 'twenty'
    assert tree[5] == 'five'
    
    # Accessing a key should splay it to the root
    assert tree.root().key() == 5

def test_delete():
    tree = SplayTreeMap()
    tree[10] = 'ten'
    tree[20] = 'twenty'
    tree[5] = 'five'
    
    del tree[10]
    
    with pytest.raises(KeyError):
        _ = tree[10]
    
    assert tree[20] == 'twenty'
    assert tree[5] == 'five'

def test_find_min_and_max():
    tree = SplayTreeMap()
    tree[10] = 'ten'
    tree[20] = 'twenty'
    tree[5] = 'five'
    
    assert tree.find_min() == (5, 'five')
    assert tree.find_position(5).key() == 5
    assert tree.find_position(20).key() == 20

def test_splay_property():
    tree = SplayTreeMap()
    tree[10] = 'ten'
    tree[20] = 'twenty'
    tree[5] = 'five'
    
    # Accessing 20 should splay it to the root
    _ = tree[20]
    assert tree.root().key() == 20

    # Accessing 5 should splay it to the root
    _ = tree[5]
    assert tree.root().key() == 5

    # Accessing 10 should splay it to the root
    _ = tree[10]
    assert tree.root().key() == 10

def test_range_search():
    tree = SplayTreeMap()
    tree[10] = 'ten'
    tree[20] = 'twenty'
    tree[5] = 'five'
    tree[15] = 'fifteen'
    tree[25] = 'twenty-five'

    results = list(tree.find_range(10, 25))
    expected = [(10, 'ten'), (15, 'fifteen'), (20, 'twenty')]

    assert results == expected
