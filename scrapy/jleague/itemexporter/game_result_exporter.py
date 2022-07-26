from scrapy.exporters import CsvItemExporter

FIELDS_TO_EXPORT = [
    'id',
    'game_day',
    'kickoff_time',
    'stadium_name',
    'spectators_num',
    'weather',
    'temperature',
    'humidity',
    'home_team_name',
    'home_team_id',
    'away_team_name',
    'away_team_id',
    'home_score',
    'home_score_1st',
    'home_score_2nd',
    'away_score',
    'away_score_1st',
    'away_score_2nd',
    'home_sh',
    'home_ck',
    'home_fk',
    'away_sh',
    'away_ck',
    'away_fk',
]


class GameResultCsvItemExporter(CsvItemExporter):
    def __init__(self, file, include_headers_line=True, join_multivalued=',', **kwargs):
        super().__init__(file, include_headers_line, join_multivalued, fields_to_export=FIELDS_TO_EXPORT)
