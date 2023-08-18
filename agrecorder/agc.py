# standard
import configparser


# ag config
class AGC:

    # public

    def __init__(self, config_path: str):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

        self.settings    = self.config['SETTING']
        self.agpgs_dir   = self.settings['AGPGS_DIR']
        self.ffmpeg_path = self.settings['FFMPEG_PATH']
        self.headers     = self.settings['HEADERS']
        self.output_dir  = self.settings['OUTPUT_DIR']

