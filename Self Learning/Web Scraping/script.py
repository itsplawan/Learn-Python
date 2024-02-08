import requests
import bs4 as beautifulsoup
import csv

file = 'I:\Python\Self Learning\Web Scraping\links.csv'

url = 'https://www.sharesansar.com/announcement'

response = requests.get(url)

with open(file,"a") as file:
    csvwriter = csv.writer(file)
    if response.status_code == 200:
        soup = beautifulsoup(response.text, 'html.parser')
        div_tags = soup.find('div',class_='col-lg-1 col-md-1 col-sm-1 hidden-xs')

       