from data import *
from random import *
from scamp import *

def get_rand_key():
    global notes_list
    return choice(notes_list)

def get_scale(key=get_rand_key(), mode = "easy"):
    global notes_freq

    start_scale = randint(0,1)
    note = notes_freq[key][start_scale]

    playable_notes = [note]
    for i in range(modes[mode]):
        for i in range(2):
            note+=2
            playable_notes.append(note)
        note += 1
        playable_notes.append(note)
        for i in range(3):
            note+=2
            playable_notes.append(note)
        note += 1
        playable_notes.append(note)

    new_scale = {
        "key": key,
        "octave": start_scale+1,
        "notes": playable_notes
    }

    return new_scale

def gen_question(scale, length = 3):
    notes = scale["notes"]
    questions = choices(notes, k = length)

    answers = []
    for note in questions:
        answers.append(notes_list[note % 12])

    question = {
        "notes": questions,
        "names": answers
    }

    return question

def play_question(question):
    notes = question["notes"]

    s = Session()
    piano = s.new_part("piano")

    for i in range(3):
        piano.play_note(60, 0, 1)
        for note in notes:
            piano.play_note(note, 1, 1)

def create_button_clicked():
    pass

def play_button_clicked():
    pass

def submit_button_clicked():
    pass

