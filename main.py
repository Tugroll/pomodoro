import math
from tkinter import *
import time
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
# --------------------------- TIMER RESET ------------------------------- #


def timer_reset():

    global reps
    start_button.config(state="normal")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label["text"] = "Timer"
    check_marks["text"] = ""
    reps = 0
    click_count = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    reps += 1
    start_button.config(state="disabled")

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        my_label["text"] = "Long Break"
    elif reps % 2 == 0:
        count_down(short_break)
        my_label["text"] = "Short Break"
    else:
        count_down(work_sec)
        my_label["text"] = "Work !"



    print(reps)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/ 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks["text"] += "✓"

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

my_label = Label(text="Timer", font=("Arial", 25, "bold"), bg=YELLOW, fg=GREEN)
my_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00", fill="white",font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",command=timer_reset)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=("Arial", 30, "bold"))
check_marks.grid(column=1, row=2)


window.mainloop()
