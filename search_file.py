# coding:utf-8

import os
from util import *
import MySQLdb


def main():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='zhang1234',
        db='files',
    )

    #init_db(conn, unicode('G:/王莹/other/2005巔峰戰將營704/Day 2/2.方城奇謀', 'utf8'))
    #init_db(conn, unicode('G:/', 'utf8'))
    check_file(conn)
    conn.close()


def init_db(conn, root_dir):
    cur = conn.cursor()
    cur.execute('delete FROM files.info')
    num = 0
    for file_path in file_walk(root_dir):
        num +=1
        md5 = md5checksum(file_path)
        logging.info('{0}, {1}, {2}'.format(num, file_path.encode('gb18030'), md5))

        # 插入一条数据
        sqli = "insert into info values(%s,%s)"
        cur.execute(sqli, (file_path.encode('utf8'), md5))
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
    total_size = 0
    total_files = 0
    for (k, v) in files.items():
        for n in range(len(v)-1):
            file_path = v[n]
            path = file_path.decode('utf8')
            size = os.path.getsize(path)
            create_time = os.path.getctime(path)
            modify_time = os.path.getmtime(path)
            total_size += size
            total_files += 1
            logging.info('{0}:{1}k,{2}{3}'.format(path.encode('gb18030'), size / 1024, create_time, modify_time))
    cur.close()
    logging.info('{0}:{1}G'.format(total_files, total_size/(1024*1024*1024)))

if __name__ == '__main__':
    main()
