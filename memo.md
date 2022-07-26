# 取得するデータ
## [試合詳細データ](https://data.j-league.or.jp/SFMS02)
| name | description | acquisition method |
|------|-------------|--------------------|
| game_id | 試合のID | URLの`match_card_id`パラメータの値 |
| game_day | 試合日の日付 | div.two-column-table-bottom > table > tbody > tr > td[0] |
| kickoff_time | キックオフ時刻 | div.two-column-table-bottom > table > tbody > tr > td[1] |
| stadium_name | スタジアム名 | div.two-column-table-bottom > table > tbody > tr > td[2] |
| spectators_num | 観客数 | div.two-column-table-bottom > table > tbody > tr > td[3] |
| weather | 天候 | div.two-column-table-bottom > table > tbody > tr > td[4] |
| temperature | 気温 | div.two-column-table-bottom > table > tbody > tr > td[5] |
| humidity | 湿度 | div.two-column-table-bottom > table > tbody > tr > td[6] |
| home | ホームチームのID | チームリンク内の`/profile/`前部 |
| away | アウェーチームのID | チームリンク内の`/profile/`前部 |
| home_score | ホームチームの得点 |  |
| home_score_1st | ホームチームの前半の得点 |  |
| home_score_2nd | ホームチームの後半の得点 |  |
| home_sh | ホームチームのシュート数 |  |
| home_ck | ホームチームのコーナーキック数 |  |
| home_fk | ホームチームのフリーキック数 |  |
| away_score | アウェーチームの得点 |  |
| away_score_1st | アウェーチームの前半の得点 |  |
| away_score_2nd | アウェーチームの後半の得点 |  |
| away_sh | アウェーチームのシュート数 |  |
| away_ck | アウェーチームのコーナーキック数 |  |
| away_fk | アウェーチームのフリーキック数 |  |

