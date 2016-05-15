# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import hashlib
import os
import logging
import logging.config


logging.config.fileConfig(os.path.join(os.path.dirname(__file__), './config/logging.ini'))


def md5checksum(filename):
    m = hashlib.md5()
    try:
        with open(filename, 'rb') as fp:
            while True:
                blk = fp.read(1024 * 1024 * 1)
                if not blk: break
                m.update(blk)
    # print m.hexdigest(), filename
    except Exception, e:
        logging.error('open {0} err:{1}'.format(filename, str(e)))
    return m.hexdigest()


def ensure_dir(directory):
    if not os.path.exists(directory):
        logging.info("Creating directory: %s" % directory)
        try:
            os.makedirs(directory)
        except OSError, e:
            logging.debug("makedirs Faild: %s", str(e))


def file_walk(root):
    wuf_list = []
    for rt, dirs, files in os.walk(root):
        # print('({0}) ({1}) ({2})'.format(rt, dirs, files))
        for f in files:
            wuf_list.append(os.path.join(rt, f))
    logging.info("file_walk file num = %d", len(wuf_list))
    return wuf_list


def main():
    pass


if __name__ == '__main__':
    main()
