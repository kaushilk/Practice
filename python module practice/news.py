import requests
from bs4 import BeautifulSoup

channel = input("What Twitter page would you like to see?: ")

page = requests.get('https://twitter.com/' + str(channel))
soup = BeautifulSoup(page.text, 'html.parser')
list = soup.find_all(class_ ='content' )

i = 1
for item in list:
    print("\nNews Story |", i, "\n-------------------------")
    text = item.p.contents[0]
    try:
        link = item.p.contents[1]['href']
    except IndexError:
        pass
    except TypeError:
        pass
    except KeyError:
        pass
    time = item.small.a['title']
    print(time, "\n", text, "\n", link, "\n-------------------------")
    i += 1
