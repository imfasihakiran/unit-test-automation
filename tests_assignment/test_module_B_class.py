import pytest
from maths.prime_check import prime_check
from searches.binary_search import binary_search


# ==========================================
# Module 1: Prime Check Boundaries & ECP
# ==========================================

@pytest.mark.module_b
@pytest.mark.boundary
@pytest.mark.order(58)
def test_prime_check_boundary_zero():
    # BVA: Lower bound zero
    assert prime_check(0) is False


@pytest.mark.module_b
@pytest.mark.boundary
@pytest.mark.order(59)
def test_prime_check_boundary_one():
    # BVA: Lower bound one (neither prime nor composite)
    assert prime_check(1) is False


@pytest.mark.module_b
@pytest.mark.boundary
@pytest.mark.order(60)
@pytest.mark.parametrize("invalid_val", [-1, -5, -10, -99])
def test_prime_check_negative_numbers(invalid_val):
    # ECP: Negative numbers equivalence class
    assert prime_check(invalid_val) is False


# ==========================================
# Module 2: Binary Search Boundaries & ECP
# ==========================================

@pytest.mark.module_c
@pytest.mark.boundary
@pytest.mark.order(61)
def test_binary_search_boundary_first_element():
    arr = [10, 20, 30, 40, 50]
    # BVA: First index boundary
    assert binary_search(arr, 10) == 0


@pytest.mark.module_c
@pytest.mark.boundary
@pytest.mark.order(62)
def test_binary_search_boundary_last_element():
    arr = [10, 20, 30, 40, 50]
    # BVA: Last index boundary
    assert binary_search(arr, 50) == 4


@pytest.mark.module_c
@pytest.mark.boundary
@pytest.mark.order(63)
def test_binary_search_empty_list():
    # ECP: Empty collection edge case
    assert binary_search([], 5) == -1


@pytest.mark.module_c
@pytest.mark.boundary
@pytest.mark.order(64)
def test_binary_search_single_element_present():
    # BVA: List with size 1 (target exists)
    assert binary_search([42], 42) == 0


@pytest.mark.module_c
@pytest.mark.boundary
@pytest.mark.order(65)
def test_binary_search_single_element_absent():
    # BVA: List with size 1 (target missing)
    assert binary_search([42], 99) == -1


@pytest.mark.module_c
@pytest.mark.boundary
@pytest.mark.order(66)
@pytest.mark.parametrize("missing_target", [5, 35, 100])
def test_binary_search_target_not_found(missing_target):
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, missing_target) == -1
