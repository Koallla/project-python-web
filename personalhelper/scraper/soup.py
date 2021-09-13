from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone
from .models import Comand
from threading import Thread


import requests


url1 = 'https://terrikon.com/football/ukraine/championship/'
url2 = 'https://football.ua/ukraine/table.html'
data_list_first = []
data_list_second = []
DELTA_TIME = timedelta(minutes=5)

def get_soup(url_adress):
    response = requests.get(url_adress)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_data_first(url1):
    soup = get_soup(url1)
    tr_list = soup.find('table', class_='grouptable').find_all('tr')

    for tr in tr_list[1:]:
        data_dict = {}
        data_dict['rating'] = int(tr.find('td').string[:-1])
        data_dict['name'] = tr.find('a').contents[1].strip()
        data_dict['games'] = int(tr.find('td', class_='team').next_sibling.string)
        data_dict['wins'] = int(tr.find('td', class_='win').string)
        data_dict['draws'] = int(tr.find('td', class_='draw').string)
        data_dict['losses'] = int(tr.find('td', class_='lose').string)
        data_dict['goals_in'] = int(tr.find('td', class_='lose').next_sibling.string)
        data_dict['goals_out'] = int(tr.find('td', string='-').next_sibling.string)
        data_dict['scores'] = int(tr.find('strong').string)
        
        data_list_first.append(data_dict)


def get_data_second(url2):
    soup = get_soup(url2)
    tr_list = soup.find('table', class_='main-tournament-table').find_all('tr')
    
    for tr in tr_list[1:]:
        data_dict = {}
        data_dict['rating'] = int(tr.find('td', class_='num').string)
        data_dict['logo'] = tr.find('td', class_='logo').img.get('src')
        data_dict['name'] = tr.find('td', class_='team').get_text().strip()
        data_dict['games'] = int(tr.find('td', class_='games').get_text())
        data_dict['wins'] = int(tr.find('td', class_='win').get_text())
        data_dict['draws'] = int(tr.find('td', class_='draw').get_text())
        data_dict['losses'] = int(tr.find('td', class_='lose').get_text())
        data_dict['goals_in'] = int(tr.find('td', class_='goal').get_text())
        data_dict['goals_out'] = int(tr.find('td', class_='miss').get_text())
        data_dict['difference'] = int(tr.find('td', class_='diff').get_text())
        data_dict['scores'] = int(tr.find('td', class_='score').get_text())

        data_list_second.append(data_dict)


def rec_data_to_lists():
    data_first = Thread(target=get_data_first, args=(url1,))
    data_first.start()
    data_second = Thread(target=get_data_second, args=(url2,))
    data_second.start()
    data_first.join()
    data_second.join()
    

def save_to_db():
    global data_list_first
    global data_list_second
    for i in range(len(data_list_first)):
        data_list_first[i].update(data_list_second[i])

        db_comand = Comand(
        rating = data_list_first[i]['rating'],
        logo = data_list_first[i]['logo'],
        name = data_list_first[i]['name'],
        games = data_list_first[i]['games'],
        wins = data_list_first[i]['wins'],
        draws = data_list_first[i]['draws'],
        losses = data_list_first[i]['losses'],
        goals_in = data_list_first[i]['goals_in'],
        goals_out = data_list_first[i]['goals_out'],
        difference = data_list_first[i]['difference'],
        scores = data_list_first[i]['scores'],    
        )

        db_comand.save()
    
    data_list_first = []
    data_list_second = []


def add_commands_to_db():
    if Comand.objects.order_by('?').first():
        data_created = Comand.objects.order_by('?').first().created
        difference = datetime.now(timezone.utc) - data_created
        if difference > DELTA_TIME:
            Comand.objects.all().delete()
            rec_data_to_lists()
            save_to_db()
    else:
        rec_data_to_lists()
        save_to_db()
        