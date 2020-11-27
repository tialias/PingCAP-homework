# -*- coding:utf-8 -*-
import time
from pymysql import *


# 装饰器，计算插入50000条数据需要的时间
def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print("the running time is : ", d_time)

    return decor


@timer
def add_test_users():
    usersvalues = []
    for num in range(100):
        usersvalues.append((num))

    conn = connect(host='127.0.01', port=4000, user='root', password='', database='test', charset='utf8')
    cs = conn.cursor()  # 获取游标
    cs.executemany("insert into t3 values(%s)", usersvalues)

    conn.commit()
    cs.close()
    conn.close()
    print('OK')


add_test_users()
