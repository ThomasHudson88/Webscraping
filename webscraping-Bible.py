import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#get a random chapter in John
random_chapter = random.randrange(1,22)

if random_chapter <10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

webpage = 'https://ebible.org/asv/JHN'+random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()		

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

page_verses = soup.find_all('div',class_='p')

print(title.text)

myverses = []
for section_verses in page_verses:
    verse_list = section_verses.text.split('.')

    for v in verse_list:
        myverses.append(v)
#Creating the sections and then each verse in the section by a period, this is pretty accurate not perfect

random_verse = random.choice(myverses)
print(f"Chapter: {random_chapter} Verse: {random_verse}")