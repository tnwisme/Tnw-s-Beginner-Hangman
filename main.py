import tkinter as tk
from tkinter import NW
import random as r
from PIL import ImageTk, Image

line_number = r.randint(1, 999)

f = open("wordlist.txt", 'r')
lines = f.readlines()
f.close()

guessed_letter = []
raw_word = lines[line_number-1]
word = raw_word.replace("\n", "")
strike = 0


def guesse():
    display = ''
    guessing_letter = guess_input.get()
    guessed_letter.append(guessing_letter)
    global strike

    for letter in word:
        if letter in guessed_letter:
            display += letter
        else:
            display += '-'
    title_label.configure(text=display)

    if guessing_letter not in word:
        strike += 1
        strike_label.configure(text=(str(strike)))
        global img_path
        global img
        global tk_img

        if strike == 1:
            img_path = 'Hangman_Strike/1.png'
        elif strike == 2:
            img_path = 'Hangman_Strike/2.png'
        elif strike == 3:
            img_path = 'Hangman_Strike/3.png'
        elif strike == 4:
            img_path = 'Hangman_Strike/4.png'
        elif strike == 5:
            img_path = 'Hangman_Strike/5.png'
        elif strike == 6:
            img_path = 'Hangman_Strike/6.png'

        img = Image.open(img_path)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=NW, image=tk_img)
        canvas.pack()


window = tk.Tk()
window.title("Hangman By TNW")
window.minsize(width=200, height=200)

title_label = tk.Label(master=window, text='-'*len(word), pady=20, font=("", 20))
title_label.pack()

strike_label = tk.Label(master=window, text=(str(strike)), pady=5)
strike_label.pack()

guess_input = tk.Entry(master=window)
guess_input.pack()

guess_button = tk.Button(master=window, text="Guess", command=guesse)
guess_button.pack()

canvas = tk.Canvas(window, height=100, width=100)
img_path = 'Hangman_Strike/no_strike.png'
img = Image.open(img_path)
tk_img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, anchor=NW, image=tk_img)
canvas.pack()

window.mainloop()
