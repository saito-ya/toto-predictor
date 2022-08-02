import scrapy
from scrapy.loader import ItemLoader
from urllib.parse import urlparse
from jleague.itemloaders.game_result_loader import GameResultLoader
from jleague.items.game_result_item import GameResultItem


BASE_URL = 'https://data.j-league.or.jp/SFMS01'

COMPETITION_YEAR = '2022'   # 年度
COMPETITION_FRAME_ID = '1'  # 大会のカテゴリ

def get_start_urls(year: str, frame_id: str) -> list[str]:
    return [
        f'{BASE_URL}/search?competition_years={year}&competition_frame_ids={frame_id}'
    ]

class GameResultSpider(scrapy.Spider):
    name = 'data.j-league.or.jp/SFMS01'
    allowed_domains = ['data.j-league.or.jp']
    start_urls = get_start_urls(COMPETITION_YEAR, COMPETITION_FRAME_ID)

    def parse(self, response):
        table = response.xpath('//table[contains(@class, "search-table")]')

        for record in table.xpath('tbody/tr'):
            href = record.xpath('td[contains(@class, "al-c")]/a/@href').get()
            if href is not None:
                yield response.follow(href, self.parse_game)

    def parse_game(self, response):
        loader = GameResultLoader(item=GameResultItem(), response=response)
        loader.add_value('id', response.url.split('match_card_id=')[1])
        loader.add_xpath('game_day', '//div[@class="two-column-table-bottom"]/table/tbody/tr/td[1]/text()')
        loader.add_xpath('kickoff_time', '//div[@class="two-column-table-bottom"]/table/tbody/tr/td[2]/text()')
        loader.add_xpath('stadium_name', '//div[@class="two-column-table-bottom"]/table/tbody/tr/td[3]/text()')
        loader.add_xpath('spectators_num', '//div[@class="two-column-table-bottom"]/table/tbody/tr/td[4]/text()')
        loader.add_xpath('weather', '//div[@class="two-column-table-bottom"]/table/tbody/tr/td[5]/text()')
        loader.add_xpath('temperature', '//div[@class="two-column-table-bottom"]/table/tbody/tr/td[6]/text()')
        loader.add_xpath('humidity', '//div[@class="two-column-table-bottom"]/table/tbody/tr/td[7]/text()')

        loader.add_xpath('home_team_name', '//th[@id="team-name-l"]/a/text()')
        loader.add_xpath('home_team_id', '//th[@id="team-name-l"]/a/@href')
        loader.add_xpath('away_team_name', '//th[@id="team-name-r"]/a/text()')
        loader.add_xpath('away_team_id', '//th[@id="team-name-r"]/a/@href')

        loader.add_xpath('home_score', '//td[@class="score"][1]/text()')
        loader.add_xpath('away_score', '//td[@class="score"][2]/text()')
        loader.add_xpath('home_score_1st', '//td[@class="time"]/dl[1]/dd[@class="left-area"]/text()')
        loader.add_xpath('away_score_1st', '//td[@class="time"]/dl[1]/dd[@class="right-area"]/text()')
        loader.add_xpath('home_score_2nd', '//td[@class="time"]/dl[2]/dd[@class="left-area"]/text()')
        loader.add_xpath('away_score_2nd', '//td[@class="time"]/dl[2]/dd[@class="right-area"]/text()')

        loader.add_xpath('home_sh', '//dl[@class="score-board-base"][1]/dd/div[@class="left-score"]/text()')
        loader.add_xpath('home_ck', '//dl[@class="score-board-base"][2]/dd/div[@class="left-score"]/text()')
        loader.add_xpath('home_fk', '//dl[@class="score-board-base"][3]/dd/div[@class="left-score"]/text()')
        loader.add_xpath('away_sh', '//dl[@class="score-board-base"][1]/dd/div[@class="right-score"]/text()')
        loader.add_xpath('away_ck', '//dl[@class="score-board-base"][2]/dd/div[@class="right-score"]/text()')
        loader.add_xpath('away_fk', '//dl[@class="score-board-base"][3]/dd/div[@class="right-score"]/text()')

        yield loader.load_item()
