import FTA
        
# Test data / Basis events
E01 = FTA.Event(fr=0.23e-09, mttr=12, t_sys=1)
E02 = FTA.Event(fr=0.11e-09, mttr=20, t_sys=1)
E03 = FTA.Event(fr=0.91e-09, mttr=1, t_sys=1)
E04 = FTA.Event(fr=0.55e-09, mttr=2, t_sys=1)
E05 = FTA.Event(fr=0.83, mttr=56, t_sys=1)
E06 = FTA.Event(fr=0.77, mttr=11, t_sys=1)
E07 = FTA.Event(fr=0.12, mttr=96, t_sys=1)
E08 = FTA.Event(fr=0.67, mttr=67, t_sys=1)
E09 = FTA.Event(fr=0.23e-09, mttr=12, t_sys=87600)
E10 = FTA.Event(fr=0.11e-09, mttr=20, t_sys=87600)
E11 = FTA.Event(fr=0.91e-09, mttr=1, t_sys=87600)
E12 = FTA.Event(fr=0.55e-09, mttr=2, t_sys=87600)
E13 = FTA.Event(fr=0.83, mttr=56, t_sys=87600)
E14 = FTA.Event(fr=0.77, mttr=11, t_sys=87600)
E15 = FTA.Event(fr=0.12, mttr=96, t_sys=87600)
E16 = FTA.Event(fr=0.67, mttr=67, t_sys=87600)

# test OR
w, q = FTA.calc_OR(E01, E02, E03, E04)
print(format(q, '.8e'))
assert format(w, '.8e') == "1.80000000e-09"
assert format(q, '.8e') == "1.33601863e-09" # "1.33601866e-09"
w, q = FTA.calc_OR(E05, E06, E07, E08)
assert format(w, '.8e') == "2.32668867e-01"
assert format(q, '.8e') == "9.02649010e-01"
w, q = FTA.calc_OR(E09, E10, E11, E12)
assert format(w, '.8e') == "1.79999999e-09"
assert format(q, '.8e') == "6.96999991e-09" # "6.96999997e-09"
w, q = FTA.calc_OR(E13, E14, E15, E16)
assert format(w, '.8e') == "9.25155692e-06"
assert format(q, '.8e') == "9.99996129e-01"
w, q = FTA.calc_OR(E09, E10, E11)
assert format(w, '.8e') == "1.24999999e-09"
assert format(q, '.8e') == "5.86999993e-09" # "5.86999998e-09"
w, q = FTA.calc_OR(E09, E10)
assert format(w, '.8e') == "3.39999998e-10"
assert format(q, '.8e') == "4.95999997e-09" # "4.95999998e-09"

# test AND
w, q = FTA.calc_AND(E01, E02, E03, E04)
assert format(w, '.8e') == "2.90044143e-38"
assert format(q, '.8e') == "5.89499363e-39"
w, q = FTA.calc_AND(E05, E06, E07, E08)
assert format(w, '.8e') == "4.78127864e-02"
assert format(q, '.8e') == "1.57669142e-02"
w, q = FTA.calc_AND(E09, E10, E11, E12)
assert format(w, '.8e') == "9.92751753e-36"
assert format(q, '.8e') == "6.07807196e-36"
w, q = FTA.calc_AND(E13, E14, E15, E16)
assert format(w, '.8e') == "1.05687618e-01"
assert format(q, '.8e') == "7.88076792e-01"
w, q = FTA.calc_AND(E09, E10, E11)
assert format(w, '.8e') == "6.26225596e-27"
assert format(q, '.8e') == "5.52551997e-27"
w, q = FTA.calc_AND(E09, E10)
assert format(w, '.8e') == "8.09599996e-19"
assert format(q, '.8e') == "6.07199997e-18"

print("All tests passed.")

