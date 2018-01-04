# coding:utf-8
import base64
import glob
import sys
import time
import math

reload(sys)
sys.setdefaultencoding('utf-8')
import hashlib
import os
import logging
import logging.config

import re
import json
from Crypto.Cipher import AES


# logging.config.fileConfig(os.path.join(os.path.dirname(__file__), './config/logging.ini'))

def sdk_decrypt(buf, key):
    if not buf or not key:
        return None
    try:
        cipher_text = base64.decodestring(buf)
        if not cipher_text:
            return None
        cipher = AES.new(key, AES.MODE_CBC, key)
        plain_text = cipher.decrypt(cipher_text)
        if not plain_text:
            return None
        return plain_text.rstrip('\0')
    except Exception as e:
        return None


def sdk_encrypt(text, key):
    if not text or not key:
        return None
    try:
        cipher = AES.new(key, AES.MODE_CBC, key)
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            text = text + (' ' * add)
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add)
        cipher_text = cipher.encrypt(text)
        if not cipher_text:
            return None
        return base64.encodestring(cipher_text)
    except Exception as e:
        return None


def md5checksum(filename):
    m = hashlib.md5()
    try:
        with open(filename, 'rb') as fp:
            while True:
                blk = fp.read(1024 * 1024 * 10)
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
    logging.info("file num = %d", len(wuf_list))
    return wuf_list


def relative_file_path(abs_file_path, abs_dir):
    rel_file_path = abs_file_path.split(abs_dir)[1]
    if rel_file_path and rel_file_path[0] in '\\/':
        rel_file_path = rel_file_path[1:]
    return rel_file_path


def print_map(prefix_str, in_map):
    i = 1
    for v in in_map:
        logging.info('%s %d: %s: %s', prefix_str, i, v, in_map[v])
        i += 1
    logging.info('%s num = %d', prefix_str, len(in_map))


def print_list(prefix_str, in_list):
    i = 1
    for v in in_list:
        logging.info('{0} {1}: {2}'.format(prefix_str, i, v))
        i += 1
    logging.info('%s num = %d', prefix_str, len(in_list))


def save_to_json(file_path, data):
    f = open(file_path, 'wb')
    if not f:
        return
    f.write(json.dumps(data, sort_keys=True, indent=2))
    f.close()


def load_json(file_path):
    f = open(file_path)
    if not f:
        return
    data = json.loads(f.read())
    f.close()
    # b = json.loads('{"mimeType": "video/mp4", "name": "Yong-Pal Episode 1(Part 4)-360p.MP4", "webContentLink": "https://docs.google.com/uc?id=0B0VS8-zQCcJmZmo5TUJnRndnRGs&export=download", "parents": ["0B0VS8-zQCcJmSVlrNEd0QWt2bHc"], "shared": false, "id": "0B0VS8-zQCcJmZmo5TUJnRndnRGs", "md5Checksum": "3f1e406b0adaede73d59cf579cff8077"}')
    return data


def remove_files(path):
    for fn in glob.glob(path):  # '*'代表匹配所有文件
        if os.path.isdir(fn):  # 如果结果为文件夹
            remove_files(fn)  # 递归
        else:
            print fn


def spend_time(func):
    def new_func(*args, **args2):
        t0 = time.time()
        print("{} start".format(func.__name__))
        back = func(*args, **args2)
        print("{} end, spend {} s".format(func.__name__, time.time() - t0))
        return back
    return new_func


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    if n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = float(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
    return True


def primes(n):
    '''
    http://en.wikipedia.org/wiki/Sieve_of_eratosthenes
    Generate primes using the sieve algorithm
    '''
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = range(3, n + 1, 2)
    m_root = n ** 0.5
    half = ((n + 1) / 2) - 1
    i = 0
    m = 3
    while m <= m_root:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]


def main():
    # file_walk(ROOT_PATH)
    remove_files('/home/john/Downloads/get_video_info*[!d]')
    # print md5checksum('/data/Descendants of the Sun E01(Part 1)-360p.MP4')
    # print get_item_title('Heroes Reborn Season 1 E1-5-360p.MP4', FILE_TYPE_US_DRAMA)
    # print get_item_title('Heroes Reborn Season 1 E1&2-5-360p.MP4', FILE_TYPE_US_DRAMA)


if __name__ == '__main__':
    main()
