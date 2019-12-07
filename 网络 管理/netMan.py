import redis
import os
import csv

r = redis.StrictRedis(host='localhost', port=6379, db=0)

with open('test2.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        print(row[0])
        f=os.popen(row[0])
        d=f.read()
        print(d)
        r.set(row[0],d)
