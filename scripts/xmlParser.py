# -*- coding: utf-8 -*-

###############################################################################
# "Twitter Tools" example
###############################################################################
#  Objectives:
#   Using tweepy to parse twitter tags
#  Source:
#   https://www.geeksforgeeks.org/xml-parsing-python/
#   https://stackoverflow.com/questions/18453566/python-dictionary-get-list-of-values-for-list-of-keys
###############################################################################

import csv
import requests
import xml.etree.ElementTree as ET


def saveRSS(downloadPath, url):
    resp = requests.get(url)
    with open(downloadPath, 'wb') as f:
        f.write(resp.content)
    return True


def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text
        newsitems.append(news)
    return newsitems


def saveToCSV(newsitems, filename):
    header = list(newsitems[0].keys())
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(newsitems)
    return True


###############################################################################
# Main
url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
xmlPath = "../data/extracted/XML/news.xml"
csvPath = "../data/extracted/XML/news.csv"

saveRSS(xmlPath, url)
news = parseXML(xmlPath)
saveToCSV(news, csvPath)
