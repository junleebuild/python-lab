from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
COUNTRY_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# ---------------------------- DATA ------------------------------- #
try:
    data = pandas.read_csv("words_to_learn.csv")
    data_dict = pandas.DataFrame.to_dict(data, orient="records")

except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = pandas.DataFrame.to_dict(data, orient="records")

finally:
    current_card = {}

# ---------------------------- SYSTEM MECHANISM ------------------------------- #
def replace_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_country, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)

    flip_timer = window.after(3000, change_the_canvas)

def change_the_canvas():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(canvas_country, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")

def known_card():
    data_dict.remove(current_card)
    if len(data_dict) == 0:
        messagebox.showinfo(title="Done!", message="You've learned all the words!")
        window.quit()
    else:
        new_data = pandas.DataFrame(data_dict)
        new_data.to_csv("words_to_learn.csv", index=False)
        replace_card()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("flash card memory")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func= change_the_canvas)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas_country = canvas.create_text(400, 150, text="", font=COUNTRY_FONT, fill="black")
canvas_word = canvas.create_text(400, 263, text="", font=WORD_FONT, fill="black")
canvas.grid(column=0, row=0, columnspan=2)

wrong_mark = PhotoImage(file="./images/wrong.png", )
wrong_mark_button = Button(image=wrong_mark, highlightthickness=0, bg=BACKGROUND_COLOR, command=replace_card)
wrong_mark_button.grid(column=0, row=1)

right_mark = PhotoImage(file="./images/right.png")
right_mark_button = Button(image=right_mark, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_card)
right_mark_button.grid(column=1, row=1)

replace_card()



window.mainloop()