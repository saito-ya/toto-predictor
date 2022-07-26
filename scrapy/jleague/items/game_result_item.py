# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GameResultItem(scrapy.Item):
    id = scrapy.Field()
    game_day = scrapy.Field()
    kickoff_time = scrapy.Field()
    stadium_name = scrapy.Field()
    spectators_num = scrapy.Field()
    weather = scrapy.Field()
    temperature = scrapy.Field()
    humidity = scrapy.Field()
    home_team_name = scrapy.Field()
    home_team_id = scrapy.Field()
    away_team_name = scrapy.Field()
    away_team_id = scrapy.Field()
    home_score = scrapy.Field()
    home_score_1st = scrapy.Field()
    home_score_2nd = scrapy.Field()
    away_score = scrapy.Field()
    away_score_1st = scrapy.Field()
    away_score_2nd = scrapy.Field()
    home_sh = scrapy.Field()
    home_ck = scrapy.Field()
    home_fk = scrapy.Field()
    away_sh = scrapy.Field()
    away_ck = scrapy.Field()
    away_fk = scrapy.Field()
