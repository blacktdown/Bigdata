"""
날짜 : 2021/01/04
이름 : 박준우
내용 : 파이썬 mongodb 프로그래밍
"""
from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계 - mongodb 접속
conn = mongo('mongodb://pjw:1234@192.168.56.101:27017')

# 2단계 - DB 선택
db = conn.get_database('pjw')

# 3단계 - Collection(테이블) 선택
collection = db.get_collection('member')

# 4단계 - Query(쿼리) 실행
rs1 = collection.find()
for row in rs1:
    print('--------------------------------')
    print('%s, %s, %s' % (row['uid'], row['name'], row['hp']))

# select * from `member` where uid='a101'
rs2 = collection.find({'uid':'a101'})
for row in rs2:
    print('================================')
    print('%s, %s, %s, %s' % (row['name'], row['pos'], row['dep'], row['rdate']))