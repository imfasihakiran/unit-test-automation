import pytest

from data_structures.stacks.stack import (
    Stack,
    StackOverflowError,
    StackUnderflowError,
)


def make_stack(limit, items=()):
    s = Stack(limit)
    for item in items:
        s.push(item)
    return s


# ---------------- push ----------------
def test_push_single_item_on_empty_stack():
    s = Stack(3)
    s.push(1)
    assert s.stack == [1]


def test_push_limit_minus_one_not_full():  # BVA: limit-1
    s = make_stack(3, [1, 2])
    assert s.size() == 2
    assert not s.is_full()


def test_push_exactly_to_limit():  # BVA: limit
    s = make_stack(3, [1, 2, 3])
    assert s.size() == 3
    assert s.is_full()


def test_push_beyond_limit_raises():  # BVA: limit+1
    s = make_stack(3, [1, 2, 3])
    with pytest.raises(StackOverflowError):
        s.push(4)


def test_push_limit_one_second_item_raises():
    s = make_stack(1, [1])
    with pytest.raises(StackOverflowError):
        s.push(2)


def test_push_zero_limit_raises():
    with pytest.raises(StackOverflowError):
        Stack(0).push(1)


@pytest.mark.parametrize("value", [1, "a", None, 3.5, [1, 2], (1, 2)])
def test_push_accepts_any_type(value):
    s = Stack(2)
    s.push(value)
    assert s.peek() == value


# ---------------- pop ----------------
def test_pop_returns_last_pushed():
    s = make_stack(5, [1, 2, 3])
    assert s.pop() == 3


def test_pop_reduces_size():
    s = make_stack(5, [1, 2, 3])
    s.pop()
    assert s.size() == 2


def test_pop_empty_raises():
    with pytest.raises(StackUnderflowError):
        Stack().pop()


def test_pop_single_item_makes_stack_empty():  # BVA: 1 item
    s = make_stack(5, [7])
    assert s.pop() == 7
    assert s.is_empty()


def test_pop_twice_gives_lifo_order():
    s = make_stack(5, ["a", "b"])
    assert [s.pop(), s.pop()] == ["b", "a"]


def test_pop_from_full_allows_push_again():
    s = make_stack(2, [1, 2])
    s.pop()
    s.push(9)
    assert s.peek() == 9


# ---------------- peek ----------------
def test_peek_returns_top():
    assert make_stack(5, [1, 2, 3]).peek() == 3


def test_peek_does_not_remove():
    s = make_stack(5, [1, 2])
    s.peek()
    assert s.size() == 2


def test_peek_empty_raises():
    with pytest.raises(StackUnderflowError):
        Stack().peek()


def test_peek_single_item():
    assert make_stack(5, [42]).peek() == 42


def test_peek_after_pop_shows_previous():
    s = make_stack(5, [1, 2, 3])
    s.pop()
    assert s.peek() == 2


# ---------------- is_empty ----------------
def test_is_empty_new_stack():
    assert Stack().is_empty() is True


def test_is_empty_after_push():
    assert make_stack(3, [1]).is_empty() is False


def test_is_empty_after_push_and_pop():
    s = make_stack(3, [1])
    s.pop()
    assert s.is_empty() is True


def test_is_empty_full_stack():
    assert make_stack(2, [1, 2]).is_empty() is False


def test_is_empty_zero_limit_stack():
    assert Stack(0).is_empty() is True


# ---------------- is_full ----------------
def test_is_full_new_stack():
    assert Stack(3).is_full() is False


def test_is_full_limit_minus_one():
    assert make_stack(3, [1, 2]).is_full() is False


def test_is_full_at_limit():
    assert make_stack(3, [1, 2, 3]).is_full() is True


def test_is_full_after_pop_from_full():
    s = make_stack(3, [1, 2, 3])
    s.pop()
    assert s.is_full() is False


def test_is_full_limit_one():
    assert make_stack(1, [1]).is_full() is True


def test_is_full_zero_limit_is_true():
    assert Stack(0).is_full() is True


# ---------------- size ----------------
def test_size_empty():
    assert Stack().size() == 0


@pytest.mark.parametrize("count", [1, 2, 3])
def test_size_after_pushes(count):
    assert make_stack(5, range(count)).size() == count


def test_size_after_pop():
    s = make_stack(5, [1, 2, 3])
    s.pop()
    assert s.size() == 2


def test_size_equals_limit_when_full():
    assert make_stack(4, [1, 2, 3, 4]).size() == 4


def test_size_unchanged_after_failed_push():
    s = make_stack(2, [1, 2])
    with pytest.raises(StackOverflowError):
        s.push(3)
    assert s.size() == 2


# ---------------- __contains__ ----------------
def test_contains_present_item():
    assert 2 in make_stack(5, [1, 2, 3])


def test_contains_absent_item():
    assert 99 not in make_stack(5, [1, 2, 3])


def test_contains_on_empty_stack():
    assert 1 not in Stack()


def test_contains_after_pop_removed():
    s = make_stack(5, [1, 2])
    s.pop()
    assert 2 not in s


def test_contains_duplicate_items():
    assert 5 in make_stack(5, [5, 5])


def test_contains_none_item():
    assert None in make_stack(5, [None])