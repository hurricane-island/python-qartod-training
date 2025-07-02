'''
This will be playing around with the ioos_qc library
Lesson: don't reinvent the wheel!!!
'''

from ioos_qc import qartod

results = qartod.gross_range_test(
    inp=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    suspect_span=[0, 8],
    fail_span=[0, 10]
)

print(results)

