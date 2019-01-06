from tkinter import *

class Game():

    def __init__(self, score_limit, ball_speed):
        self.screen = game_screen
        self.score_limit = score_limit
        self.ball_speed = ball_speed
        self.ball_position = [screen_width/2 - 5, screen_height / 2 - 5, screen_width/2 + 5, screen_height/2 + 5]
        self.player1_position = [10, screen_height/2 - 25, 20, screen_height/2 + 25]
        self.player2_position = [screen_width - 20, screen_height/2 - 25, screen_width - 10, screen_height/2 + 25]


    def start(self):
        game_ball.move_ball()


    def move_paddle(self, event):
        key = event.keysym
        if key == "z":
            player_1.move_paddle_up()
        if key == "s":
            player_1.move_paddle_down()
        if key == "Up":
            player_2.move_paddle_up()
        if key == "Down":
            player_2.move_paddle_down()


class Ball ():
    def __init__(self, screen, position):
        self.screen = game_screen
        self.deltax = game.ball_speed
        self.deltay = game.ball_speed
        self.last_touched_by = None
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = game_screen.create_oval(
            position[0], position[1], position[2], position[3], fill="white")
        self.ball_position = self.screen.coords(self.ball)

    def move_ball(self):
        global game
        position = self.screen.coords(self.ball)
        if len(game_screen.find_overlapping(position[0], position[1], position[2], position[3])) == 2 and game_screen.find_overlapping(position[0], position[1], position[2], position[3])[1] == 2:
            self.last_touched_by = player_1
            self.deltax = - (self.deltax - 1)
        if len(game_screen.find_overlapping(position[0], position[1], position[2], position[3])) == 2 and game_screen.find_overlapping(position[0], position[1], position[2], position[3])[1] == 3:
            self.last_touched_by = player_2
            self.deltax = - (self.deltax + 1)
        if position[0] <= 0:
            self.stop_ball()
            player_2.score += 1
            self.screen.move(self.ball, screen_width/2 - 5 - position[0], screen_height / 2 - 5 - position[1])
            game.start()
            print(player_2.score)
        if position[2] >= screen_width:
            self.stop_ball()
            player_1.score += 1
            self.screen.move(self.ball, screen_width/2 - 5 - position[0], screen_height / 2 - 5 - position[1])
            game.start()
            print(player_1.score)
        if position[1] <= 0 or position[3] >= self.screen_height:
            self.deltay = - self.deltay
        self.screen.move(self.ball, self.deltax, self.deltay)
        self.screen.after(20, self.move_ball)
            
    def stop_ball(self):
        self.deltax = 0
        self.deltay = 0
        


class Player():
    def __init__(self, screen, position):
        self.screen = game_screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.deltay = 25
        self.score = 0
        self.paddle = game_screen.create_rectangle(
            position[0], position[1], position[2], position[3], fill='white')
        self.paddle_position = self.screen.coords(self.paddle)

    def move_paddle_up(self):
        if self.paddle_position[1] >= 0:
            self.screen.move(self.paddle, 0, - self.deltay)


    def move_paddle_down(self):
        if self.paddle_position[3] <= self.screen_height:
            self.screen.move(self.paddle, 0, self.deltay)


def raise_screen(screen):
    screen.tkraise()

# Initialisation of the components

screen = Tk()
screen.title('Pong')

screen_width = 1000
screen_height = 600

game_screen = Canvas(screen, width=screen_width,
                     height=screen_height, bg='black')
game = Game(5,3)
game_ball = Ball(game_screen, game.ball_position)
player_1 = Player(game_screen, game.player1_position)
player_2 = Player(game_screen, game.player2_position)
screen.bind("<Key>", game.move_paddle)

# Component's placements



game_screen.grid(row=0, column=0, sticky='nsew')
game.start()

# Infinite loop

screen.bind()
screen.mainloop()
