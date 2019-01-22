#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from urllib.request import urlopen
from urllib.parse import urlparse
import configparser
from bs4 import BeautifulSoup
from flask import Flask, render_template, make_response
from email.utils import formatdate

app = Flask(__name__)


def get_data(url):
    """
    Performs a GET request & returns the content with BS
    """
    result = urlopen(url).read()
    return BeautifulSoup(result, "html.parser")

def get_headlines(url, pub_date):
    url = urlparse(url).geturl()
    soup = get_data(url)
    articles = []
    for section in soup.select("div.trendingarticles > div.story"):
        d = {}
        d['title'] = section.find("span", class_="tr-headline").get_text()
        d['url'] = url + section.find("a").get("href")
        d['pub_date'] = pub_date
        articles.append(d)
    return articles


def get_site(site_key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    conf = config[site_key]

    site = {}
    site['title'] = conf['title']
    site['url'] = conf['url']
    site['description'] = conf['description']
    site['pub_date'] = formatdate()
    site['articles'] = get_headlines(str(conf['url']), formatdate())
    
    return site

@app.route("/")
def index():
    return render_template('index.html', feeds=[])

@app.route("/<news_source>.xml")
def get_rss_feed(news_source):
    rss_xml = render_template('index.xml', site=get_site(news_source))
    response = make_response(rss_xml)
    response.headers['Content-Type'] = 'application/rss+xml'
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
