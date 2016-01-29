import parser
from bs4 import BeautifulSoup
import urllib.request as ur
import re


def get_rutracker_html(movie):
	response = ur.urlopen(movie)
	return response.read()

def parse_rutracker(html):
	soup = BeautifulSoup(html)
	table = soup.find("tbody")
	row = table.find('td').findNext('td').findNext()
	print(table.prettify())
	print("________________________________________________")
	print(row.prettify())
	return row.get("href")

def concatenation(movie):
	#movie = movie.decode('utf-8')
	punctiation = re.compile(u'\W+?', re.UNICODE)
	a = (re.sub(punctiation, '+', movie))[:-2]
	print (a)
	return a

def main():
	#print(u'http:\/\/rutracker.online\/' + concatenation(parser.get_movie_name()) + u'.html')
	magnet = parse_rutracker(get_rutracker_html(u'http://rutracker.online\/' + iri_to_uri(concatenation(parser.get_movie_name())) + u'.html'))
	print (magnet)

def iri_to_uri(iri):
    """
    Convert an Internationalized Resource Identifier (IRI) portion to a URI
    portion that is suitable for inclusion in a URL.

    This is the algorithm from section 3.1 of RFC 3987.  However, since we are
    assuming input is either UTF-8 or unicode already, we can simplify things a
    little from the full method.

    Takes an IRI in UTF-8 bytes (e.g. '/I \xe2\x99\xa5 Django/') or unicode
    (e.g. '/I ♥ Django/') and returns ASCII bytes containing the encoded result
    (e.g. '/I%20%E2%99%A5%20Django/').
    """
    # The list of safe characters here is constructed from the "reserved" and
    # "unreserved" characters specified in sections 2.2 and 2.3 of RFC 3986:
    #     reserved    = gen-delims / sub-delims
    #     gen-delims  = ":" / "/" / "?" / "#" / "[" / "]" / "@"
    #     sub-delims  = "!" / "$" / "&" / "'" / "(" / ")"
    #                   / "*" / "+" / "," / ";" / "="
    #     unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"
    # Of the unreserved characters, urllib.quote already considers all but
    # the ~ safe.
    # The % character is also added to the list of safe characters here, as the
    # end of section 3.1 of RFC 3987 specifically mentions that % must not be
    # converted.
    if iri is None:
        return iri
    return quote(force_bytes(iri), safe=b"/#%[]=:;$&()+,!?*@'~")

if __name__ == '__main__':
    main()