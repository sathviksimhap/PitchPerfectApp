from scamp import *
from data import *
from functions import *
from tkinter import *

BG_YELLOW = "#f7f5dd"

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
window.config(padx=30, pady=30, bg=BG_YELLOW)

# Title label
title_label = Label(text="Pitch-Perfect",fg="#6495ED", font=("Showcard Gothic", 96))
title_label.config(padx=30, pady=30, bg=BG_YELLOW)
title_label.place(relx=.5, rely=.02, anchor=CENTER)

#Notes label
notes_string = ""
notes_label = Label(text="Notes:"+notes_string, font=("Magneto", 48))
notes_label.config(padx=30, pady=30, bg=BG_YELLOW)
notes_label.place(relx=.2, rely=.2, anchor=CENTER)

# Scale label
scale_string = ""
scale_label = Label(text="Scale:"+scale_string, font=("Magneto", 48))
scale_label.config(padx=30, pady=30, bg=BG_YELLOW)
scale_label.place(relx=.2, rely=.4, anchor=CENTER)

#Create button
create_button = Button(text="Create", font=("Magneto", 30), command=create_button_clicked)
create_button.config(padx=30, pady=30, bg=BG_YELLOW)
create_button.place(relx=.5, rely=.02, anchor=CENTER)

#Play button
play_button = Button(text="Play", font=("Magneto", 30), command=play_button_clicked)
play_button.config(padx=30, pady=30, bg=BG_YELLOW)
play_button.place(relx=.5, rely=.02, anchor=CENTER)

#Notes input
notes_input = Entry(width=10)
notes_input.place(relx=.5, rely=.02, anchor=CENTER)


window.mainloop()