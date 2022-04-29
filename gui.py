import random_quiz_generator
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from quiz_data import capitals
from quiz_data import elements

root = Tk()
root.title('Self-quiz')
root.geometry("300x300")
textboxes = tk.Canvas(root, width=430, height=330, relief='raised')
textboxes.pack()
label = tk.Label(root, text='Choose your topic')
textboxes.create_window(213, 104, window=label)
# entry box
e = tk.Entry(root)
textboxes.create_window(303, 146, window=e)


def retrieve_input():
    input = textboxes.get

    label1 = tk.Label(root, text=input)
    textboxes.create_window(200, 230, window=label1)


btn1 = Button(root, text=" +")
btn1.pack(side=TOP)
btn2 = Button(root, text=" - ")
btn2.pack(side=RIGHT)

button1 = tk.Button(text="Choose topic", command=retrieve_input)
THREE = 3
topic = retrieve_input
list(topic.get())
correctAnswer = list[topic.keys()]
wrongAnswers = list(topic.values())
del wrongAnswers[wrongAnswers.index(correctAnswer)]  # remove the right answer
wrongAnswers = random.sample(wrongAnswers, THREE)
answerOptions = wrongAnswers + [correctAnswer]
random.shuffle(answerOptions)
answer1 = StringVar(root, wrongAnswers)
answer2 = StringVar(root, wrongAnswers)

correctAnswer = tk.StringVar()
for question in answerOptions:
    r = ttk.Radiobutton(
        root,
        text=[0],
        value=[1],
        variable=correctAnswer
    )
    r.pack(fill='x', padx=5, pady=5)

root.mainloop()
