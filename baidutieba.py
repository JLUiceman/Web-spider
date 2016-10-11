# encoding=utf8

import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup
import re


class Tieba:

	def __init__(self,baseUrl,only):
		self.baseUrl = baseUrl
		self.only  = '?see_lz='+str(only)

	def getData(self,pageNum):
		try:
		    url = self.baseUrl + self.only + '&pn=' + str(pageNum)
		    req = urllib2.Request(url)
		    response = urllib2.urlopen(req)
		    return response
		except urllib2.HTTPError, e:
				print e.code
		except urllib2.URLError, e:
				print e.reason
		else:
				print 'get it'
		finally:
				pass	
	

def getContent(data):
	soup = BeautifulSoup(data,"html.parser")
	for img in soup.find_all('img'):
		print img

def getNum(data):
	num = 0
	soup = BeautifulSoup(data)
	for span in soup.select(".red"):
		num = num + 1
		if num == 2:
			print span.string
			return int(span.string)

def init(num):
	while num > 0 :
		dd = tieba.getData(num).read()
		getContent(dd)
		num = num - 1			

baseUrl = 'http://tieba.baidu.com/p/4752659902'	
tieba = Tieba(baseUrl,1)
data = tieba.getData(1).read()
num = getNum(data)

 
init(num)

