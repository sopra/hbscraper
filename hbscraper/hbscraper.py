#!/usr/local/bin/python

import requests
from bs4 import BeautifulSoup
import lxml.html
import logging
import csv

class hbscraper(object):

  LIST_PAGE = "https://beauty.hotpepper.jp/bsln00031/"

  SHOP_LIST = {
    "Ash 町田店": "https://beauty.hotpepper.jp/slnH000039016/",
    "Ash 銀座店 ": "https://beauty.hotpepper.jp/slnH000039017/",
    "Ash 渋谷店": "https://beauty.hotpepper.jp/slnH000039042/",
    "Ash 鶴見店": "https://beauty.hotpepper.jp/slnH000039045/",
    "Ash 関内店": "https://beauty.hotpepper.jp/slnH000039066/",
    "Ash 緑園都市店": "https://beauty.hotpepper.jp/slnH000039071/",
    "Ash 本八幡店": "https://beauty.hotpepper.jp/slnH000039079/",
    "Ash 立川店": "https://beauty.hotpepper.jp/slnH000039090/",
    "Ash 元町店": "https://beauty.hotpepper.jp/slnH000049741/",
    "Ash 青葉台店": "https://beauty.hotpepper.jp/slnH000063582/",
    "Ash 下北沢店": "https://beauty.hotpepper.jp/slnH000068650/",
    "Ash 大宮店": "https://beauty.hotpepper.jp/slnH000074667/",
    "Ash 中野店": "https://beauty.hotpepper.jp/slnH000074668/",
    "Ash 亀戸店": "https://beauty.hotpepper.jp/slnH000074866/",
    "Ash 北千住店": "https://beauty.hotpepper.jp/slnH000074878/",
    "Ash 仙川店": "https://beauty.hotpepper.jp/slnH000074879/",
    "Ash 池袋店": "https://beauty.hotpepper.jp/slnH000074881/",
    "Ash 千歳烏山店": "https://beauty.hotpepper.jp/slnH000074884/",
    "Ash 川崎店": "https://beauty.hotpepper.jp/slnH000074887/",
    "Ash 京王八王子店": "https://beauty.hotpepper.jp/slnH000074888/",
    "Ash 豊田店": "https://beauty.hotpepper.jp/slnH000074892/",
    "Ash 国立店": "https://beauty.hotpepper.jp/slnH000074894/",
    "Ash 高円寺店": "https://beauty.hotpepper.jp/slnH000074895/",
    "Ash 荻窪店": "https://beauty.hotpepper.jp/slnH000074897/",
    "Ash 武蔵境店": "https://beauty.hotpepper.jp/slnH000074899/",
    "Ash 中目黒店": "https://beauty.hotpepper.jp/slnH000074901/",
    "Ash 学芸大学店": "https://beauty.hotpepper.jp/slnH000074903/",
    "Ash 二子玉川店": "https://beauty.hotpepper.jp/slnH000074905/",
    "Ash 自由が丘店": "https://beauty.hotpepper.jp/slnH000074906/",
    "Ash 戸塚店": "https://beauty.hotpepper.jp/slnH000074909/",
    "Ash 菊名店": "https://beauty.hotpepper.jp/slnH000074910/",
    "Ash 二俣川北口店": "https://beauty.hotpepper.jp/slnH000074912/",
    "Ash 阿佐ヶ谷店": "https://beauty.hotpepper.jp/slnH000074913/",
    "Ash 行徳店": "https://beauty.hotpepper.jp/slnH000074916/",
    "Ash 西川口店": "https://beauty.hotpepper.jp/slnH000074923/",
    "Ash 吉祥寺店": "https://beauty.hotpepper.jp/slnH000076567/",
    "Ash 鶴ヶ峰1号店": "https://beauty.hotpepper.jp/slnH000076568/",
    "Ash 鶴ヶ峰2号店": "https://beauty.hotpepper.jp/slnH000076570/",
    "Ash 横浜店": "https://beauty.hotpepper.jp/slnH000076571/",
    "Ａｓｈ センター南店": "https://beauty.hotpepper.jp/slnH000076572/",
    "Ash 横浜西口店": "https://beauty.hotpepper.jp/slnH000078751/",
    "Ash 東戸塚店": "https://beauty.hotpepper.jp/slnH000078752/",
    "Ash 大倉山店": "https://beauty.hotpepper.jp/slnH000078755/",
    "Ash 西荻窪店": "https://beauty.hotpepper.jp/slnH000078757/",
    "Ash 都立大学店": "https://beauty.hotpepper.jp/slnH000078758/",
    "Ash 保土ヶ谷店": "https://beauty.hotpepper.jp/slnH000080865/",
    "Ash 白楽店": "https://beauty.hotpepper.jp/slnH000080868/",
    "Ash 武蔵小金井店": "https://beauty.hotpepper.jp/slnH000080898/",
    "Ash 瀬谷店": "https://beauty.hotpepper.jp/slnH000080901/",
    "Ash 二俣川南口店": "https://beauty.hotpepper.jp/slnH000080902/",
    "Ash 十日市場店": "https://beauty.hotpepper.jp/slnH000080907/",
    "Ash 新子安店": "https://beauty.hotpepper.jp/slnH000080910/",
    "Ash 市が尾店": "https://beauty.hotpepper.jp/slnH000080912/",
    "Ash 鴨居店": "https://beauty.hotpepper.jp/slnH000080919/",
    "Ash 日吉店": "https://beauty.hotpepper.jp/slnH000080920/",
    "Ash 練馬店": "https://beauty.hotpepper.jp/slnH000081114/",
    "Ash 瑞江店": "https://beauty.hotpepper.jp/slnH000084518/",
    "Ash 大森店": "https://beauty.hotpepper.jp/slnH000084546/",
    "Ash 三鷹店": "https://beauty.hotpepper.jp/slnH000086073/",
    "Ash 桜木町店": "https://beauty.hotpepper.jp/slnH000086099/",
    "Ash 大泉学園店": "https://beauty.hotpepper.jp/slnH000086729/",
    "Ash 小岩店": "https://beauty.hotpepper.jp/slnH000094503/",
    "Ash 町田駅前通り店": "https://beauty.hotpepper.jp/slnH000097246/",
    "Ash 日野店": "https://beauty.hotpepper.jp/slnH000104862/",
    "Ash桜新町店【アッシュ　サクラシンマチ】": "https://beauty.hotpepper.jp/slnH000104863/",
    "Ash たまプラーザ店": "https://beauty.hotpepper.jp/slnH000109084/",
    "Ash 鷺沼店": "https://beauty.hotpepper.jp/slnH000109085/",
    "Ash 稲田堤店": "https://beauty.hotpepper.jp/slnH000109087/",
    "Ash 中山店": "https://beauty.hotpepper.jp/slnH000126115/",
    "Ash 淵野辺店": "https://beauty.hotpepper.jp/slnH000126154/",
    "Ash 等々力店": "https://beauty.hotpepper.jp/slnH000138384/",
    "Ash 本牧店": "https://beauty.hotpepper.jp/slnH000140786/",
    "Ash 元住吉店": "https://beauty.hotpepper.jp/slnH000140789/",
    "Ash さがみ野店": "https://beauty.hotpepper.jp/slnH000142643/",
    "Ash 成瀬店": "https://beauty.hotpepper.jp/slnH000142644/",
    "Ash 浜田山店": "https://beauty.hotpepper.jp/slnH000154875/",
    "Ash 中野坂上店": "https://beauty.hotpepper.jp/slnH000156163/",
    "Ash 石神井公園店": "https://beauty.hotpepper.jp/slnH000159474/",
    "Ash 橋本店": "https://beauty.hotpepper.jp/slnH000166536/",
    "Ash 駒沢大学店【アッシュ　コマザワダイガク】": "https://beauty.hotpepper.jp/slnH000166739/",
    "Ash 都筑ふれあいの丘店": "https://beauty.hotpepper.jp/slnH000166743/",
    "Ash 志木南口店": "https://beauty.hotpepper.jp/slnH000189331/",
    "Ash 北上尾店": "https://beauty.hotpepper.jp/slnH000216740/",
    "Ash 宮前平店 ": "https://beauty.hotpepper.jp/slnH000225604/",
    "Ash 西船橋店": "https://beauty.hotpepper.jp/slnH000227163/",
    "Ash 藤が丘店　": "https://beauty.hotpepper.jp/slnH000231549/",
    "Ash 久我山店": "https://beauty.hotpepper.jp/slnH000231550/",
    "Ash 久が原店　": "https://beauty.hotpepper.jp/slnH000231554/",
    "Ash 池上店　": "https://beauty.hotpepper.jp/slnH000231556/",
    "Ash 亀戸東口店　": "https://beauty.hotpepper.jp/slnH000231558/",
    "Ash 高幡不動店【アッシュ　タカハタフドウ】": "https://beauty.hotpepper.jp/slnH000234662/",
    "Ash 長津田店": "https://beauty.hotpepper.jp/slnH000243311/",
    "Ash 分倍河原店": "https://beauty.hotpepper.jp/slnH000243312/",
    "Ash 八幡山店": "https://beauty.hotpepper.jp/slnH000258022/",
    "Ash 田無店　": "https://beauty.hotpepper.jp/slnH000261867/",
    "Ash 上大岡店": "https://beauty.hotpepper.jp/slnH000263222/",
    "Ash 高津店": "https://beauty.hotpepper.jp/slnH000275236/",
    "Ash One by One 新宿店": "https://beauty.hotpepper.jp/slnH000283187/",
    "Ash あざみ野店": "https://beauty.hotpepper.jp/slnH000298799/",
    "Ash 目白店": "https://beauty.hotpepper.jp/slnH000319501/",
    "Ash 草加店": "https://beauty.hotpepper.jp/slnH000321518/",
    "Ash 三ツ境店": "https://beauty.hotpepper.jp/slnH000323652/",
    "Ash 川口店": "https://beauty.hotpepper.jp/slnH000329228/",
    "Ash 反町店": "https://beauty.hotpepper.jp/slnH000346243/",
    "Ash 相模大野店": "https://beauty.hotpepper.jp/slnH000351414/",
    "Ash 日暮里店　": "https://beauty.hotpepper.jp/slnH000360540/",
  }

  def __init__(self):
    '''
    constructor
    '''
    logging.basicConfig(level=logging.INFO)
    self.resultset = []

  def scrape(self):
    '''
    scraping program
    '''
    for shop, url in self.SHOP_LIST.items():
      self.get_reviewpage(shop, url, 1)
    
    with open('./result.csv', 'w') as f:
      writer = csv.writer(f)
      writer.writerows(self.resultset)

  def get_reviewpage(self, shop, url, page):
    target_url = url + 'review/PN' + str(page) + '.html'
    logging.debug(target_url)

    response = requests.get(target_url)
    logging.debug(response)

    soup = BeautifulSoup(response.text, 'lxml')
    dom = lxml.html.fromstring(response.text)
    # ぺーじから情報取得へ
    self.parse(soup, dom, shop)

    # 「次へ」があれば次のページへ
    prelist = soup.find('div', attrs = {'class', 'preList'}).find('p', attrs = {'class', 'pa bottom0 right0'})
    if '次へ' in prelist.get_text():
      self.get_reviewpage(shop, url, page + 1)
  
  def parse(self, soup, dom, shop):
    '''
    '''
    ### 口コミ一覧を取得
    rv_items = soup.find_all('li', attrs = {'class', 'reportCassette mT30'})
    for ritem in rv_items:
      record = []
      record.append(shop)

      # 投稿日
      record.append(ritem.find('div', attrs = {'class', 'fr'}).get_text())

      # 投稿者（名前は省く）
      record.append(ritem.find('p', attrs = {'class', 'fl w580 pL25'}) \
        .find('span', attrs = {'class', 'mL5 fs10 fgGray'}).get_text())
      
      ### point
      p = ritem.find('ul', attrs = {'class': 'judgeList cFix'}) \

      # total point
      tp = p.select('ul > li:nth-child(1)')[0] \
        .find('span', attrs = {'class', 'mL5 mR10 fgPink'}).get_text()
      logging.debug('tp = ' + tp)
      record.append(tp)

      # funiki
      funiki = p.select('ul > li:nth-child(2)')[0] \
        .find('span', attrs = {'class', 'mL10 fgPink b'}).get_text()
      logging.debug('funiki = ' + funiki)
      record.append(funiki)

      # service
      service = p.select('ul > li:nth-child(3)')[0] \
        .find('span', attrs = {'class', 'mL10 fgPink b'}).get_text()
      logging.debug('service = ' + service)
      record.append(service)

      # tech
      tech = p.select('ul > li:nth-child(4)')[0] \
        .find('span', attrs = {'class', 'mL10 fgPink b'}).get_text()
      logging.debug('tech = ' + tech)
      record.append(tech)

      # menu
      menu = p.select('ul > li:nth-child(5)')[0] \
        .find('span', attrs = {'class', 'mL10 fgPink b'}).get_text()
      logging.debug('menu = ' + menu)
      record.append(menu)

      # comment
      com = ritem.find('div', attrs = {'class', 'mT10 pH10'})
      record.append(com.find('p', attrs = {'class', 'mT10 wwbw'}).get_text())

      # coupon
      record.append(com.find('dd', attrs = {'class', 'oh zoom1'}).get_text())

      # response
      shop_response = ritem.find('div', attrs = {'class', 'mT20 mH10 pV5 pH9 bdGray'})
      if shop_response:
        record.append(shop_response.find('p', attrs = {'class', 'mT10 wwbw'}).get_text())
      else:
        record.append('')

      logging.debug(record)
      self.resultset.append(record)

    

if __name__ == "__main__":
  p = hbscraper()
  p.scrape()