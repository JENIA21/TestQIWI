import time

from celery_app.celery import celery
from config import Config
from game_of_life.game_logic import CellGrid
from models import GameData, session


# @celery.task


def game_loop(cells):
    cells.circulate_count()
    cells.circulate_rule()
    output = []
    for i in cells.cells:
        field_string = ""
        for j in i:
            field_string += str(j)
        output.append(field_string + '\n')
    save = GameData(output_data=''.join(output))
    session.add(save)
    session.commit()
    time.sleep(Config.SLEEP_PERIOD)
    game_loop(cells=cells)
