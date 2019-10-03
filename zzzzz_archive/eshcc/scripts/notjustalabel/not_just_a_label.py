import sys
import csv
import os
import requests
import time

from bs4 import BeautifulSoup

URL = 'https://www.notjustalabel.com/designers?page=%s'
DETAIL_URL = 'https://www.notjustalabel.com/designer/%s'


def fetch_listing_page(page_number):
    url = URL % page_number
    print('fetching listing page %s' % page_number)
    response = requests.get(url)
    if response.status_code != 200:
        print('Error fetching listing %s' % page_number)
        sys.exit(1)

    soup = BeautifulSoup(response.content, 'html.parser')
    designers = soup.find_all('div', class_='views-row')
    designer_urls = []
    for designer in designers:
        url = designer.find_all('a')[-1].attrs['href']
        designer_urls.append(url)
    return designer_urls


def fetch_detail_page(page_id):
    print('fetching detail: %s' % page_id)
    url = DETAIL_URL % page_id
    response = requests.get(url)
    if response.status_code != 200:
        print('Error fetching detail %s' % page_id)
        sys.exit(1)

    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find_all('h1')[0].text.strip()
    location_field = soup.find_all('div', class_='field-content')[0]
    city, country = [f.text for f in location_field.find_all(
        'div', class_='content')]
    return dict(id=page_id, name=name, city=city, country=country)


"""
This is where the main part of program kicks in and where we should start
reading. The first block starting with "if not ..." populates the file
'designers.txt' which hold the information to access the individual designers
pages later on in the program.

The second block starting with "writer = ..." prepares the csv file for writing
content into it
"""

if __name__ == '__main__':

    if not os.path.isfile('designers.txt'):  # If the file is not already there
        urls = []  # Initialize an empty list called 'urls'
        for page_number in range(402):  # Loop through the range 0-402
            # Calls the function above with each of the numbers from the range
            urls.extend(fetch_listing_page(page_number))
            time.sleep(1)  # Be nice to the server: One call per second
        # Write the results of the calls to the file
        open('designers.txt', 'w').write('\n'.join(urls))

    writer = csv.writer(open('designers.csv', 'w'))  # Prepare the output file
    # Names of the columns in the csv file in a list called 'cols'
    cols = ['id', 'name', 'city', 'country']
    writer.writerow(cols)  # Write the header to the file
    # The next line uses the result of the first function stored in the file
    # designers.txt in a list of urls (one per line)
    detail_urls = open('designers.txt').read().splitlines()
    count = 0  # Initialze a variable called count and set it to 0
    # Loop, we use one url at a time from our list detail_urls
    for url in detail_urls:
        # We call our second function defined above passing in the last part
        # of the URL we scraped using our first function. We collect the
        # results in a variable 'details' that we use underneath to fill in
        # the rows of the csv file.
        # The actual contents of details is the dict or dictionary returned
        # by our second function.
        details = fetch_detail_page(url.split('/')[-1])
        time.sleep(1)  # Always be nice to the server at the other end
        # Here we fill the rest of the csv file we setup earlier
        row = []
        for col in cols:
            row.append(details[col].encode('utf8'))
        writer.writerow(row)
        # Just for the workshop, you would want all the results
        count += 1
        if count == 10:
            break
