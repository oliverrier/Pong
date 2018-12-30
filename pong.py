from tkinter import *


class Ball ():
    def __init__(self, screen, x1, y1, x2, y2):
        self.screen = game_screen
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.deltax = 3
        self.deltay = 3
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = game_screen.create_oval(
            self.x1, self.y1, self.x2, self.y2, fill="white")

    def move_ball(self):
        position = self.screen.coords(self.ball)
        if position[0] <= 0 or position[2] >= self.screen_width:
            self.deltax = - self.deltax
        if position[1] <= 0 or position[3] >= self.screen_height:
            self.deltay = - self.deltay
        self.screen.move(self.ball, self.deltax, self.deltay)
        self.screen.after(20, self.move_ball)


class Player():
    def __init__(self, screen, position):
        self.screen = game_screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.deltay = 3
        self.paddle = game_screen.create_rectangle(
            position[0], position[1], position[2], position[3], fill='white')
    
    def move_paddle_up(self):
        postion = self.screen.coords(self.paddle)
        if position[1] == 0:
            self.deltay = 0
        self.screen.move(self.paddle, 0, - self.deltay)

    def move_paddle_down(self):
        postion = self.screen.coords(self.paddle)
        if postion[3] == self.screen_height:
            self.deltay = 0
        self.screen.move(self.paddle, 0, self.deltay)


# Initialisation of the components
screen = Tk()
screen.title('Pong')
screen_width = 1000
screen_height = 600
game_screen = Canvas(screen, width=screen_width,
                     height=screen_height, bg='black')
game_ball = Ball(game_screen, screen_width/2 - 5, screen_height /
                 2 - 5, screen_width/2 + 5, screen_height/2 + 5)
player_1 = Player(game_screen, [10, screen_height/2 - 25, 20, screen_height/2 + 25])
player_2 = Player(game_screen, [screen_width - 20, screen_height/2 - 25, screen_width - 10, screen_height/2 +25])
game_screen.pack()

# Component's placements
game_screen.grid(row=0, column=0, rowspan=2, columnspan=3)


# Infinite loop
game_ball.move_ball()
screen.bind()
screen.mainloop()
