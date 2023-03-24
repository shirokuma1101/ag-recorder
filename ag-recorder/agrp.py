# -*- coding: utf-8 -*-

# standard
import datetime
import os
import requests
import subprocess
import time

# m3u8
import m3u8

# debug
from pprint import pprint

class HLS:

    # public

    def __init__(self):
        pass

    @staticmethod
    def download(url, output_dir, headers) -> list:
        file_details = []
        playlist = m3u8.load(url)
        for segment in playlist.segments:
            ts_url = segment.base_uri + segment.uri
            ts = requests.get(ts_url, headers=headers)
            with open(output_dir + os.path.basename(segment.uri), 'wb') as f:
                f.write(ts.content)

            file_details.append({
                'name': os.path.basename(segment.uri),
                'size': len(ts.content),
                'path': output_dir + os.path.basename(segment.uri),
                'url': ts_url,
                'duration': segment.duration,
            })

        return file_details

    @staticmethod
    def encode(file_details, output_dir, file_path) -> None:
        if not file_details:
            return

        filelist_path = output_dir + os.path.splitext(os.path.basename(file_path))[0] + '.txt'
        with open(filelist_path, 'w') as f:
            f.write('\n'.join(['file ' + file_detail['name'] for file_detail in file_details]))

        command = 'ffmpeg -y -loglevel error -f concat -i ' + filelist_path + ' -c copy ' + file_path
        subprocess.run(command, shell=True)

    @staticmethod
    def duration(file_details, margin=0) -> int:
        return sum([file_detail['duration'] for file_detail in file_details]) - sum([file_detail['duration'] for i, file_detail in enumerate(reversed(file_details)) if margin > i])


class AGRP:

    # public

    def __init__(self, ag_hls_url, output_dir=None, headers=None):
        self.ag_hls_url = ag_hls_url
        self.output_dir = output_dir
        self.headers = headers
        self.file_details = []

    def download(self):
        self.file_details.append(HLS.download(self.ag_hls_url, self.output_dir, self.headers))

    def download_until(self, until_datetime, interval_sec=None):
        interval_auto = False
        if not interval_sec:
            interval_sec = 0
            interval_auto = True

        elapsed_sec = 0
        while True:
            if until_datetime < datetime.datetime.now():
                break

            if elapsed_sec < interval_sec:
                elapsed_sec += 1
                time.sleep(1)
                continue

            else:
                elapsed_sec = 0
                file_details = HLS.download(self.ag_hls_url, self.headers, self.output_dir)
                if interval_auto:
                    interval_sec = HLS.duration(file_details, 1)

                self.file_details.append(file_details)

        self.file_details.append(HLS.download(self.ag_hls_url, self.headers, self.output_dir))

    def encode(self, file_path):
        HLS.encode(self._make_unique_file_details(), self.output_dir, file_path)

    # private

    def _make_unique_file_details(self):
        unique_file_details = []
        for file_details in self.file_details:
            for file_detail in file_details:
                if file_detail not in unique_file_details:
                    unique_file_details.append(file_detail)

        return unique_file_details


if __name__ == '__main__':
    ag_hls_url = 'https://hls-base1.mitene.ad.jp/agqr1/iphone/3Gs.m3u8'
    ag = AGRP(ag_hls_url,
            'C:\\Workspace\\Tmp\\',
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'})
    ag.download_until(datetime.datetime(2023, 1, 31, 15, 00, 0))
    ag.encode('C:\\Workspace\\out.mp4')

