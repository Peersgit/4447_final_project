from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import re
import numpy as np

import asyncio
import aiohttp

headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/101.0.4951.67 Safari/537.36"
                }




def year_check(year):
    if year < 2020:
        return True
    else:
        return False
    

async def scrape_main_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return []
            
            html = await response.text()
            game_ids = extract_game_ids(html)
            return game_ids

def extract_game_ids(html):
    soup = BeautifulSoup(html, 'html.parser')

    return [box.get('id') for box in soup.find_all('section', class_=re.compile('^Scoreboard bg'))]


async def scrape_game_data(game_id):
    url = 'https://www.espn.com/nfl/playbyplay/_/gameId/{}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url.format(game_id)) as response:
            if response.status != 200:
                return None
            html = await response.text()
            data = parse_html(html, url.format(game_id))
            return data



def parse_html(html, url):

    soup = BeautifulSoup(html, 'html.parser')

    score_table = soup.find('tbody', class_='Table__TBODY')

    if score_table != None:
        table = score_table.find_all('tr')
    else:
        table = [0]

    if len(table) != 2:
        away_ = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
        home_ = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    else:
        away_, home_ = score_table.find_all('tr')
        away_ = [x.text for x in away_.find_all('td')]
        home_ = [x.text for x in home_.find_all('td')]

    away_team_name = AER_check(soup.find('div', class_=re.compile('^Gamestrip__Team--away')).find('h2', class_=re.compile('^ScoreCell')))

    home_team_name = AER_check(soup.find('div', class_=re.compile('^Gamestrip__Team--home')).find('h2', class_=re.compile('^ScoreCell')))

    stadium_name = AER_check(soup.find('div', class_=re.compile('^GameInfo__Location__Name')))

    records = soup.find_all('div', class_=re.compile('^Gamestrip__Record'))

    if len(records) == 2:
        away_current_record = AER_check(records[0])
        home_current_record = AER_check(records[1])
    else:
        away_current_record = np.nan
        home_current_record = np.nan

    game_date = AER_check(soup.find('div', class_='n8 GameInfo__Meta').find('span'))

    game_location = AER_check(soup.find('span', class_='Location__Text'))

    sa = AER_check(soup.find('div', class_='Attendance__Numbers'))
    if sa == np.nan:
        stadium_attendance = sa
    else:
        stadium_attendance = str(sa).replace('Attendance: ', '')

    sc = AER_check(soup.find('div', class_=re.compile('Attendance__Capacity')))
    if sc == np.nan:
        stadium_capacity = sc
    else:
        stadium_capacity = str(sc).replace('Capacity: ', '')

    return {
        'game_url': url,
        'away_team_name': away_team_name,
        'away_team_initials': away_[0],
        'away_record_status': away_current_record,
        'away_Q1': away_[1],
        'away_Q2': away_[2],
        'away_Q3': away_[3],
        'away_Q4': away_[4],
        'away_final_score': away_[5],
        'home_team_name': home_team_name,
        'home_team_initials': home_[0],
        'home_record_status': home_current_record,
        'home_Q1': home_[1],
        'home_Q2': home_[2],
        'home_Q3': home_[3],
        'home_Q4': home_[4],
        'home_final_score': home_[5],
        'stadium_name': stadium_name,
        'stadium_attendance': stadium_attendance,
        'stadium_capacity': stadium_capacity,
        'game_location': game_location,
        'game_date': game_date
    }
    


def save_data(data, name):

    frame = pd.DataFrame(data)

    frame.to_csv(name, index=False)


def AER_check(func):
    """ Attribute Error Check """
    try:
        return func.text
    except AttributeError:
        return np.nan
         


async def main():

    base_url = 'https://www.espn.com/nfl/scoreboard/_/week/{}/year/{}/seasontype/{}'

    pre_2020 = {
        2: list(range(1, 18)),
        3: [1,2,3,4,5]
    }

    post_2020 = {
        2: list(range(1,19)),
        3: [1,2,3,4,5]
    }

    years=[2022]
    tps = [2,3]

    file_name = '-22'

    tasks=[]
    for year in years:
        for tp in tps:
            if year_check(year):
                for val in pre_2020[tp]:
                    tasks.append(asyncio.ensure_future(scrape_main_page(base_url.format(val, year, tp))))
            else:
                for val in post_2020[tp]:
                    tasks.append(asyncio.ensure_future(scrape_main_page(base_url.format(val, year, tp))))


    start_time_main = time.time()
    results = await asyncio.gather(*tasks)
    end_time_main = time.time()

    game_data_tasks = []
    for result in results:
        for game_id in result:
            game_data_tasks.append(asyncio.ensure_future(scrape_game_data(game_id)))


    start_time = time.time()
    game_data_results = await asyncio.gather(*game_data_tasks)
    end_time = time.time()
    data = [gd for gd in game_data_results if gd is not None]

    print("The amount of time it takes to scrape the main data pages: {}".format(end_time_main - start_time_main))
    print("The amount of time it takes to gather all of the game data: {}".format(end_time - start_time))
    print("########")

    save_data(data, f'./Data/NFLData{file_name}.csv')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
