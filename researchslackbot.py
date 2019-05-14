#!/bin/python

from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv) > 1:
	name = sys.argv[1]

#authordict = [
#	['as', ],
#	['gjl',


def urlBuilder(name_search):
	url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=' + name_search + '%5BAuthor%5D'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	study_list = soup.find_all('p', class_='title')
	for x in range(len(study_list)):
		print(study_list[x].get_text())


print(urlBuilder('Robbins+R'))

