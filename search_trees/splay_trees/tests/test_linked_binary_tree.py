import pytest


def test_init():
    from linked_binary_tree import LinkedBinaryTree
    tree = LinkedBinaryTree()
    assert len(tree) == 0