\# Module A - Stack (data\_structures/stacks/stack.py)



Tested by: imfasihakiran



\## What I looked at

The Stack class has a limit (default 10). push() fails when the stack is full, pop() and peek() fail when it is empty. Other methods: is\_empty, is\_full, size, `in` check, bool and str.



\## ECP (equivalence classes)



push(item)

\- valid: stack has space, any type of item

\- invalid: stack already full (StackOverflowError)



pop() and peek()

\- valid: stack has at least 1 item

\- invalid: stack is empty (StackUnderflowError)



is\_empty() / is\_full() / size()

\- stack empty, stack partly filled, stack full



item in stack

\- item is present, item is not present, stack is empty



Stack(limit)

\- valid: limit more than 0 (like 3 or 10)

\- invalid: limit 0 or negative



\## BVA (boundary values), taking limit = 3

\- items in stack: 0, 1, 2 (limit-1), 3 (limit), 4 (limit+1, should fail)

\- pop/peek: on empty stack and on a stack with exactly 1 item

\- limit value: -1, 0, 1

\- default limit: 10 pushes work, the 11th fails



\## Things I noticed while testing

\- The two error classes inherit from BaseException, not Exception.

\- Stack(0) and Stack(-1) are accepted, there is no check on limit.

\- With Stack(0), is\_empty() and is\_full() both return True.



\## Test files

\- tests\_assignment/test\_moduleA\_functions.py : tests for each method

\- tests\_assignment/test\_moduleA\_class.py : tests for the class as a whole



Run with: python -m pytest tests\_assignment -v

