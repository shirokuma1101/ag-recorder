# standard

# wx
import wx

#
from agrecorder.agpg import AGPG
from agrecorder.agrp import AGRP
from agrecorder.agrw import AGRW


def main():
    agpg = AGPG()
    agrp = AGRP('https://hls-base1.mitene.ad.jp/agqr1/iphone/3Gs.m3u8', 'C:\\Workspace\\Tmp\\')

    app = wx.App()
    agrw = AGRW(agpg, agrp)
    agrw.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

