from urllib.request import urlopen
import bs4 as bs
import time

start_time = time.time()

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'
source = urlopen(url).read().decode('latin-1')
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
