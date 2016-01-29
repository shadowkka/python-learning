from bs4 import BeautifulSoup
import urllib.request as ur
import random
#import downloader

def get_html(url):
    response = ur.urlopen(url)
    return response.read()


def parse_top(html):
	soup = BeautifulSoup(html, "lxml")
	top250 = []
	for i in range(1, 251):
		row = soup.find('tr', id="top250_place_%d" %i)
		name = row.find('a', class_="all")
		top250.append(name.text)
	return top250

def get_movie_name():
	top250 = []
	try:
		f = open ('top250.txt', 'r')
	except IOError as e:
		print(u'Downloading top movies...')
		top250 = parse_top(get_html('file:///home/konstantin-mint17/top250.html'))
		f = open('top250.txt', 'w')
		for i in range (0, 250):
			f.write(top250[i] + '\n')
	f.close()
	f = open('top250.txt', 'r')
	movie = f.readlines()[random.randint(0, 250)]
	f.close()
	return movie
	
if __name__ == '__main__':
    main()
