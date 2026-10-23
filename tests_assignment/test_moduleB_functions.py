import pytest
from maths.prime_check import prime_check
from searches.binary_search import binary_search


# ==========================================
# Module 1: Prime Check Functions (Module B)
# ==========================================

@pytest.mark.module_b
@pytest.mark.boundary
@pytest.mark.order(50)
def test_prime_check_smallest_prime():
    assert prime_check(2) is True


@pytest.mark.module_b
@pytest.mark.unit
@pytest.mark.order(51)
def test_prime_check_small_odd_primes():
    assert prime_check(3) is True
    assert prime_check(5) is True
    assert prime_check(7) is True


@pytest.mark.module_b
@pytest.mark.unit
@pytest.mark.order(52)
def test_prime_check_large_prime():
    assert prime_check(97) is True


@pytest.mark.module_b
@pytest.mark.unit
@pytest.mark.order(53)
def test_prime_check_small_composites():
    assert prime_check(4) is False
    assert prime_check(9) is False


@pytest.mark.module_b
@pytest.mark.unit
@pytest.mark.order(54)
def test_prime_check_large_composite():
    assert prime_check(100) is False


# ==========================================
# Module 2: Binary Search Functions (Module C)
# ==========================================

@pytest.mark.module_c
@pytest.mark.unit
@pytest.mark.order(55)
def test_binary_search_found_middle():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2


@pytest.mark.module_c
@pytest.mark.unit
@pytest.mark.order(56)
def test_binary_search_found_standard():
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, 30) == 2


@pytest.mark.module_c
@pytest.mark.unit
@pytest.mark.order(57)
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
