import requests
from bs4 import BeautifulSoup
import csv

# File path for the CSV file
filename = 'I:/Python/Self Learning/Web Scraping/links.csv'

url = 'https://www.sharesansar.com/announcement'

response = requests.get(url)

#print(response.headers)

# Use 'with' statement to automatically close the file when done
with open(filename, "a", newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all <div> tags with class 'col-lg-1 col-md-1 col-sm-1 hidden-xs'
        div_tags = soup.find_all('div', class_='col-lg-1 col-md-1 col-sm-1 hidden-xs')
        
        # Iterate over each <div> tag found
        for div_tag in div_tags:
            # Find the <a> tag within the <div> tag
            a_tag = div_tag.find('a')
            if a_tag:
                # Extract title and href attributes
                title = a_tag.text.strip()
                href = a_tag.get('href')
                
                # Write the title and href to the CSV file
                csvwriter.writerow([title, href])
            else:
                print('No <a> tag found within <div> tag')
    else:
        print('Failed to fetch webpage:', response.status_code)
