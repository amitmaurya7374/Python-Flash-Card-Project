"""In this project we will built a FLash app"""

import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


# print(to_learn[0]["French"])

# ------------------------Reading data-----------------------------------------------------------#
def next_card():
    """Show a card"""
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    random_word_french = current_card["French"]
    card_canvas.itemconfig(front_img, image=front_img)
    card_canvas.itemconfig(card_title, text="French", )
    card_canvas.itemconfig(card_word, text=f"{random_word_french}", )
    window.after(3000, flip_card)


def flip_card():
    """FLip a card after 3 sec"""
    # random_word_dict = random.choice(to_learn)
    print(current_card)
    random_word_english = current_card["English"]
    card_canvas.itemconfig(background_img, image=back_image)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=f"{random_word_english}", fill="white")


#

# ------------------------------------------- creating a window----------------------------------#
window = Tk()
window.title("flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, flip_card, )
card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file="images/card_back.png")
background_img = card_canvas.create_image(400, 260, image=front_img)
card_canvas.grid(row=0, column=0, columnspan=2)

card_word = card_canvas.create_text(400, 330, font="Ariel 40 italic bold",
                                    text="word")
card_title = card_canvas.create_text(400, 263, font="Ariel 40 italic bold",
                                     text="Title")

cross_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_button_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
