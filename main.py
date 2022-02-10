import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps in [1, 3, 5, 7]:
        title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
    elif reps in [2, 4, 6]:
        title.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    elif reps == 8:
        title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = int(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

title = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 38,))
title.grid(column=2, row=1)

start_button = tkinter.Button(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = tkinter.Button(text="Reset", bg=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=3)

check_mark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_mark.grid(row=4, column=2)

window.mainloop()