from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('scraped.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title','place','date'])

for i in range(1,12):
    if(i == 1):
        source = requests.get('https://www.rallylist.com/browse-protest-and-rallies/').text
    else:
        source = requests.get('https://www.rallylist.com/browse-protest-and-rallies/page/' + str(i) + '/').text
    soup = BeautifulSoup(source, 'lxml')

    for article in soup.find_all('article'):
        title = article.h2.a.text
        if(title != "Protesting During Coronavirus Shutdown"):
            print(title)

            place = article.find('div', class_='entry-byline-block entry-byline-cats').a.text
            print(place)

            link = article.find('div', class_='entry-summary').a['href']
            print(link);

            try:
                date = article.find('div', class_='entry-byline-block entry-byline-tags').a.text
                print(date)

            except Exception as e:
                date = "none"
                print(date)

            print()

            csv_writer.writerow([title,place,date,link])

csv_file.close()
