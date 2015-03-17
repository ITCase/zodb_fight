import timeit

from myzodb import MyZODB

db = MyZODB('./Data.fs')
start_time = timeit.default_timer()
values = db.dbroot.values()
elapsed = timeit.default_timer() - start_time
print(elapsed)
db.close()
