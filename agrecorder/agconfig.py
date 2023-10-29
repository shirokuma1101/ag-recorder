# standard
import configparser
from datetime import datetime
import json


# ag config
class AGConfig:

    # public

    def __init__(self, config_path: str):
        self._config = configparser.ConfigParser()
        self._config.read(config_path)

    @property
    def settings(self) -> dict:
        return self._config['SETTING']

    @property
    def agpgs_dir(self) -> str:
        return self.settings['AGPGS_DIR']

    @property
    def ffmpeg_path(self) -> str:
        return self.settings['FFMPEG_PATH']

    @property
    def ffplay_path(self) -> str:
        return self.settings['FFPLAY_PATH']

    @property
    def get_agpgs_time(self) -> list:
        return [datetime.strptime(t, '%H:%M:%S').time() for t in eval(self.settings['GET_AGPGS_TIME'])]

    @property
    def headers(self) -> dict:
        return json.loads(self.settings['HEADERS'])

    @property
    def recorded_dir(self) -> str:
        return self.settings['RECORDED_DIR']

    @property
    def recording_dir(self) -> str:
        return self.settings['RECORDING_DIR']

