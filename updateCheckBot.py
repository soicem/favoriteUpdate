from bs4 import BeautifulSoup

import re
import requests


from database.db import dbConnection


from clock_param import clock
def start(name, pageUrl):
    def getUrl(pageUrl):
        html = requests.get(pageUrl).text
        return html

    def getInfo(pageUrl):
        html = getUrl(pageUrl)
        bsObj = BeautifulSoup(html, "html.parser")
        return bsObj.title

    info = getInfo(pageUrl)
    print(info)

@clock('{name}({args}) dt={elapsed:0.3f}s')
def search(targets):
    for target in targets:
        start(target[1], target[2]) # url