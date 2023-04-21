# standard
import datetime
import json
import re

# scraping
import requests
from bs4 import BeautifulSoup


# ag program guide
class AGPG:

    # public

    DATE_FORMAT = '%Y%m%d'
    DATETIME_FORMAT = '%Y-%m-%d %H:%M'
    AGPG_URL = 'https://www.joqr.co.jp/qr/agdailyprogram/'

    def __init__(self, agpgs_dir: str, headers: dict = None):
        self.agpgs_dir = agpgs_dir
        self.headers = headers

    def get_by_day(self, dt: datetime.datetime = datetime.datetime.now()) -> list:
        # A&Gの番組表は指定日の29時(翌5時)まであるので、指定日前日の24時から指定日の24時までの番組表を取得する
        agpgs = []

        # 指定日前日の24時からの番組表を取得
        soup = self._get_soup((dt - datetime.timedelta(days=1)).strftime('%Y%m%d'))
        pgs = soup.find_all('article', attrs={'class': re.compile(r'dailyProgram-itemBox.*')})
        for pg in pgs:
            # 24時以降の番組のみ取得
            airtime = self._get_airtime(pg)
            if airtime[0][0] >= 24:
                # 0から23時に変換
                start_dt = datetime.datetime(dt.year, dt.month, dt.day, airtime[0][0] - 24, airtime[0][1])
                end_dt = datetime.datetime(dt.year, dt.month, dt.day, airtime[1][0] - 24, airtime[1][1])
                agpgs.append(self._create_agpg(pg, start_dt, end_dt))

        # 指定日の24時までの番組表を取得
        soup = self._get_soup(dt.strftime('%Y%m%d'))
        pgs = soup.find_all('article', attrs={'class': re.compile(r'dailyProgram-itemBox.*')})
        for pg in pgs:
            # 24時以前の番組のみ取得
            airtime = self._get_airtime(pg)
            if airtime[0][0] < 24:
                start_dt = datetime.datetime(dt.year, dt.month, dt.day, airtime[0][0], airtime[0][1])
                # 終了時間が24時の場合は翌日の0時に変換
                end_dt = (datetime.datetime(dt.year, dt.month, dt.day, airtime[1][0], airtime[1][1])
                          if airtime[1][0] < 24 else
                          datetime.datetime(dt.year, dt.month, dt.day, airtime[1][0] - 24, airtime[1][1]) + datetime.timedelta(days=1))
                agpgs.append(self._create_agpg(pg, start_dt, end_dt))

        return agpgs

    def get_by_time(self, dt: datetime.datetime = datetime.datetime.now(), agpgs: list = None) -> list:
        if agpgs == None:
            agpgs = self.get_by_day(dt)
        # 指定日の指定時刻からの番組表を取得
        return [agpg for agpg in agpgs if agpg['airtime'][0] <= dt and dt < agpg['airtime'][1]]

    @classmethod
    def load(cls, file_path: str) -> list:
        agpgs = []
        with open(file_path, 'r', encoding='utf-8') as f:
            agpgs = json.load(f)
        for agpg in agpgs:
            agpg['airtime'] = [datetime.datetime.strptime(agpg['airtime'][0], cls.DATETIME_FORMAT), datetime.datetime.strptime(agpg['airtime'][1], cls.DATETIME_FORMAT)]
        return agpgs

    @classmethod
    def save(cls, agpgs: list, file_path: str) -> None:
        for agpg in agpgs:
            agpg['airtime'] = [agpg['airtime'][0].strftime(cls.DATETIME_FORMAT), agpg['airtime'][1].strftime(cls.DATETIME_FORMAT)]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(agpgs, f, ensure_ascii=False, indent=None)

    # private

    def _create_agpg(self, pg: BeautifulSoup, start_dt: datetime.datetime, end_dt: datetime.datetime) -> dict:
        agpg = {}
        data_hc_content = (pg.find('div', attrs={'class': 'dailyProgram-itemDetail'}).get('data-hc-content'))
        personality = pg.find('p', attrs={'class': 'dailyProgram-itemPersonality'})
        agpg['data-hc-content'] = data_hc_content if data_hc_content != None else "None"
        agpg['airtime']         = [start_dt, end_dt]
        agpg['title']           = (pg.find('p', attrs={'class': 'dailyProgram-itemTitle'}).text).strip()
        agpg['personality']     = personality.text.strip() if personality != None else "None"
        agpg['description']     = (pg.find('div', attrs={'class': 'dailyProgram-itemDescription rm_container'}).text).strip()
        agpg['repeat']          = True if 'is-repeat' in ' '.join(pg.get('class')) else False
        agpg['url']             = (pg.find('p', attrs={'class': 'dailyProgram-itemTitle'}).find('a').get('href')).strip()
        return agpg

    def _get_airtime(self, pg: BeautifulSoup) -> list:
        airtime = (pg.find('h3', attrs={'class': 'dailyProgram-itemHeaderTime'}).text).strip().split(' – ')
        return [[int(airtime[0].split(':')[0]), int(airtime[0].split(':')[1])],
                [int(airtime[1].split(':')[0]), int(airtime[1].split(':')[1])]]

    def _get_soup(self, date: str) -> BeautifulSoup:
        res = requests.get(f'{self.AGPG_URL}?date={date}', headers=self.headers)
        return BeautifulSoup(res.text, 'lxml')

