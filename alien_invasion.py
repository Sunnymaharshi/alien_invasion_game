import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
     # Initialize game and create a screen object.
     pygame.init()
     setting=Settings()
     screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
     pygame.display.set_caption("Alien Invasion")
     # Make the Play button.
     play_button = Button(setting, screen, "Play")
     # Create an instance to store game statistics and scoreboard.
     stats = GameStats(setting)
     sb = Scoreboard(setting, screen, stats)
     # Make a ship, a group of bullets, and a group of aliens.
     ship=Ship(setting,screen)
     bullets = Group()
     aliens = Group()
     # Create the fleet of aliens.
     gf.create_fleet(setting, screen, ship, aliens)

     
     # Start the main loop for the game.
     while True:
          # Watch for keyboard and mouse events.
          gf.check_events(setting, screen, stats, sb, play_button, ship,aliens, bullets)
          if stats.game_active:
               ship.update()
               gf.update_bullets(setting, screen, stats, sb, ship, aliens, bullets)
               gf.update_aliens(setting, screen, stats, sb, ship, aliens, bullets)
          gf.update_screen(setting, screen, stats, sb, ship, aliens, bullets, play_button)
          
         
         
         
         

    
     
run_game()
