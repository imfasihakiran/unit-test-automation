import pytest

from data_structures.stacks.stack import (
    Stack,
    StackOverflowError,
    StackUnderflowError,
)


@pytest.mark.module_a
@pytest.mark.unit
@pytest.mark.order(1)
def test_lifo_order():
    s = Stack(5)
    for i in [1, 2, 3]:
        s.push(i)
    assert [s.pop(), s.pop(), s.pop()] == [3, 2, 1]


@pytest.mark.module_a
@pytest.mark.boundary
@pytest.mark.order(2)
def test_fill_and_drain_cycle():
    s = Stack(3)
    for i in range(3):
        s.push(i)
    assert s.is_full()
    for _ in range(3):
        s.pop()
    assert s.is_empty()


@pytest.mark.module_a
@pytest.mark.unit
@pytest.mark.order(3)
def test_bool_conversion():
    s = Stack(2)
    assert bool(s) is False
    s.push(1)
    assert bool(s) is True


@pytest.mark.module_a
@pytest.mark.unit
@pytest.mark.order(4)
def test_str_representation():
    s = Stack(3)
    assert str(s) == "[]"
    s.push(1)
    s.push(2)
    assert str(s) == "[1, 2]"


@pytest.mark.module_a
@pytest.mark.boundary
@pytest.mark.order(5)
def test_default_limit_is_ten():
    s = Stack()
    for i in range(10):
        s.push(i)
    with pytest.raises(StackOverflowError):
        s.push(10)


@pytest.mark.module_a
@pytest.mark.unit
@pytest.mark.order(6)
def test_interleaved_push_pop_peek():
    s = Stack(3)
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    s.push(3)
    assert s.peek() == 3
    assert s.size() == 2


@pytest.mark.module_a
@pytest.mark.boundary
@pytest.mark.order(7)
def test_state_intact_after_overflow():
    s = Stack(2)
    s.push(1)
    s.push(2)
    with pytest.raises(StackOverflowError):
        s.push(3)
    assert str(s) == "[1, 2]"


@pytest.mark.module_a
@pytest.mark.boundary
@pytest.mark.order(8)
def test_state_intact_after_underflow():
    s = Stack(2)
    with pytest.raises(StackUnderflowError):
        s.pop()
    assert s.is_empty()


@pytest.mark.module_a
@pytest.mark.unit
@pytest.mark.order(9)
def test_exceptions_inherit_base_exception_only():
    assert issubclass(StackOverflowError, BaseException)
    assert not issubclass(StackOverflowError, Exception)
    assert issubclass(StackUnderflowError, BaseException)
    assert not issubclass(StackUnderflowError, Exception)
