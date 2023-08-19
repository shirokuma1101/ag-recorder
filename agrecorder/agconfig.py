# standard
import configparser


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
    def headers(self) -> dict:
        return self.settings['HEADERS']

    @property
    def recorded_dir(self) -> str:
        return self.settings['RECORDED_DIR']

