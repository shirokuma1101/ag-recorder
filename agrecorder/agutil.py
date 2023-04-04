# standard
import configparser
import os
import shutil
import urllib.parse

# scraping
import requests


# ag utility
class AGUtil:

    def __init__(self, config_path: str):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.bin_dir = self.config['SETTING']['bin_dir']

    def get_ffmpeg(self):
        url = self.config['SETTING']['ffmpeg_url']
        orig_name = os.path.basename(urllib.parse.urlparse(url).path)
        zip_path = f'{self.bin_dir}/{orig_name}'
        ffmpeg_dir = f'{self.bin_dir}/ffmpeg'

        data = requests.get(url).content
        with open(zip_path, 'wb') as f:
            f.write(data)
        shutil.unpack_archive(zip_path, self.bin_dir)

        if os.path.exists(path=ffmpeg_dir):
            shutil.rmtree(path=ffmpeg_dir)

        shutil.move(f'{os.path.splitext(zip_path)[0]}/bin', ffmpeg_dir)
        os.remove(path=zip_path)
        shutil.rmtree(path=os.path.splitext(zip_path)[0])

