from ioos_qc import qartod

# QARTOD FLAGS:
# 1 = pass
# 2 = test not run on this data 
# 3 = suspect
# 4 = fail 
# 9 = missing data

results_gr = qartod.gross_range_test(
    inp = [10.3, 68.1, 4.4, 71.9, 45.2, 12.5, 0.0, 100.0, 50.0, 5.0],
    fail_span = [0, 100],
    suspect_span = [15, 45]
)

print(results_gr)