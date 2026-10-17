from tkinter import *
from tkinter import messagebox
wd = Tk()
import random

def check_answer():
    player_answer = answer.get().strip().lower()
    correct_answer = riddles[current_riddle].strip().lower()

    if player_answer == correct_answer:
        messagebox.showinfo("Correct!", "Correct answer! Well done!")
        confetti()

    else:
        choice = messagebox.askyesno(
            "Wrong Answer",
            "Wrong answer!\n\n"
            "YES = Try again\n"
            "NO = Skip to the next riddle"
        )

        if choice:
            answer.delete(0, END)
            answer.focus_set()
        else:
            next_riddle()
riddles = {
    "What has keys but cannot open locks?": "piano",
    "What gets wetter the more it dries?": "towel",
    "What has hands but cannot clap?": "clock",
    "What has one eye but cannot see?": "needle",
    "What goes up but never comes down?": "your age",
    "What has many teeth but cannot bite?": "comb",
    "What can you catch but not throw?": "a cold",
    "What has a neck but no head?": "bottle",
    "What has cities but no houses?": "map",
    "What disappears when you say its name?": "silence",
    "What has four legs but cannot walk?": "table",
    "What belongs to you but others use it more?": "your name",
    "What can fill a room but takes up no space?": "light",
    "What has a head and a tail but no body?": "coin",
    "What gets bigger the more you take away?": "a hole",
    "What has words but never speaks?": "book",
    "What runs but never walks?": "river",
    "What has a thumb and four fingers but is not alive?": "glove",
    "What has a bed but never sleeps?": "river",
    "What has a bark but no bite?": "tree",
    "What can travel around the world while staying in one corner?": "stamp",
    "What has a face and two hands but no arms or legs?": "clock",
    "What has lots of eyes but cannot see?": "potato",
    "What can you break without touching it?": "promise",
    "What is always in front of you but cannot be seen?": "future",
    "What has a ring but no finger?": "telephone",
    "What has branches but no leaves?": "bank",
    "What comes down but never goes up?": "rain",
    "What has a spine but no bones?": "book",
    "What kind of room has no doors or windows?": "mushroom",
    "What has 13 hearts but no other organs?": "deck of cards",
    "What goes up and down but stays in the same place?": "stairs",
    "What has a tongue but cannot talk?": "shoe",
    "What can you hold without touching it?": "your breath",
    "What is full of holes but still holds water?": "sponge",
    "What has a head, a foot, and four legs?": "bed",
    "What is always coming but never arrives?": "tomorrow",
    "What starts with E, ends with E, and contains one letter?": "envelope",
    "What has many needles but cannot sew?": "pine tree",
    "What can fly without wings?": "time",
    "What has a crown but is not a king?": "tooth",
    "What has four wheels and flies?": "garbage truck",
    "What is black when clean and white when dirty?": "blackboard",
    "What has a heart that does not beat?": "artichoke",
    "What has an end but no beginning?": "stick",
    "What has no life but can die?": "battery",
    "What can you keep after giving it to someone?": "your word",
    "What has one head and one foot but no legs?": "bed",
    "What kind of tree fits in your hand?": "palm",
    "What has a lot of words but never tells a story?": "dictionary"
}

wd.title("Riddle Master")
wd.geometry("600x600")
wd.configure(bg="lightblue")


title = Label(
    wd,
    text="RIDDLE MASTER",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title.place(x=100, y=60, width=400, height=50)

random_riddle = random.choice(list(riddles.keys()))

riddle = Label(
    wd,
    text=random_riddle,
    font=("Arial", 16),
    bg="white",
    fg="black",
    wraplength=400
)
riddle.place(x=50, y=170, width=500, height=120)

answer = Entry(
    wd,
    font=("Arial", 16),
    justify="center"
)
current_riddle = random_riddle
bt = Button(
    wd,
    text="Submit Answer",
    font=("Arial", 14, "bold"),
    bg="darkblue",
    fg="white",
    command = check_answer
)
bt.place(x=175, y=410, width=250, height=50,)
def next_riddle():
    global current_riddle

    current_riddle = random.choice(list(riddles.keys()))
    riddle.config(text=current_riddle)
    answer.delete(0, END)


def confetti():
    pieces = []

    for i in range(30):
        piece = Label(
            wd,
            text="●",
            font=("Arial", random.randint(10, 18)),
            fg=random.choice([
                "red", "blue", "yellow",
                "green", "orange", "purple", "pink"
            ]),
            bg="lightblue"
        )
        piece.place(
            x=random.randint(10, 570),
            y=random.randint(-100, -10)
        )
        pieces.append({
            "label": piece,
            "x": int(piece.place_info()["x"]),
            "y": int(piece.place_info()["y"]),
            "speed": random.randint(4, 9)
        })

    def animate(step=0):
        for p in pieces:
            p["y"] += p["speed"]
            p["label"].place(x=p["x"], y=p["y"])

            if step > 12:
                p["label"].config(fg="lightblue")

        if step < 18:
            wd.after(80, lambda: animate(step + 1))
        else:
            for p in pieces:
                p["label"].destroy()

            next_riddle()

    animate()




bt.config(command=check_answer)
answer.place(x=100, y=330, width=400, height=45)



feedback = Label(
    wd,
    text="Good luck!",
    font=("Arial", 12),
    bg="lightblue",
    fg="darkblue"
)
feedback.place(x=100, y=480, width=400, height=30)








wd.mainloop()