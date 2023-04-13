# standard
import configparser
import datetime
import os
import sys

from pprint import pprint
import wx


def test_agpg():
    from agrecorder.agpg import AGPG

    agpg = AGPG()
    pprint(agpg.get_by_day())
    pprint(agpg.get_by_time())
    agpg.save(agpg.get_by_day(), 'agpg.json')
    pprint(agpg.load('agpg.json'))


def test_agrp():
    from agrecorder.agrp import AGRP

    ag = AGRP('https://hls-base1.mitene.ad.jp/agqr1/iphone/3Gs.m3u8', 'C:\\Workspace\\Tmp\\')
    ag.download_until(datetime.datetime(2023, 4, 3, 22, 5, 0))
    ag.encode('C:\\Workspace\\out.mp4', 'bin\\ffmpeg\\ffmpeg.exe')
    ag.cleanup()


def test_agrw():
    from agrecorder.agrw import AGRW

    agrw = AGRW(None, None)
    agrw.run()


def test_agutil():
    from agrecorder.agutil import AGUtil

    config = configparser.ConfigParser()
    config.read('ag-recorder.ini')

    AGUtil.get_ffmpeg(config['SETTING']['bin_dir'], config['SETTING']['ffmpeg_url'])


def main():
    sys.path.append('.')
    test_agpg()
    test_agrp()
    test_agrw()
    test_agutil()


if __name__ == '__main__':
    main()

