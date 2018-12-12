from tkinter import *

class Ball ():
    def __init__(self, screen, x1, y1, x2, y2):
        self.screen = game_screen
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.deltax = 3
        self.deltay = 5
        self.screen_width = self.screen.winfo_width()
        self.screen_height = self.screen.winfo_height()
        self.ball = game_screen.create_oval(self.x1, self.y1, self.x2, self.y2, fill="white")

    def move_ball(self):
        pos = self.screen.coords(self.ball)
        if pos[0] <= 0:
            self.deltax = - 1 * self.deltax
        if pos[2] >= self.screen_width:
            self.deltax = - 1 * self.deltax
        if pos[1] <= 0:
            self.deltay = - 1 * self.deltay
        if pos[3] >= self.screen_height:
            self.deltay = - 1 * self.deltay
        self.screen.move(self.ball, self.deltax, self.deltay)
        self.screen.after(20, self.move_ball)


# Initialisation of the components
screen = Tk()
screen.title('Pong')
screen_width = 1000
screen_height = 600
game_screen = Canvas(screen, width = screen_width, height = screen_height, bd = 0, highlightthickness = 0, bg = 'black')
quit_button = Button(screen, text = 'Quit', command= screen.destroy, width = 20)
game_ball = Ball(game_screen, screen_width/2 - 5, screen_height/2 - 5, screen_width/2 + 5, screen_height/2 + 5)

# Component's placements
game_screen.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
quit_button.grid(row = 1, column = 1)

# Collision's gestion



# Infinite loop
game_ball.move_ball()
screen.mainloop()
