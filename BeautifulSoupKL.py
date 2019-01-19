#Credits to "SAF Business Analytics" [Youtube: https://youtu.be/SWHAMG71O7U]
from bs4 import BeautifulSoup
import urllib, csv, os, datetime, urllib.request, re, sys
# choose a 'html based weather website'.
theurl="https://www.yr.no/place/Malaysia/Kuala_Lumpur/Kuala_Lumpur/hour_by_hour.html"
thepage=urllib.request.urlopen(theurl)
soup=BeautifulSoup(thepage,"html.parser")
soup
# hunt for the information you want. Perhaps go to source page and 'select','inspect element' to see source code
soup.find_all('tr')
soup.find_all('tr')[0]
soup.find_all('tr')[20]
