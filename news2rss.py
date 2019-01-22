#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

def get_data(url):
	"""
	Performs a GET request & returns the content with BS
	"""
	result = urllib.request.urlopen(url).read()
	return BeautifulSoup(result, "html.parser")


def main():
  """
  Main Method if running on the CLI
  """
  URL = 'https://www.irishtimes.com' # TODO: Sample url
  soup = get_data(URL)
  for section in soup.select("div.trendingarticles > div.story"):
    print('Headline:',section.find("span", class_="tr-headline").get_text())
    print('URL:', URL + section.find("a").get("href"))


if __name__ == "__main__":
  main()
