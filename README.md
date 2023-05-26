# 4447_final_project
A final project for DU MSDS 4447 Data Science Tools 1

This is a final project for COMP 4447 that demonstrates collecting, manipulating, cleaning, and visualizing data for further use. The scope of the project is to collect data from ESPN on NFL games since 2017 and conduct exploratory analysis on the effects COVID-19 had on the sport. To retrieve the data, a web scraping script was made using the python libraries aiohttp and asyncio to efficiently and quickly extract useful information from an HTML web page. From this script, another notebook file is used to clean and engineer new features that will provide useful information for our EDA analysis.


# Literature Review
- [Covid's impact using player data](https://coronavirus.jhu.edu/pandemic-data-initiative/data-outlook/moving-goalposts-how-data-show-covid-19-impacted-the-nfl)
- [Rule changes to the NFL 2020 season](https://www.sportingnews.com/us/nfl/news/nfl-covid-rules-coronavirus-football-2020/rovse8r08zbu1quh7y3joydah)


# Data Source
- [ESPN](https://www.espn.com/nfl/scoreboard/_/week/1/year/2022/seasontype/2)
- [Scraper](ScrapeESPN.py)


# Binder
- [Analysis.ipynb](https://mybinder.org/v2/gh/Peersgit/4447_final_project/main?labpath=Analysis.ipynb)
- [featureEngineering.ipynb](https://mybinder.org/v2/gh/Peersgit/4447_final_project/main?labpath=featureEngineering.ipynb)


# Collected Features
- game_url : url for the game
- away_team_name : The name of the away team
- away_team_initials : The initials for the away team
- away_Q1 : First quarter score for the away team
- away_Q2 : Second quarter score for the away team
- away_Q3 : Third quarter score for the away team
- away_Q4 : Fourth quarter score for the away team
- away_final_score : The away teams final score of the match
- home_team_name : The name of the home team
- home_team_initials : The initials for the home team
- home_Q1 : First quarter score for the home team
- home_Q2 : Second quarter score for the home team
- home_Q3 : Third quarter score for the home team
- home_Q4 : Fourth quarter score for the home team
- home_final_score : The home team final score of the match
- stadium_name : Name of the stadium
- stadium_attendance : Attendance for the game
- stadium_capacity : Capcity of the stadium
- game_date : Date of the game
- season : year (2017 - 2022)

# Engineered Features
- away_team_win_perc : The win percentage for the away team at every game. (If they win their first game, their win % for the second game would be 100%)
- home_team_win_perc : The win percentage for the home team at every game. (If they win their first game, their win % for the second game would be 100%)
- Q1_diff : The difference between the home and away quarter 1 score
- Q2_diff : The difference between the home and away quarter 2 score
- Q3_diff : The difference between the home and away quarter 3 score
- Q4_diff : The difference between the home and away quarter 4 score
- final_score_diff : The difference between the final score for the home and away team
- home_avg : The average points score for all 4 quarters, home
- away_avg : The average points score for all 4 quarters, away
- winner : The finner of the game, 1:home, 0:away
- lat_away : Coordinates for the away team
- long_away : Coordinates for the away team
- lat_home : Coordinates for the home team
- long_home : Coordinates for the home team
- lat_game : Coordinates for the stadium the game is played at
- long_game : Coordinates for the stadium the game is played at
- away_distance_to_game : The distance the away team had to travel for each game
- home_distance_to_game : The distance the home team had to travel for each game
- city : The name of the city the stadium resides in
- state_code : The state code for that city
