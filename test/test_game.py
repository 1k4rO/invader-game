from game.bullet import Bullet
from invader_game import InvaderGame
from game.settings import Settings
from game.ship import Ship

ig = InvaderGame()
settings = Settings()
bullet = Bullet(ig)
ship = Ship(ig)

def test_bullet_speed():
    bullet.y = 100
    bullet.update()
    assert 100 - settings.bullet_speed == bullet.y
    
def test_right_ship_movement():
    ship.x = 50
    ship.moving_right = True
    ship.update()
    ship.moving_right = False
    assert 50+settings.ship_speed == ship.x

def test_left_ship_movement():
    ship.x = 50
    ship.moving_left = True
    ship.update()
    ship.moving_left = False
    assert 50-settings.ship_speed == ship.x


def test_left_ship_movement_out_screen():
    ship.x = 0
    ship.rect.left = 0
    ship.moving_left = True
    ship.update()
    ship.moving_left = False
    assert 0 == ship.x

def test_right_ship_movement_out_screen():
    ship.rect.right = ship.screen_rect.right
    ship.x = 50000
    ship.moving_right = True
    ship.update()
    ship.moving_right = False
    assert ship.x == 50000