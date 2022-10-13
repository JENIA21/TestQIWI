from celery_app.task import game_loop
from game_of_life.game_logic import CellGrid

cells = CellGrid(50, 50)
game_loop(cells=cells)
