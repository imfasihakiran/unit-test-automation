import pytest
from searches.binary_search import binary_search

def test_binary_search_boundary_first_element():
    arr = [10, 20, 30, 40, 50]
    # BVA: First index boundary
    assert binary_search(arr, 10) == 0

def test_binary_search_boundary_last_element():
    arr = [10, 20, 30, 40, 50]
    # BVA: Last index boundary
    assert binary_search(arr, 50) == 4

def test_binary_search_empty_list():
    # ECP: Empty collection edge case
    assert binary_search([], 5) == -1

def test_binary_search_single_element_present():
    # BVA: List with size 1 (target exists)
    assert binary_search([42], 42) == 0

def test_binary_search_single_element_absent():
    # BVA: List with size 1 (target missing)
    assert binary_search([42], 99) == -1

@pytest.mark.parametrize("missing_target", [5, 35, 100])
def test_binary_search_target_not_found(missing_target):
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, missing_target) == -1