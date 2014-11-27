#!/usr/bin/env python
#-*- coding: utf-8 -*-

from urllib import urlopen
from datetime import datetime
from bs4 import BeautifulSoup
from urllib2 import urlopen

def updateUrl (url):
	f=urlopen('http://gaybb.me/category/debtdandy/')


def orariFermata (numeroFermata):
	ris=[]

	sock = urlopen ("http://www.5t.torino.it/5t/trasporto/arrivi.jsp?stoppingPointCtl:action:getTransits&shortName=" + str(numeroFermata))    
	temp_html = sock.read().decode("utf-8").encode('cp850','replace').decode('cp850')

	data = temp_html[temp_html.find('Data'):]
	data = data[6:data.find('<')]
	for el in data.split():
		if (':' in el):
			ora = el
	now = datetime.strptime(ora, "%H:%M:%S")

	# Parsifica l'HTML
	soup = BeautifulSoup(temp_html)
	table = soup.find_all ('table')[0]
	row = table.find_all ('tr')


	for i in range (1, len(row)):
		col = row[i].find_all('td')
		bus =  {}	
		bus['linea'] = col[0].find_all('a')[0].string
		bus['orario'] = [divmod((datetime.strptime(col[1].string, "%H:%M") - now).seconds, 60)[0], col[1].string]
	
		if (len(col[2].find_all('div')) == 0):  
			bus['tipo'] = col[2].string
		else:
			bus['tipo'] = col[2].find_all('div')[0].string

		ris.append(bus)

	return ris


