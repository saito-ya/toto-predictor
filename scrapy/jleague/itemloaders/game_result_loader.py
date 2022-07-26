from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
from jleague.utils.number_util import convert_int, convert_float
from jleague.utils.string_util import strip_comma, strip_percent

def get_team_id(element):
    return element.split('/')[4]


class GameResultLoader(ItemLoader):
    id_out = TakeFirst()

    game_day_out = TakeFirst()

    kickoff_time_in = MapCompose(str.strip)
    kickoff_time_out = TakeFirst()

    stadium_name_in = MapCompose(str.strip)
    stadium_name_out = TakeFirst()

    spectators_num_in = MapCompose(str.strip, strip_comma, convert_int)
    spectators_num_out = TakeFirst()

    weather_in = MapCompose(str.strip)
    weather_out = TakeFirst()

    temperature_in = MapCompose(str.strip, convert_float)
    temperature_out = TakeFirst()

    humidity_in = MapCompose(str.strip, strip_percent, convert_float)
    humidity_out = TakeFirst()

    home_team_name_in = MapCompose(str.strip)
    home_team_name_out = TakeFirst()

    home_team_id_in = MapCompose(str.strip, get_team_id)
    home_team_id_out = TakeFirst()

    away_team_name_in = MapCompose(str.strip)
    away_team_name_out = TakeFirst()

    away_team_id_in = MapCompose(str.strip, get_team_id)
    away_team_id_out = TakeFirst()

    home_score_in = MapCompose(str.strip, convert_int)
    home_score_out = TakeFirst()

    home_score_1st_in = MapCompose(str.strip, convert_int)
    home_score_1st_out = TakeFirst()

    home_score_2nd_in = MapCompose(str.strip, convert_int)
    home_score_2nd_out = TakeFirst()

    away_score_in = MapCompose(str.strip, convert_int)
    away_score_out = TakeFirst()

    away_score_1st_in = MapCompose(str.strip, convert_int)
    away_score_1st_out = TakeFirst()

    away_score_2nd_in = MapCompose(str.strip, convert_int)
    away_score_2nd_out = TakeFirst()

    home_sh_in = MapCompose(str.strip, convert_int)
    home_sh_out = TakeFirst()

    home_ck_in = MapCompose(str.strip, convert_int)
    home_ck_out = TakeFirst()

    home_fk_in = MapCompose(str.strip, convert_int)
    home_fk_out = TakeFirst()

    away_sh_in = MapCompose(str.strip, convert_int)
    away_sh_out = TakeFirst()

    away_ck_in = MapCompose(str.strip, convert_int)
    away_ck_out = TakeFirst()

    away_fk_in = MapCompose(str.strip, convert_int)
    away_fk_out = TakeFirst()

