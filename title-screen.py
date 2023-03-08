from PPlay.window import *
from PPlay.sprite import *
from tittle_snail import Follow_mouse

game_loop = Window(1366, 786)
snail_title = Sprite('images\snail.png')
snail_title.set_position(1366 - snail_title.width, 786 - snail_title.height)
play_button = Sprite('assets\play_button.png')
play_button.x = 918
play_button.y = 430
# SPD_sec = 10

while True:
    game_loop.set_background_color([0,155,13])
    game_loop.set_title('Everlasting Escape')
    game_loop.draw_text('Everlasting Escape', 683, 393, size=50, color=(0,0,0), font_name='Arial', bold=True, italic=False)
    play_button.draw()
    # snail_title.move_x(SPD_sec * game_loop.delta_time())
    Follow_mouse(game_loop,snail_title)
    snail_title.draw()
    if game_loop.get_mouse().is_over_object(play_button) and game_loop.get_mouse().is_button_pressed(1):
        # animar mouse hover no play
        game_loop.close()
    game_loop.update()