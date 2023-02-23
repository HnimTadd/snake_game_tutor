import pygame
import enum
import random
from GUI import SnakeUI
class Buttons():
    def __init__(self, pygame):
        self.pygame = pygame
        self.Down = self.pygame.K_DOWN
        self.Up = self.pygame.K_UP
        self.Left = self.pygame.K_LEFT
        self.Right = self.pygame.K_RIGHT
        self.Quit = self.pygame.QUIT
        self.Q = self.pygame.K_q
        self.Continue = self.pygame.K_c

class snakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block = 10
        self.xAcc = 1
        self.yAcc = 0
        self.score = 0
        cfg = {
            'block': self.block,
            'width': self.width,
            'height': self.height
        }
        self.UI = SnakeUI(cfg)
        self.clock = self.UI.pygame.time.Clock()
        self.Buttons = Buttons(self.UI.pygame)

    def get_dis_width(self):
        return self.width
    
    def get_dis_heigt(self):
        return self.height

    def getRandomPoint(self):
        x = round(random.randrange(self.UI.x_min, self.UI.x_max - self.block)/10.0)*10.0
        y = round(random.randrange(self.UI.y_min, self.UI.y_max - self.block) /10.0)*10.0
        return (x, y)
    
    def resetGame(self):
        self.speed = 10
        self.body = [self.getRandomPoint()]
        self.headX, self.headY = self.body[0]
        self.score = 0
        self.game_over = False
        self.length = 1
    def endGame(self):
        exit()
    
    def moveUp(self):
        if self.xAcc != 0 and self.yAcc != 1:
            self.xAcc = 0
            self.yAcc = -1

    def moveDown(self):
        if self.xAcc != 0 and  self.yAcc != -1:
            self.xAcc = 0
            self.yAcc = 1

    def moveLeft(self):
        if  self.xAcc != 1 and self.yAcc != 0:
            self.xAcc = -1
            self.yAcc = 0 
    def moveRight(self):
        if self.xAcc != -1 and self.yAcc != 0:
            self.xAcc = 1
            self.yAcc = 0 

    def play(self):
        self.resetGame()
        food = self.getRandomPoint()
        while not self.game_over:
            for event in self.UI.pygame.event.get():
                if event.type == self.UI.pygame.KEYDOWN:
                    pressed_key = event.key
                # TODO: Control the snake's movement by using the (UP | DOWN | LEFT | RIGHT) arrow keys. 
                # TODO:If the key down is pressed, the snakehead's direction must be down. The same is true for other keys.
                # TODO: The snake game's four implemented methods—moveUp, moveDown, moveLeft, and moveRight—can be used to change the snake's direction of travel. 
                # Example: method moveDown causes the snake to move downward. 
                # You have to check if pressed_key variable is the arrow key, then the snake will move in that arrow's direction.
                # Example: if press_key == self.Buttons.Down:
                #               {handle snake moveDown code}

                # Hint: you can call snake game's methods by using self.[method-name]()
                # Example: if you want to call moveDown method, you have to type self.moveDown()

            newHeadX, newHeadY = self.headX + self.block*self.xAcc, self.headY + self.block*self.yAcc

            # TODO: if snake head position is out of display area, the game should end.
            # Hint: check if self.headX >= self.width or self.headX < 0
            # or self.headY >= self.height or self.headX < 0
            # If game is over, just set self.game_over = True

            if newHeadX >= self.UI.x_max or newHeadX< self.UI.x_min or newHeadY >= self.UI.y_max or newHeadY < self.UI.y_min:
                self.game_over = True

            # TODO: Check if snake hit itself
            for block in self.body:
                if (newHeadX, newHeadY) == block:
                    self.game_over = True
            self.body.insert(0, (newHeadX, newHeadY))
            self.headX, self.headY = newHeadX, newHeadY
            if len(self.body) > self.length:
                self.body.pop()
            if (newHeadX, newHeadY) == food:
                food = self.getRandomPoint()
                self.length += 1
                self.score += 1
                self.speed += 0.5
            self.clock.tick(self.speed)
            self.UI.display(self.body, food, self.score)
        while True:
            for event in self.UI.pygame.event.get():
                if event.type == self.UI.pygame.KEYDOWN:
                    if event.key == self.Buttons.Q:
                        self.endGame()
                    if event.key == self.Buttons.Continue:
                        self.play()
            self.UI.print_lose(self.score)

            



