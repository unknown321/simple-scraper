#!/usr/bin/python

# scrapes webpages listed in a text file (file 1)
# looks for domains from another text file
# if domain is found on page, then pair [page url, domain] is written to csv file

import csv
import urllib2

file1 = open('urls.txt','r')
urls = file1.readlines()
file1.close()
file2 = open('domains.txt','r')
domains = file2.readlines()
file2.close()
csvfile = open('result.csv', 'wb')
csvwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

for u in urls:
	url = u.rstrip('\n')
	try:
		page = urllib2.urlopen(url).read()
	except Exception, e:
		print e
	else:
		for d in domains:
			domain = d.rstrip('\n')
			r = page.find(domain)
			if r!=-1:
				csvwriter.writerow([url,domain])
csvfile.close()