# standard
import os
import subprocess
import time
from datetime import datetime

# scraping
import requests

# m3u8
import m3u8

# agconfig
from agrecorder.agconfig import AGConfig


# ag record process
class AGRP:

    # public

    class HLS:

        # public

        def __init__(self):
            raise NotImplementedError

        @staticmethod
        def download(hls_url: str, output_dir: str, headers: dict = None) -> list:
            # file detail list to return {name, size, path, url, duration}
            file_details = []

            # parse m3u8
            playlist = m3u8.load(hls_url)

            # download ts files
            for segment in playlist.segments:
                # download ts file
                ts_url = segment.base_uri + segment.uri
                ts = requests.get(ts_url, headers=headers)
                path = f'{output_dir}/{os.path.basename(segment.uri)}'
                with open(path, 'wb') as f:
                    f.write(ts.content)
                # append file details
                file_details.append({
                    'name': os.path.basename(segment.uri),
                    'size': len(ts.content),
                    'path': path,
                    'url': ts_url,
                    'duration': segment.duration,
                })

            # return file details
            return file_details

        @staticmethod
        def interval(file_details: list, margin: int = 0) -> int:
            return (sum([file_detail['duration'] for file_detail in file_details])
                    - sum([file_detail['duration'] for i, file_detail in enumerate(reversed(file_details)) if margin > i]))

        @staticmethod
        def encode(file_details: list, file_path: str, ffmpeg_path: str) -> None:
            if not file_details:
                return

            filelist_path = f"{os.path.dirname(file_details[0]['path'])}/{os.path.splitext(os.path.basename(file_path))[0]}.txt"
            with open(filelist_path, 'w') as f:
                f.write('\n'.join(['file ' + file_detail['name']
                        for file_detail in file_details]))

            cmd = f'"{ffmpeg_path}" -y -loglevel error -f concat -i {filelist_path} -c copy {file_path}'
            subprocess.run(cmd, shell=True)

            os.remove(filelist_path)

        @staticmethod
        def play(hls_url: str, ffplay_path: str) -> None:
            subprocess.Popen(f'{ffplay_path} {hls_url}', shell=True)

        @staticmethod
        def stop() -> None:
            subprocess.run('taskkill /f /im ffplay.exe', shell=True)

    #AG_HLS_URL = 'https://www.uniqueradio.jp/agapps/hls/cdn.m3u8'
    #AG_HLS_URL = 'https://agcdn.cdnext.stream.ne.jp/hls2/basic/data/prog_index.m3u8'
    AG_HLS_URL = 'https://agcdn02.cdnext.stream.ne.jp/hls2/basic/data/prog_index.m3u8'

    def __init__(self, agconfig: AGConfig):
        self._agconfig = agconfig
        self._file_details = []

    def cleanup(self) -> None:
        for file_detail in self._make_unique_file_details():
            os.remove(file_detail['path'])
        self._file_details.clear()

    def download(self) -> list:
        return self.HLS.download(self.AG_HLS_URL, self._agconfig.recording_dir, self._agconfig.headers)

    def download_until(self, until_datetime: datetime, interval_sec: int = None) -> None:
        interval_auto = False
        if not interval_sec:
            interval_sec = 0
            interval_auto = True

        elapsed_sec = 0
        while True:
            if until_datetime < datetime.now():
                break

            if elapsed_sec < interval_sec:
                elapsed_sec += 1
                time.sleep(1)
                continue

            else:
                elapsed_sec = 0
                file_details = self.download()
                if interval_auto:
                    interval_sec = self.HLS.interval(file_details, 1)

                self._file_details.append(file_details)

        self._file_details.append(self.download())

    def encode(self, file_name) -> None:
        #TODO: format file_name
        self.HLS.encode(self._make_unique_file_details(), f'{self._agconfig.recorded_dir}/{file_name}', self._agconfig.ffmpeg_path)

    def play(self) -> None:
        self.HLS.play(self.AG_HLS_URL, self._agconfig.ffplay_path)

    def stop(self) -> None:
        self.HLS.stop()

    # private

    def _make_unique_file_details(self) -> list:
        unique_file_details = []
        for file_details in self._file_details:
            for file_detail in file_details:
                if file_detail not in unique_file_details:
                    unique_file_details.append(file_detail)

        return unique_file_details

