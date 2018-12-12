from tkinter import *

class Ball ():
    def __init__(self, screen, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.screen = screen
        self.ball = game_screen.create_oval(self.x1, self.y1, self.x2, self.y2, fill="white")

    def move_ball(self):
        deltax = 2
        deltay = 1
        self.screen.move(self.ball, deltax, deltay)
        self.screen.after(20, self.move_ball)


# Initialisation of the components
screen = Tk()
screen.title('Pong')
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
game_screen = Canvas(screen, width = screen_width, height = screen_height, bg = 'black')
quit_button = Button(screen, text = 'Quit', command= screen.destroy, width = 20)
game_ball = Ball(game_screen, screen_width/2, screen_height/2, screen_width/2 + 10, screen_height/2 + 10)

# Component's placements
game_screen.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
quit_button.grid(row = 1, column = 1)


# Infinite loop
game_ball.move_ball()
screen.mainloop()
