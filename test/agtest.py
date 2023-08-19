# standard
import configparser
import os
import sys
from datetime import datetime, timedelta

from pprint import pprint
import wx


def test_agconfig():
    from agrecorder.agconfig import AGConfig

    agconfig = AGConfig('ag-recorder.ini')
    pprint(agconfig.settings)
    pprint(agconfig.agpgs_dir)
    pprint(agconfig.ffmpeg_path)
    pprint(agconfig.ffplay_path)
    pprint(agconfig.headers)
    pprint(agconfig.recorded_dir)

def test_agpg():
    from agrecorder.agconfig import AGConfig
    from agrecorder.agpg import AGPG

    agconfig = AGConfig('ag-recorder.ini')

    agpg = AGPG(agconfig)
    pprint(agpg.get_by_day())
    pprint(agpg.get_by_time())
    agpg.save()
    pprint(agpg.load())


def test_agrp():
    from agrecorder.agconfig import AGConfig
    from agrecorder.agrp import AGRP

    agconfig = AGConfig('ag-recorder.ini')

    ag = AGRP(agconfig)
    #ag.download()
    ag.download_until(datetime.now())
    ag.encode('out.mp4')
    ag.cleanup()


def test_agrw():
    from agrecorder.agrw import AGRW

    agrw = AGRW(None, None)
    agrw.run()


def test_agutil():
    from agrecorder.agutil import AGUtil
    #agutil = AGUtil()
    AGUtil.get_ffmpeg('./bin')


def main():
    sys.path.append('.')
    #test_agconfig()
    #test_agpg()
    #test_agrp()
    #test_agrw()
    #test_agutil()


if __name__ == '__main__':
    main()

