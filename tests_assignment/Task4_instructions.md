# Task 4: Test Suite Execution Instructions

## Prerequisites
Ensure all required testing plugins are installed:
pip install pytest pytest-xdist pytest-order

---

## Running Test Suites & Groups

### 1. Default Run (All Modules)
Run the entire test suite across all modules:
python -m pytest

### 2. Parallel Test Execution
Run test cases concurrently across multiple CPU cores using pytest-xdist:
python -m pytest -n auto

### 3. Running Specific Groups (By Marker)
- **Unit Tests Only:**
  python -m pytest -m unit

- **Boundary & ECP Tests Only:**
  python -m pytest -m boundary

- **Module A (Stack) Tests Only:**
  python -m pytest -m module_a

- **Module B (Prime Check) Tests Only:**
  python -m pytest -m module_b

- **Module C (Binary Search) Tests Only:**
  python -m pytest -m module_c

---

## Test Execution Order & Data-Driven Parameterization
- Execution ordering is enforced globally using `@pytest.mark.order(N)` decorators from `pytest-order` so foundational unit tests execute in a clean sequence.
- Data-driven tests utilize `@pytest.mark.parametrize` to execute test logic across multiple dynamic inputs.
