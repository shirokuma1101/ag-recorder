# standard
import os
import shutil
from urllib.parse import urlparse

# scraping
import requests


# ag utility
class AGUtil:

    def __init__(self):
        pass

    @staticmethod
    def get_ffmpeg(bin_dir: str, ffmpeg_url: str):
        orig_name = os.path.basename(urlparse(ffmpeg_url).path)
        zip_path = f'{bin_dir}/{orig_name}'
        ffmpeg_dir = f'{bin_dir}/ffmpeg'

        data = requests.get(ffmpeg_url).content
        with open(zip_path, 'wb') as f:
            f.write(data)
        shutil.unpack_archive(zip_path, bin_dir)

        if os.path.exists(path=ffmpeg_dir):
            shutil.rmtree(path=ffmpeg_dir)

        shutil.move(f'{os.path.splitext(zip_path)[0]}/bin', ffmpeg_dir)
        os.remove(path=zip_path)
        shutil.rmtree(path=os.path.splitext(zip_path)[0])

