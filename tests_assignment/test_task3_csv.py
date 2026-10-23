import csv
from pathlib import Path

import pytest

from data_structures.stacks.stack import (
    Stack,
    StackOverflowError,
    StackUnderflowError,
)

CSV_FILE = Path(__file__).parent / "data" / "stack_test_data.csv"


def load_rows():
    with open(CSV_FILE, newline="") as f:
        return [
            (r["test_id"], int(r["limit"]), r["pushes"], r["operation"], r["expected"])
            for r in csv.DictReader(f)
        ]


@pytest.mark.parametrize("test_id,limit,pushes,operation,expected", load_rows())
def test_stack_from_csv(test_id, limit, pushes, operation, expected):
    s = Stack(limit)
    items = [int(x) for x in pushes.split(";")] if pushes else []

    # push_overflow: fill the stack, the last push must fail
    if operation == "push_overflow":
        with pytest.raises(StackOverflowError):
            for item in items:
                s.push(item)
        return

    for item in items:
        s.push(item)

    if expected == "UNDERFLOW":
        with pytest.raises(StackUnderflowError):
            getattr(s, operation)()
        return

    result = getattr(s, operation)()
    assert str(result) == expected, f"{test_id} failed"