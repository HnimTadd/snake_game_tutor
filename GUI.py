import pygame
from snakeGame import *
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
class SnakeUI:
    def __init__(self, cfg):
        self.pygame = pygame
        self.pygame.init()
        self.pygame.display.set_caption('Snake game')
        self.game_over = False
        self.dis_width = cfg['width']
        self.dis_height = cfg['height']
        self.dis = self.pygame.display.set_mode((self.dis_width, self.dis_height))
        self.font_style = self.pygame.font.SysFont('bahnschrift', 25)
        self.score_style = self.pygame.font.SysFont('comicsansms', 30)
        self.block = cfg['block']
        self.initBorder()

    def initBorder(self):
        padding_top = 70
        padding_bot = 20
        padding_left_right = 10
        self.x_min = round((padding_left_right - self.block) / 10.0) * 10.0
        self.y_min = round((padding_top - self.block) / 10.0) * 10.0
        self.x_max = round((self.dis_width - padding_left_right - self.block) / 10.0) * 10.0 + self.block
        self.y_max = round((self.dis_height - padding_bot - self.block) / 10.0) * 10.0

    def drawBorder(self):
        padding_top = 70
        padding_bot = 20
        padding_left_right = 10
        self.x_min_min = round((padding_left_right - self.block) / 10.0) * 10.0
        self.yx_min_min = round((padding_top - self.block) / 10.0) * 10.0
        self.x_min_max = round((self.dis_width - padding_left_right - self.block) / 10.0) * 10.0 + self.block
        self.yx_min_max = round((self.dis_height - padding_bot - self.block) / 10.0) * 10.0
        self.pygame.draw.rect(self.dis, green, [self.x_min, self.y_min, self.block, self.y_max-self.y_min])
        self.pygame.draw.rect(self.dis, red, [self.x_max, self.y_min, self.block, self.y_max - self.y_min + self.block])
        self.pygame.draw.rect(self.dis, green, [self.x_min, self.y_min, self.x_max - self.x_min, self.block])
        self.pygame.draw.rect(self.dis, red, [self.x_min, self.y_max, self.x_max - self.x_min, self.block])

    def print_message(self, msg,  color= black):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width/2 - mesg.get_width()/2, self.dis_height/2 - mesg.get_height()/2])
    
    def print_score(self, score, color = red):
        value = self.score_style.render("Your Score: " + str(score), True, color)
        self.dis.blit(value, [0,0])
    
    def print_snake(self, blocks):
        for block in blocks:
            self.pygame.draw.rect(self.dis, black, [block[0], block[1], self.block, self.block])
        
    def print_food(self, food):
        self.pygame.draw.rect(self.dis, green, [food[0], food[1], self.block, self.block])
    
    def print_lose(self, score):
        self.dis.fill(blue)
        msg = "You Lost! Press C-Play again or Q-Quit"
        self.print_message(msg, red)
        self.print_score(score)
        self.pygame.display.update()


    def display(self, blocks,food, score):
        self.dis.fill(blue)
        self.drawBorder()
        self.print_score(score)
        self.print_food(food)
        self.print_snake(blocks)
        self.pygame.display.update()
