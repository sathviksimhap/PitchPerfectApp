from scamp import *
from data import *
from functions import *
from tkinter import *

DARK_THEME = "#1e1e1e"
DARK_BUTTON = "#3e3e42"
WHITE_BUTTON_TEXT = "#ffffff"
FONT = ("Agency FB", 48)

scale = get_scale()
question = gen_question(scale, 3)

# while True:
#     n = input()
#     if n == "0":
#         break
#     if n == "2":
#         print(question["names"])
#     else:
#         play_question(question)

############################################UI##################################

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
create_button = Button(text="Create", fg=WHITE_BUTTON_TEXT, font=FONT, command=create_button_clicked)
create_button.config(padx=30, pady=30, bg=DARK_THEME)
create_button.place(relx=0.65, rely=0.25, anchor=CENTER)

#Play button
play_button = Button(text="Play", fg=WHITE_BUTTON_TEXT, font=FONT, command=play_button_clicked)
play_button.config(width=8, padx=30, pady=30, bg=DARK_THEME)
play_button.place(relx=0.85, rely=0.25, anchor=CENTER)

#Notes input
notes_input = Text(height=2, width=22, bg=DARK_THEME, fg=WHITE_BUTTON_TEXT, font=FONT)
notes_input.place(relx=0.75, rely=0.5, anchor=CENTER)

#Submit button
submit_button = Button(text="Submit", fg=WHITE_BUTTON_TEXT, font=FONT, command=submit_button_clicked)
submit_button.config(width=10, padx=30, pady=30, bg=DARK_THEME)
submit_button.place(relx=0.75, rely=0.75, anchor=CENTER)


window.mainloop()