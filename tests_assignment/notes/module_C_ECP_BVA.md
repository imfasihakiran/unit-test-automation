# Module C - Binary Search (searches/binary_search.py)
Tested by: Danish (24F-3037)

## What I looked at
The binary_search function takes a sorted collection and a target value, returning the 0-based index of the target if present, or -1 if the target is not found in the list.

## ECP (equivalence classes)
binary_search(collection, target)
- valid present target: target is located at the middle, start, or end of a sorted list
- missing target: target is smaller than the minimum element, larger than the maximum element, or falls between existing elements
- edge collections: empty list ([]), single-element list ([item])

## BVA (boundary values)
- list length boundaries: 0 items (empty list), 1 item (single-element list)
- position boundaries: index 0 (first element), index len(arr)-1 (last element)
- missing target boundaries: search value below min element, search value above max element

## Things I noticed while testing
- Passing an empty list ([]) cleanly returns -1 without causing an IndexError.
- Single-element lists ([42]) correctly return index 0 when matched, and -1 when the target is absent.

## Test files
- tests_assignment/module_c_functions.py : tests for standard target positions and parameterized lookups
- tests_assignment/module_c_class.py : tests for first/last index boundaries, empty lists, single elements, and missing targets
Run with: python -m pytest tests_assignment -v