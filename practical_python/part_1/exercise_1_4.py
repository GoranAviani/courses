"""
Exercise 1.4: Where is My Bus?
"""
import urllib.request
from xml.etree.ElementTree import parse


def main():
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
    doc = parse(u)
    print(doc)
    for pt in doc.findall('.//pt'):
        print(pt.text)

if __name__ == '__main__':
    main()