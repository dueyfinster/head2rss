#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import urllib.request
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

def get_data(url):
    """
    Performs a GET request & returns the content with BS
    """
    result = urllib.request.urlopen(url).read()
    return BeautifulSoup(result, "html.parser")

def get_headlines():
    URL = 'https://www.irishtimes.com' # TODO: Sample url
    soup = get_data(URL)
    for section in soup.select("div.trendingarticles > div.story"):
        print('Headline:',section.find("span", class_="tr-headline").get_text())
        print('URL:', URL + section.find("a").get("href"))

@app.route("/")
def index():
    return render_template('index.html', feeds=[])

@app.route("/<news_source>.rss")
def get_rss_feed(news_source):
    return render_template('index.rss', feeds=[])

if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    get_headlines()
