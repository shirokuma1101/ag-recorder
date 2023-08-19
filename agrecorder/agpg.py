# standard
import json
import os
import re
from datetime import datetime, timedelta
from enum import Enum, auto

# scraping
import requests
from bs4 import BeautifulSoup

# agconfig
from agrecorder.agconfig import AGConfig


# ag program guide
class AGPG:

    # public

    class Items(Enum):
        ID          = 0
        AIRTIME     = auto()
        TITLE       = auto()
        PERSONALITY = auto()
        DESCRIPTION = auto()
        REPEAT      = auto()
        URL         = auto()

    URL_QUERY_DATE_FORMAT     = '%Y%m%d'
    SERIALIZE_DATETIME_FORMAT = '%Y-%m-%d %H:%M'
    AGPG_URL                  = 'https://www.joqr.co.jp/qr/agdailyprogram/'

    def __init__(self, agconfig: AGConfig, dt: datetime = datetime.now()):

        # private

        self._agconfig = agconfig
        self._agpgs = []
        self._dt = dt

    def get_by_day(self, force: bool = False) -> list:
        if self._agpgs and not force:
            return self._agpgs
        if self.load():
            return self._agpgs
        # A&Gの番組表は指定日の29時(翌5時)まであるので、指定日前日の24時から指定日の24時までの番組表を取得する
        self._agpgs.clear()

        # 指定日前日の24時からの番組表を取得
        soup = self._get_soup(self._dt - timedelta(days=1))
        pgs = soup.find_all('article', attrs={'class': re.compile(r'dailyProgram-itemBox.*')})
        for pg in pgs:
            # 24時以降の番組のみ取得
            airtime = self._get_airtime(pg)
            if airtime[0][0] >= 24:
                # 0から23時に変換
                start_dt = datetime(self._dt.year, self._dt.month, self._dt.day, airtime[0][0] - 24, airtime[0][1])
                end_dt = datetime(self._dt.year, self._dt.month, self._dt.day, airtime[1][0] - 24, airtime[1][1])
                self._agpgs.append(self._create_agpg(pg, start_dt, end_dt))

        # 指定日の24時までの番組表を取得
        soup = self._get_soup(self._dt)
        pgs = soup.find_all('article', attrs={'class': re.compile(r'dailyProgram-itemBox.*')})
        for pg in pgs:
            # 24時以前の番組のみ取得
            airtime = self._get_airtime(pg)
            if airtime[0][0] < 24:
                start_dt = datetime(self._dt.year, self._dt.month, self._dt.day, airtime[0][0], airtime[0][1])
                # 終了時間が24時の場合は翌日の0時に変換
                end_dt = (datetime(self._dt.year, self._dt.month, self._dt.day, airtime[1][0], airtime[1][1])
                          if airtime[1][0] < 24 else
                          datetime(self._dt.year, self._dt.month, self._dt.day, airtime[1][0] - 24, airtime[1][1]) + timedelta(days=1))
                self._agpgs.append(self._create_agpg(pg, start_dt, end_dt))

        return self._agpgs

    def get_by_time(self, dt: datetime = datetime.now()) -> list:
        if self._agpgs == None:
            self.get_by_day(dt)
        # 指定日の指定時刻からの番組表を取得
        return [agpg for agpg in self._agpgs if agpg['airtime'][0] <= dt and dt < agpg['airtime'][1]]

    def load(self) -> list:
        file_path = f'{self._agconfig.agpgs_dir}/{self._dt.strftime(self.URL_QUERY_DATE_FORMAT)}.json'
        if (os.path.exists(file_path) == False):
            return []

        with open(file_path, 'r', encoding='utf-8') as f:
            self._agpgs = json.load(f)
        for agpg in self._agpgs:
            agpg['airtime'] = [datetime.strptime(agpg['airtime'][0], self.SERIALIZE_DATETIME_FORMAT), datetime.strptime(agpg['airtime'][1], self.SERIALIZE_DATETIME_FORMAT)]
        return self._agpgs

    def save(self) -> None:
        file_path = f'{self._agconfig.agpgs_dir}/{self._dt.strftime(self.URL_QUERY_DATE_FORMAT)}.json'
        for agpg in self._agpgs:
            agpg['airtime'] = [agpg['airtime'][0].strftime(self.SERIALIZE_DATETIME_FORMAT), agpg['airtime'][1].strftime(self.SERIALIZE_DATETIME_FORMAT)]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self._agpgs, f, ensure_ascii=False, indent=None)

    # private

    @classmethod
    def _create_agpg(cls, pg: BeautifulSoup, start_dt: datetime, end_dt: datetime) -> dict:
        agpg = {}
        data_hc_content = (pg.find('div', attrs={'class': 'dailyProgram-itemDetail'}).get('data-hc-content'))
        personality = pg.find('p', attrs={'class': 'dailyProgram-itemPersonality'})
        agpg[cls.Items.ID.name.lower()]          = data_hc_content if data_hc_content != None else 'None'
        agpg[cls.Items.AIRTIME.name.lower()]     = [start_dt, end_dt]
        agpg[cls.Items.TITLE.name.lower()]       = (pg.find('p', attrs={'class': 'dailyProgram-itemTitle'}).text).strip()
        agpg[cls.Items.PERSONALITY.name.lower()] = personality.text.strip() if personality != None else 'None'
        agpg[cls.Items.DESCRIPTION.name.lower()] = (pg.find('div', attrs={'class': 'dailyProgram-itemDescription rm_container'}).text).strip()
        agpg[cls.Items.REPEAT.name.lower()]      = True if 'is-repeat' in ' '.join(pg.get('class')) else False
        agpg[cls.Items.URL.name.lower()]         = (pg.find('p', attrs={'class': 'dailyProgram-itemTitle'}).find('a').get('href')).strip()
        return agpg

    @staticmethod
    def _get_airtime(pg: BeautifulSoup) -> list:
        airtime = (pg.find('h3', attrs={'class': 'dailyProgram-itemHeaderTime'}).text).strip().split(' – ')
        return [[int(airtime[0].split(':')[0]), int(airtime[0].split(':')[1])],
                [int(airtime[1].split(':')[0]), int(airtime[1].split(':')[1])]]

    def _get_soup(self, dt: datetime) -> BeautifulSoup:
        res = requests.get(f'{self.AGPG_URL}?date={dt.strftime(self.URL_QUERY_DATE_FORMAT)}', headers=self._agconfig.headers)
        return BeautifulSoup(res.text, 'lxml')

