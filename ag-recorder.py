# standard
import configparser

# agpg, agrp, agrw
from agrecorder.agpg import AGPG
from agrecorder.agrp import AGRP
from agrecorder.agrw import AGRW


def main():
    # config
    config = configparser.ConfigParser()
    config.read('ag-recorder.ini')

    agpg = AGPG(config['SETTING']['AGPGS_DIR'])
    agrp = AGRP(config['SETTING']['AG_HLS_URL'], config['SETTING']['FFMPEG_PATH'], config['SETTING']['OUTPUT_DIR'])

    agrw = AGRW(agpg, agrp)
    agrw.run()


if __name__ == '__main__':
    main()

