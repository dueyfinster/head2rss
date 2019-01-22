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
  URL = 'https://www.irishtimes.com/' # TODO: Sample url
  session = requests.session()
  soup = get_data(session, URL)
  print(soup)


if __name__ == "__main__":
  main()
