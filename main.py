from tkinter import *
import pandas
import random
FIRST_LANGUAGE = "French"
SECOND_LANGUAGE = "English"
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def is_known():
    try:
        data.remove(current_card)
    except ValueError:
        canvas.itemconfig(language_label, text="The")
        canvas.itemconfig(word_label, text="End")
    else:
        button_pressed()
        new_data = pandas.DataFrame(data)
        new_data.to_csv("data/words_to_learn.csv", index=False)


def flip_the_card():
    global current_card
    canvas.itemconfig(language_label, text=SECOND_LANGUAGE, fill="white")
    canvas.itemconfig(word_label, text=current_card[SECOND_LANGUAGE], fill="white")
    canvas.itemconfig(card_current_image, image=card_back_image)


# -----------------------------Change display word after button pressed-----------
def button_pressed():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_current_image, image=card_front_image)
    canvas.itemconfig(language_label, text=FIRST_LANGUAGE, fill="black")
    canvas.itemconfig(word_label, text=current_card[FIRST_LANGUAGE], fill="black")
    flip_timer = window.after(3000, func=flip_the_card)


# -------------------------------Import data from csv file------------------------
try:
    read_data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    try:
        read_data = pandas.read_csv("data/french_words.csv")
    except FileNotFoundError:
        print("Data file not found.")
    else:
        data = read_data.to_dict(orient="records")

else:
    data = read_data.to_dict(orient="records")


# -------------------------------UI generate--------------------------------------
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_the_card)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=button_pressed)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_current_image = canvas.create_image(400, 260, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
language_label = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

button_pressed()

window.mainloop()