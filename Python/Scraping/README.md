"""
pip3 install lxml
pip3 install BeautifulSoup4
"""

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

#Avoir tous les paragraphes (tags inclus)
    para = soup.find_all('p')

#Avoir tous les paragraphes (tags exclus)
    para = soup.find_all('p')
    for p in para:
        print(p.text)


#Avoir que du texte brut de toute la page
    print(soup.get_text())

#Récupéreer n'importe quelle tag : 
    imgs = soup.find_all('img')
    for img in imgs:
        print(img.get('src'))

#Récupéreer les blocks enfants:
    Exemple récupéreer tous les liens dans un nav
    nav = soup.nav
    links = nav.find_all('a')
    for link url in links:
        print(url.get('href))


#Récupéreer les blocks enfants selon une classe ou un id:
    res = soup.find_all('div', class_='footer-copyright') #Pour rechercher un id alors remplacer class_ par id 
    for s in res:
        print(s.text.strip())



#Pour les ficheirs xml:
    import bs4 as bs
    import urllib.request

    source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
    soup = bs.BeautifulSoup(source, 'xml') #ici c'est bien du xml !

    datas = soup.find_all('loc')

    for data in datas:
        print(data.text)



----------------
#SELENIUM : bot qui simulte un utilisateur utilisant un navigateur

#drivers : https://www.seleniumhq.org/download/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Simulation des touches clavier
import time 

driver = webdriver.Chrome('driver/chromedriver.exe');
driver.set_page_load_timeout(10);
driver.get('https://www.google.com');
driver.find_element_by_name('q').send_keys('Python automatisation'); #ecire sur un input avec un name="q"
driver.find_element_by_name('btnK').send_keys(Keys.ENTER) #Simuler la touche ENTER
time.sleep(4)
driver.close();