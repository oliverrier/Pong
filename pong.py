from tkinter import *

# Initialisation of the components
screen = Tk()
screen.title('Pong')
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
game_screen = Canvas(screen, width = screen_width, height = screen_height, bg = 'black')
quit_button = Button(screen, text = 'Quit', command= screen.destroy, width = 20)
ball = game_screen.create_oval(50, 50, 100, 100)

# Component's placements
game_screen.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
quit_button.grid(row = 1, column = 1)
ball.grid_location()


# Infinite loop
screen.mainloop()
