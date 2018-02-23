import sys
import csv
import os
import requests
import time

from bs4 import BeautifulSoup

URL = 'http://steamcommunity.com/app/476600/homecontent/?userreviewsoffset=%s&p=%s&numperpage=5&browsefilter=toprated&browsefilter=toprated&appid=476600&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'


def fetch_reviews(page_number):
    url = URL % ((page_number * 10)-10, page_number)
    response = requests.get(url)
    if response.status_code != 200:
        print('Error fetching page: %s' % page_number)
        sys.exit(1)
    return response.content


def extract_content(reviews_data):
    soup = BeautifulSoup(reviews_data, 'html.parser')
    cards = soup.find_all("div", class_="apphub_UserReviewCardContent")
    contents = []
    for card in cards:
        date = card.find_all('div', class_='date_posted')[0].text
        title = card.find_all('div', class_='title')[0].text
        hours = card.find_all('div', class_='hours')[0].text
        review_text = card.find_all(
            'div', class_='apphub_CardTextContent')[-1].text.strip()
        contents.append(
            dict(date=date, title=title, hours=hours, review_text=review_text))
    return contents


if __name__ == '__main__':
    page_number = 0
    writer = csv.writer(open('reviews.csv', 'w'))
    cols = ['date', 'title', 'hours', 'review_text']
    writer.writerow(cols)
    while True:
        page_number += 1
        reviews_file = 'data/reviews_%s.html' % page_number
        if os.path.isfile(reviews_file):
            reviews_data = open(reviews_file).read().decode('utf8')
        else:
            print('Fetching page %s' % page_number)
            reviews_data = fetch_reviews(page_number)
            open(reviews_file, 'w').write(reviews_data)
            time.sleep(1)
        print('Extracting page %s' % page_number)
        for review in extract_content(reviews_data):
            row = []
            for col in cols:
                row.append(review[col].encode('utf8'))
            writer.writerow(row)
