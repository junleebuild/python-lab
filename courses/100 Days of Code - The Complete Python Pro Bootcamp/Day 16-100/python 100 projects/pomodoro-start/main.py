from tkinter import *
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
REPS = 0
CHECK_MARK = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS == 0 or REPS == 2 or REPS == 4 or REPS == 6:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        count_down(work_sec)
        REPS+=1
    elif REPS == 7:
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        count_down(long_break_sec)
        REPS = 0
    else:
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        count_down(short_break_sec)
        REPS += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min == 0:
        count_min = "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if REPS % 2 == 0 and REPS != 0:
            global CHECK_MARK
            CHECK_MARK += "✔"
            check_mark.config(text=CHECK_MARK)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row= 0)

start_button = Button(text="Start",command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=3)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


window.mainloop()