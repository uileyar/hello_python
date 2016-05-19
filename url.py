# coding:utf-8
import httplib2
import json
from util import *
from compat import *

VIDEO_INFO = 'https://drive.google.com/get_video_info?docid='

_FORMATS_EXT = {
    '5': 'flv',
    '6': 'flv',
    '13': '3gp',
    '17': '3gp',
    '18': 'mp4',
    '22': 'mp4',
    '34': 'flv',
    '35': 'flv',
    '36': '3gp',
    '37': 'mp4',
    '38': 'mp4',
    '43': 'webm',
    '44': 'webm',
    '45': 'webm',
    '46': 'webm',
    '59': 'mp4',
}


def _download_info(id):
    http = httplib2.Http(timeout=60)
    video_info_url = VIDEO_INFO + id
    print video_info_url
    for retry in range(3):
        try:
            (resp, content) = http.request(video_info_url, "GET")
            if resp['status'] != '200':
                for (k, v) in resp.items():
                    logging.error("%s: %s", k, v)
                continue
            return content
        except Exception, e:
            logging.error("fail:{0}".format(e))
    return None


def _parse_info(info):
    video_info = compat_parse_qs(info)
    print json.dumps(video_info, indent=2)
    print video_info.get('title')
    print _get_fmt(video_info)

    encoded_url_map = video_info.get('url_encoded_fmt_stream_map', [''])[0]
    for url_data_str in encoded_url_map.split(','):
        url_data = compat_parse_qs(url_data_str)
        #print url_data
        type = _get_type(url_data)
        if 'itag' not in url_data or 'url' not in url_data:
            continue
        format_id = url_data['itag'][0]
        url = url_data['url'][0]
        print format_id, type, url


def mimetype2ext(mt):
    if mt is None:
        return None

    ext = {
        'audio/mp4': 'm4a',
    }.get(mt)
    if ext is not None:
        return ext

    _, _, res = mt.rpartition('/')

    return {
        '3gpp': '3gp',
        'smptett+xml': 'tt',
        'srt': 'srt',
        'ttaf+xml': 'dfxp',
        'ttml+xml': 'ttml',
        'vtt': 'vtt',
        'x-flv': 'flv',
        'x-mp4-fragmented': 'mp4',
        'x-ms-wmv': 'wmv',
    }.get(res, res)


def _get_type(url_data):
    type_ = url_data.get('type', [None])[0]
    if type_:
        type_split = type_.split(';')
        kind_ext = type_split[0].split('/')
        if len(kind_ext) == 2:
            kind, _ = kind_ext
            return kind+'/'+mimetype2ext(type_split[0])


def int_or_none(v, scale=1, default=None, get_attr=None, invscale=1):
    if get_attr:
        if v is not None:
            v = getattr(v, get_attr, None)
    if v == '':
        v = None
    if v is None:
        return default
    try:
        return int(v) * invscale // scale
    except ValueError:
        return default


def _get_fmt(video_info):
    formats_spec = {}
    fmt_list = video_info.get('fmt_list', [''])[0]
    if fmt_list:
        for fmt in fmt_list.split(','):
            spec = fmt.split('/')
            if len(spec) > 1:
                width_height = spec[1].split('x')
                if len(width_height) == 2:
                    formats_spec[spec[0]] = {
                        'resolution': spec[1],
                        'width': int_or_none(width_height[0]),
                        'height': int_or_none(width_height[1]),
                    }
    return formats_spec

def main():
    doc_id ='0B0VS8-zQCcJmNVU1QWdjam02RWs'
    #content = _download_info(doc_id)
    with open('./get_video_info', 'rb') as fp:
        content = fp.read(1024 * 1024 * 10)
    _parse_info(content)



if __name__ == '__main__':
    main()