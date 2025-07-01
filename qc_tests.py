'''
WORK IN PROGRESS
USING ioos_qc LIBRARY
LESSON: DON'T REINVENT THE WHEEL

QARTOD flags:
1 = pass
2 = not evaluated
3 = suspect
4 = fail
9 = missing data
'''
from ioos_qc import qartod

results = qartod.gross_range_test(
    inp=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    suspect_span=[0, 8],
    fail_span=[0, 10]
)

print(results)



