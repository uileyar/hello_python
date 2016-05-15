# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import hashlib
import os
import logging
import logging.config
from config import *
import re

logging.config.fileConfig(os.path.join(os.path.dirname(__file__), './config/logging.ini'))


def md5checksum(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as fp:
        while True:
            blk = fp.read(1024 * 1024 * 1)
            if not blk: break
            m.update(blk)
    # print m.hexdigest(), filename
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


def split_file(file):
    file_type = file_name = part_name = ''
    fs = file.split(os.sep)
    if len(fs) < 2:
        logging.error("split_file fail file = %s", file)
    elif len(fs) == 2:
        file_type = FILE_TYPE_KR_DRAMA
        file_name = fs[0]
        part_name = fs[1]
    else:
        file_type = fs[0]
        file_name = fs[1]
        part_name = fs[2]
    return file_type, file_name, part_name


def get_video_title(filename):
    '''
    :param filename: 1 Descendants of the Sun
    :return: Descendants of the Sun
    '''
    title = ''
    match = re.match(r'\d+\s*(.*)', filename)
    if match:
        title = match.group(1)
    else:
        logging.error("%s not match video", filename)
    # logging.info('"%s"', title)
    return title


def get_item_title(filename, file_type):
    title = ''
    if file_type == FILE_TYPE_KR_DRAMA:
        '''
        :param filename: Neighborhood Hero E01 END(Part 4)-360p.MP4
                         Descendants of the Sun E01(Part 1)-360p.MP4
        :return: 1-1
        '''
        match = re.match(r'.*E(\d+)\s*\w*\(.art\s*(\d+)', filename)
        if match:
            if match.group(1)[0] == '0':
                title = match.group(1)[1:]
            else:
                title = match.group(1)
            title = title + '-' + match.group(2)
        else:
            logging.error("%s not match Korean drama", filename)
    elif file_type == FILE_TYPE_US_DRAMA:
        '''
        :param filename: Limitless Season1 E1-1-360p.mp4
        :return: 1-1
        '''
        match = re.match(r'.*E(.+-\d+)-', filename)
        if match:
            title = match.group(1)
        else:
            logging.error("%s not match American drama", filename)
    elif file_type == FILE_TYPE_US_MOVIE:
        '''
        :param filename: 1 Batman vs Superman-360p(Part 2).MP4
        :return: Part 2
        '''
        match = re.match(r'.*\((.art)\s*(\d+)', filename)
        if match:
            title = match.group(1) + ' ' + match.group(2)
        else:
            logging.error("%s not match American movie", filename)
    # logging.info('"%s"', title)
    return title


def main():
    # file_walk(ROOT_PATH)
    print get_item_title('Heroes Reborn Season 1 E1-5-360p.MP4', FILE_TYPE_US_DRAMA)
    print get_item_title('Heroes Reborn Season 1 E1&2-5-360p.MP4', FILE_TYPE_US_DRAMA)


if __name__ == '__main__':
    main()
