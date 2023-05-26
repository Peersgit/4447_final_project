# 4447_final_project
A final project for DU MSDS 4447 Data Science Tools 1

This is a final project for COMP 4447 that demonstrate collecting, manipulating, and cleaning data for further use. The scope of the project is to collect data from ESPN on NFL games since 2017 and conduct exploratory analysis on the effects COVID-19 had on the sport. To retrieve the data, a webscraping script was made using aiohttp and asyncio to efficiently and quickly extract usefull information from an HTML web page. From this script, another notebook file is used to clean and engineer new features that will provide usefull information for our EDA analysis.


# Literature Review
- [Covid's impact using player data](https://coronavirus.jhu.edu/pandemic-data-initiative/data-outlook/moving-goalposts-how-data-show-covid-19-impacted-the-nfl)
- [Rule changes to the NFL 2020 season](https://www.sportingnews.com/us/nfl/news/nfl-covid-rules-coronavirus-football-2020/rovse8r08zbu1quh7y3joydah)

# Data Source
- [ESPN](https://espn.com/nfl)
- [Scraper](ScrapeESPN.py)
