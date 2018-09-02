#2. Write a Python program to download and display the content of robot.txt for en.wikipedia.org.

import requests

response = requests.get("https://en.wikipedia.org/robots.txt")

robotText = response.text
print("Robots.txt is a text file webmasters create to instruct web robots (typically search engine robots) how to crawl pages on their website. \n\n")
print("robot.txt from english wikiperia contains: \n\n" + robotText)