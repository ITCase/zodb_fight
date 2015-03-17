import timeit

from pymongo import MongoClient

client = MongoClient('mongodb', 27017)
db = client.test_database

start_time = timeit.default_timer()
values = list(db.test.find())
elapsed = timeit.default_timer() - start_time
print(elapsed)
