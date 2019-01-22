#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_data(session, url):
	"""
	Performs a GET request & returns the content with BS
	"""
	result = session.get(url)
	return BeautifulSoup(result.content, "html.parser")

def post_data(session, url, data):
	"""
	Performs a POST request & returns the content with BS
	"""
	result = session.post(url, data=data, headers=dict(referer=CONF['LOGIN_URL']))
	return BeautifulSoup(result.content, "html.parser")


def main():
  """
	Main Method if running on the CLI
	"""
  URL = 'https://www.irishtimes.com' # TODO: Sample url
  session = requests.session()
  soup = get_data(session, URL)
  ta_section = soup.find("div", class_="trendingarticles")
  for section in ta_section.find_all("div", class_="story"):
    print('Headline:',section.find("span", class_="tr-headline").get_text())
    print('URL:', URL + section.find("a").get("href"))


if __name__ == "__main__":
  main()
