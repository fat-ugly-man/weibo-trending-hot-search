#-*- coding:utf-8 -*-
import json
import datetime
import requests
from bs4 import BeautifulSoup

day = datetime.datetime.now()
day_str = day.strftime('%Y-%m-%d')
with open('raw/' + day_str + '.json', 'r') as file:
	data = file.read()
	json_data = json.loads(data)

for item in json_data:
	url = 'https://s.weibo.com/' + item['url']
	print (url)
	ret_data = requests.get(url)
	soup = BeautifulSoup(ret_data.content, 'lxml')	
	#print (soup)
	break
