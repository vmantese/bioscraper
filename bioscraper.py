import requests   # fetches raw web pages for us
from bs4 import BeautifulSoup  # turns raw web pages into object hierarchy and provides selectors
from urlparse import urljoin
#from urlunshort import resolve
import re     # regular expression module for matching, parsing
import csv    # simplifies process of writing data to csv 
import nltk   # natural language tool kit module for quick analysis
import cStringIO #string buffer
from scrape import Scrape
#  a list of URLs about venture capital, investing,  data stores

allowedDomains = ["bizjournals.com","stltoday.com","stlpublicradio.org","alivemag.com","stlamerican.com","techli.com","stlregionalchamber.com","cbslocal.com","ktrs.com","ksdk.com","kmov.com","fox2now.com","kplr11.com"]


pagesToScrape = ["http://www.bizjournals.com/stlouis/blog/biznext/2015/07/10-biggest-funding-rounds-for-startups-so-far-this.html", "http://www.bizjournals.com/stlouis/news/", "http://www.stltoday.com/", "http://news.stlpublicradio.org/#stream/0", "http://www.alivemag.com/", "http://www.stlamerican.com/", "http://techli.com/#.", "http://www.stlregionalchamber.com/who-we-are/chamber-blog", "http://stlouis.cbslocal.com/station/kmox/", "http://www.ktrs.com/", "http://www.ksdk.com/", "http://www.kmov.com/", "http://fox2now.com/", "http://kplr11.com/", "http://www.biospace.com/", "http://medcitynews.com/", "http://www.fiercebiotech.com/", "http://blogs.wsj.com/venturecapital/page/2/", "http://techcrunch.com/", "http://venturebeat.com/", "http://www.bloomberg.com/", "http://www.americanentrepreneurship.com/", "http://siteselection.com/", "http://businessfacilities.com/", "http://www.tradeandindustrydev.com/", "http://www.sec.gov/edgar.shtml", "https://www.sec.gov/about/forms/formd.pdf", "http://www.edgar-online.com/"]

firstScrape = Scrape(pagesToScrape)
for index,URL in enumerate(firstScrape.getDictionary()):
    output = cStringIO.StringIO()
    webpage = requests.get(URL)
    content = webpage.content
    soup = BeautifulSoup(content,'html.parser')
    #print soup.body.text  # good line , gives good text info
    #print soup.title.text  #  also decent line here for quick line-up of titles
    #print soup.select("td")  # good, produces a lot of information but it is all in html as <td info, need to parse futher
    #print soup.body
    output.write("<scrape id=\"" + firstScrape.getAddress() + ":" + str(index) + "\" baseURI=\"" + URL + "\">\n")
    for link in soup.find_all("a", href=True):
        output.write(link['href'])
        output.write('\n')
    output.write("</scrape>\n")
    firstScrape.writeScrape(output)
