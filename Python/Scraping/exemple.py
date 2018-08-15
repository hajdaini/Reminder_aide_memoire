# EXEMPLE 1 "E-commerce Scraping"

from urllib.request import urlopen
import bs4 as bs
import time

start_time = time.time()

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'
source = urlopen(url).read().decode('utf-8')
soup = bs.BeautifulSoup(source, 'lxml')

res = soup.find_all('div', class_='item-container')
items = []

for r in res:
    values = []
    values.append(r.find(class_="item-title").text.replace(',', '|'))
    values.append(r.find(class_="price-current").strong.text)
    values.append(r.find('div', class_="item-branding").img.get('title'))
    items.append(values)

try:
    with open('res.csv', 'w') as file:
        file.write('sep =,\n')  # for excel
        headers = 'name,price,provider\n'
        file.write(headers)
        for item in items:
            file.write(','.join(item) + "\n")
except:
    print("File is already open !")

print("Finish in {0:.4f} s".format(time.time() - start_time))

#----------------------------------------------------------------------------------------

# EXEMPLE 2 "Youtube trending Scraping"

from urllib import request
import bs4 as bs
import time

start_time = time.time()

url = "https://www.youtube.com/feed/trending"
html_content = request.urlopen(url).read().decode('utf-8')

soup = bs.BeautifulSoup(html_content, 'lxml')

res = soup.find_all('div', class_='yt-lockup-content')
items = []

for r in res:
    values = []
    values.append(r.div.a.text)
    values.append(r.h3.a.text.replace(',', '|'))
    try:  # sometimes it appends something wrong and then it crash, that's why i just pass in except (I filter the wrong append when i write in the csv.file)
        values.append(r.select('ul > li')[1].get_text(strip=True)).decode("utf-8")
    except:
        pass
    items.append(values)

try:
    with open('res.csv', 'w') as file:
        file.write('sep =,\n')  # for excel
        headers = 'Youtubeur,Titre,Vues\n'
        file.write(headers)
        for item in items:
            try: # filtering wrong append
                file.write(','.join(item) + "\n")
            except:
                pass
except:
    print("File is already open !")

print("Finish in {0:.4f} s".format(time.time() - start_time))
