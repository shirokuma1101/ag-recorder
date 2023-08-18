# standard
import os
import shutil
from urllib.parse import urlparse

# scraping
import requests


# ag utility
class AGUtil:

    # public

    FFMPEG_RELEASE_URL = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip'

    def __init__(self):
        """This class provides utility functions for the AG Recorder.

        Raises:
            NotImplementedError: This class should not be instantiated.
        """
        raise NotImplementedError

    @staticmethod
    def get_ffmpeg(bin_dir: str) -> str:
        """Download and extract ffmpeg to the specified directory.

        Args:
            bin_dir (str): The directory to download and extract ffmpeg to.

        Returns:
            str: The path to the extracted ffmpeg directory.
        """
        # ffmpeg dir
        ffmpeg_dir = f'{bin_dir}/ffmpeg'
        # at the moment it parses "ffmpeg-master-latest-win64-gpl-shared.zip" from url
        zip_path = f'{bin_dir}/{os.path.basename(urlparse(AGUtil.FFMPEG_RELEASE_URL).path)}'

        # download and extract ffmpeg
        with open(zip_path, 'wb') as f:
            f.write(requests.get(AGUtil.FFMPEG_RELEASE_URL).content)
        shutil.unpack_archive(zip_path, bin_dir)

        # remove old ffmpeg if exists
        if os.path.exists(ffmpeg_dir):
            shutil.rmtree(ffmpeg_dir)
        # move extracted ffmpeg to ffmpeg dir
        shutil.move(f'{os.path.splitext(zip_path)[0]}/bin', ffmpeg_dir)

        # remove zip and extracted dir
        os.remove(zip_path)
        shutil.rmtree(os.path.splitext(zip_path)[0])

        # return ffmpeg path
        return ffmpeg_dir

