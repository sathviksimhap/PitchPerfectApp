from scamp import *
from random import *
from tkinter import *
from tkinter import messagebox

#######################################Data###########################################

notes_freq = {
    "C": [48, 60, 72, 84, 96],
    "C#": [49, 61, 73, 85, 97],
    "D": [50, 62, 74, 86, 98],
    "D#": [51, 63, 75, 87, 99],
    "E": [52, 64, 76, 88, 100],
    "F": [53, 65, 77, 89, 101],
    "F#": [54, 66, 78, 90, 102],
    "G": [55, 67, 79, 91, 103],
    "G#": [56, 68, 80, 92, 104],
    "A": [57, 69, 81, 93, 105],
    "A#": [58, 70, 82, 94, 106],
    "B": [59, 71, 83, 95, 107]
}

notes_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

modes = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}

answer_status = ["Wrong!", "Almost!", "Correct!"]

colours = ["red", "yellow", "green"]

# Global Variables

question = {"notes": [], "names": []}
scale = {"key": "", "octave": -1, "notes": []}

#####################################Functions#######################################

def get_rand_key():
    global notes_list
    return choice(notes_list)

def new_scale(key="", mode ="easy"):
    if key == "Random":
        key = get_rand_key()

    start_scale = randint(0,1)
    note = notes_freq[key][start_scale]

    playable_notes = [note]
    for i in range(modes[mode]):
        for j in range(2):
            note+=2
            playable_notes.append(note)
        note += 1
        playable_notes.append(note)
        for k in range(3):
            note+=2
            playable_notes.append(note)
        note += 1
        playable_notes.append(note)

        scale["key"] = key
        scale["octave"] = start_scale + 1
        scale["notes"] = playable_notes

def gen_question(length = 3):
    notes = scale["notes"]
    questions = choices(notes, k = length)

    answers = []
    for note in questions:
        answers.append(notes_list[note % 12])

    question["notes"] = questions
    question["names"] = answers

def play_question():
    notes = question["notes"]

    s = Session()
    piano = s.new_part("piano")

    for i in range(3):
        piano.play_note(60, 0, 1)
        for note in notes:
            piano.play_note(note, 1, 1)

def check_answer(answer):
    if answer == question["names"]: return 2

    relative_answer = []
    for note in answer:
        relative_answer.append(notes_freq[note][0])
    relative_question = []
    for note in question["names"]:
        relative_question.append(notes_freq[note][0])

    relative = []
    i = 0
    while i < len(relative_question):
        relative.append(relative_question[i] - relative_answer[i])
        i+=1

    check = all(x == relative[0] for x in relative)

    if check: return 1
    else: return 0

def create_button_clicked():
    key = default_scale_menu_value.get()
    new_scale(key)
    gen_question()
    play_button.config(fg="Green")
    correct_label.config(text="")
    print("Question:", question["names"])

def play_button_clicked():
    if question["notes"]: play_question()
    else: messagebox.showinfo("Click \"New Question\" Button", "Please Create a Question Before Clicking the \"Play\" Button")

def submit_button_clicked():
    user_answer = notes_input.get()
    user_answer = user_answer.upper()
    user_answer = user_answer.split()
    notes_input.delete(0, END)

    check = check_answer(user_answer)
    correct_label.config(text=answer_status[check], fg=colours[check])

    print("user_answer:", user_answer)
    print("check", check)

############################################UI##################################

DARK_THEME = "#1e1e1e"
DARK_BUTTON = "#3e3e42"
WHITE_BUTTON_TEXT = "#ffffff"
FONT = ("Agency FB", 48)

# Window
window = Tk()
window.title("PitchPerfect")
window.minsize(width=1920, height=1080)
window.config(padx=30, pady=30, bg=DARK_THEME)

# Title label
title_label = Label(text="Pitch-Perfect",fg=WHITE_BUTTON_TEXT, font=("Showcard Gothic", 96))
title_label.config(padx=30, pady=30, bg=DARK_THEME)
title_label.place(relx=0.5, rely=0.02, anchor=CENTER)

# Scale label
scale_label = Label(text="Scale:", fg=WHITE_BUTTON_TEXT, font=FONT)
scale_label.config(width=20, padx=10, pady=10, bg=DARK_THEME)
scale_label.place(relx=0.15, rely=0.25, anchor=CENTER)

#Scale Menu
default_scale_menu_value = StringVar()
default_scale_menu_value.set("Random")

scale_menu_options = ["Random"] + notes_list
scale_menu = OptionMenu(window, default_scale_menu_value, *scale_menu_options)
scale_menu.config(width=8, padx=10, pady=10, bg=DARK_THEME, fg=WHITE_BUTTON_TEXT, font=FONT)
scale_menu.place(relx=0.27, rely=0.25, anchor=CENTER)

dropdown_menu = scale_menu["menu"]
dropdown_menu.config(font=("Agency FB", 24))

#Correct Label
correct_label = Label(text="", fg=WHITE_BUTTON_TEXT, font=("Agency FB", 96))
correct_label.config(width=20, padx=10, pady=10, bg=DARK_THEME)
correct_label.place(relx=0.2, rely=0.8, anchor=CENTER)

#Create button
create_button = Button(text="New Question", fg=WHITE_BUTTON_TEXT, font=FONT, command=create_button_clicked)
create_button.config(padx=10, pady=10, bg=DARK_THEME)
create_button.place(relx=0.65, rely=0.25, anchor=CENTER)

#Play button
play_button = Button(text="Play", fg="Red", font=FONT, command=play_button_clicked)
play_button.config(width=8, padx=10, pady=10, bg=DARK_THEME)
play_button.place(relx=0.85, rely=0.25, anchor=CENTER)

#Notes input
notes_input = Entry(width=22, bg=DARK_THEME, fg=WHITE_BUTTON_TEXT, font=FONT)
notes_input.place(relx=0.75, rely=0.5, anchor=CENTER)

#Submit button
submit_button = Button(text="Submit", fg=WHITE_BUTTON_TEXT, font=FONT, command=submit_button_clicked)
submit_button.config(width=10, padx=10, pady=10, bg=DARK_THEME)
submit_button.place(relx=0.75, rely=0.75, anchor=CENTER)


window.mainloop()