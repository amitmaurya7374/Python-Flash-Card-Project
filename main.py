"""In this project we will built a FLash app"""
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

# creating a window
window = Tk()
window.title("flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR, highlightthickness=0)

card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
card_canvas.create_image(400, 260, image=front_img)
card_canvas.grid(row=0, column=0, columnspan=2)

card_canvas.create_text(400,330,font="Ariel 40 italic bold",
                        text="trouve")
card_canvas.create_text(400,263,font="Ariel 40 italic bold",
                        text="French")

cross_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_button_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

check_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_button_image, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
