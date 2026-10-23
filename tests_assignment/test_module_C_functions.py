import pytest
from searches.binary_search import binary_search

def test_binary_search_found_middle():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2

def test_binary_search_found_standard():
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, 30) == 2

@pytest.mark.parametrize("target, expected_idx", [
    (10, 0),
    (20, 1),
    (30, 2),
    (40, 3),
    (50, 4),
])
def test_binary_search_all_elements(target, expected_idx):
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, target) == expected_idx