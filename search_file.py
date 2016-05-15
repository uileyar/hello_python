# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os


def file_walk(root):
    wuf_list = []
    for rt, dirs, files in os.walk(root):
        # print('({0}) ({1}) ({2})'.format(rt, dirs, files))
        for f in files:
            wuf_list.append(os.path.join(rt, f))
    logging.info("file_walk file num = %d", len(wuf_list))
    return wuf_list

