# agconfig, agrw
from agrecorder.agconfig import AGConfig
from agrecorder.agrw import AGRW


def main():
    agrw = AGRW('ag-recorder.ini')
    agrw.run()


if __name__ == '__main__':
    main()

