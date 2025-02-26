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

# Global Variables

question = {"notes": [], "names": []}
scale = {"key": "", "octave": -1, "notes": []}

#####################################Functions#######################################

def get_rand_key():
    global notes_list
    return choice(notes_list)

def get_scale(key=get_rand_key(), mode = "easy"):
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
    question["names "] = answers

def play_question():
    notes = question["notes"]

    s = Session()
    piano = s.new_part("piano")

    for i in range(3):
        piano.play_note(60, 0, 1)
        for note in notes:
            piano.play_note(note, 1, 1)

def create_button_clicked():
    get_scale()
    gen_question()

def play_button_clicked():
    if question["notes"]: play_question()
    else: messagebox.showinfo("Click \"New Question\" Button", "Please Create a Question Before Clicking the \"Play\" Button")

def submit_button_clicked():
    user_answer = notes_input.get()
    print(user_answer)




# while True:
#     n = input()
#     if n == "0":
#         break
#     if n == "2":
#         print(question["names"])
#     else:
#         play_question(question)

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

#Notes label
notes_string = ""
notes_label = Label(text="Notes:"+notes_string, fg=WHITE_BUTTON_TEXT, font=FONT)
notes_label.config(width=20, padx=30, pady=30, bg=DARK_THEME)
notes_label.place(relx=0.15, rely=0.2, anchor=CENTER)

# Scale label
scale_string = ""
scale_label = Label(text="Scale:"+scale_string, fg=WHITE_BUTTON_TEXT, font=FONT)
scale_label.config(width=20, padx=30, pady=30, bg=DARK_THEME)
scale_label.place(relx=0.15, rely=0.8, anchor=CENTER)

#Create button
create_button = Button(text="New Question", fg=WHITE_BUTTON_TEXT, font=FONT, command=create_button_clicked)
create_button.config(padx=30, pady=30, bg=DARK_THEME)
create_button.place(relx=0.65, rely=0.25, anchor=CENTER)

#Play button
play_button = Button(text="Play", fg=WHITE_BUTTON_TEXT, font=FONT, command=play_button_clicked)
play_button.config(width=8, padx=30, pady=30, bg=DARK_THEME)
play_button.place(relx=0.85, rely=0.25, anchor=CENTER)

#Notes input
notes_input = Entry(width=22, bg=DARK_THEME, fg=WHITE_BUTTON_TEXT, font=FONT)
notes_input.place(relx=0.75, rely=0.5, anchor=CENTER)

#Submit button
submit_button = Button(text="Submit", fg=WHITE_BUTTON_TEXT, font=FONT, command=submit_button_clicked)
submit_button.config(width=10, padx=30, pady=30, bg=DARK_THEME)
submit_button.place(relx=0.75, rely=0.75, anchor=CENTER)


window.mainloop()