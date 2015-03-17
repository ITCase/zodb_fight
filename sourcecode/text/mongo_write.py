import timeit

from pymongo import MongoClient

client = MongoClient('mongodb', 27017)

db = client.test_database
dbroot = {}

start_time = timeit.default_timer()
for i in range(1000):
    dbroot['%s_number' % i] = 3
    dbroot['%s_string' % i] = 'Gift'
    dbroot['%s_list' % i] = [1, 2, 3, 5, 7, 12]
    dbroot['%s_dictionary' % i] = {'1918': 'Red Sox', '1919': 'Reds'}
    dbroot['%s_deeply_nested' % i] = {
        '1918': [('Red Sox', 4), ('Cubs', 2)],
        '1919': [('Reds', 5), ('White Sox', 3)],
    }
db.test.insert(dbroot)
elapsed = timeit.default_timer() - start_time
print(elapsed)
