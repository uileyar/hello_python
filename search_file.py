# coding:utf-8

import os
from util import *
import MySQLdb


def main():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234',
        db='files',
    )

    #init_db(conn, 'G:\\')
    check_file(conn)
    conn.close()


def init_db(conn, root_dir):
    cur = conn.cursor()
    cur.execute('delete FROM files.info')

    for file_path in file_walk(root_dir):
        md5 = md5checksum(file_path)

        # 插入一条数据
        sqli = "insert into info values(%s,%s)"
        cur.execute(sqli, (file_path, md5))
    cur.close()
    conn.commit()


def check_file(conn):
    files = {}
    cur = conn.cursor()
    cur.execute("SELECT * FROM info")
    rows = cur.fetchall()
    for row in rows:
        if row[1] not in files:
            files[row[1]] = []
        files[row[1]].append(row[0])
    for (k, v) in files.items():
        if len(v) > 1:
            for file_path in v:
                size = os.path.getsize(file_path) / 1024
                create_time = os.path.getctime(file_path)
                modify_time = os.path.getmtime(file_path)
                logging.info('{0}:{1}k,{2}{3}'.format(file_path, size, create_time, modify_time))

    cur.close()


if __name__ == '__main__':
    main()
