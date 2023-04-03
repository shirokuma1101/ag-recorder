import datetime
import sys

from pprint import pprint
import wx


def test_agpg():
    #from agrecorder.agpg import AGPG
    from agpg import AGPG

    agpg = AGPG()
    pprint(agpg.get_by_day())
    pprint(agpg.get_by_time())
    agpg.save(agpg.get_by_day(), 'agpg.json')
    pprint(agpg.load('agpg.json'))


def test_agrp():
    #from agrecorder.agrp import AGRP
    from agrp import AGRP

    ag = AGRP('https://hls-base1.mitene.ad.jp/agqr1/iphone/3Gs.m3u8', 'C:\\Workspace\\Tmp\\')
    ag.download_until(datetime.datetime(2023, 4, 3, 22, 5, 0))
    ag.encode('C:\\Workspace\\out.mp4', 'bin\\ffmpeg\\ffmpeg.exe')


def test_agrw():
    #from agrecorder.agrw import AGRW
    from agrw import AGRW

    app = wx.App()
    frame = AGRW(None)
    frame.Show()
    app.MainLoop()


def test_agutil():
    #from agrecorder.agutil import AGUtil
    from agutil import AGUtil

    agutil = AGUtil('config.ini')
    agutil.get_ffmpeg()

def main():
    sys.path.append('agrecorder')
    #test_agpg()
    #test_agrp()
    test_agrw()
    #test_agutil()


if __name__ == '__main__':
    main()
