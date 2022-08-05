import const
from models.game_result import GameResult

def main():
    print(const.GAME_RESULT_DATA_BASE_PATH)

    game_result = GameResult()
    print(game_result.get_classname())

if __name__ == '__main__':
    main()
