import tkinter as tk
from tkinter import *
import random
#----------------------
# WINDOW SETUP -----------------------
win = tk.Tk()
win.geometry("750x750")
win.title("Number Guess Challenge")


# VARIABLES -----------------------
# The computer secretly picks a number
num = random.randint(1, 50)

# Tkinter variables for automatic updates
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()

# Starting values
hint.set("Welcome! Try guessing a number between 1 and 50.")
score.set(5)
final_score.set(score.get())


# -----------------------
# GAME LOGIC
#----------------------
def fun():
    """Main game function that checks the user’s guess."""
    
    try:
        x = int(guess.get())  # Make sure the user entered a number
    except:
        hint.set("Please enter a valid NUMBER 😊")
        return

    # Update score display
    final_score.set(score.get())

    if score.get() > 0:

        # Out-of-range guess
        if x < 1 or x > 50:
            hint.set("Oops! Enter a number only between 1 and 50.")
            score.set(score.get() - 1)
            final_score.set(score.get())

        # Correct guess
        elif x == num:
            hint.set("🎉 Amazing! You guessed it correctly! 🎉")
            score.set(score.get() - 1)
            final_score.set(score.get())

        # Too low
        elif x < num:
            hint.set("Too low! Try a slightly higher number 👍")
            score.set(score.get() - 1)
            final_score.set(score.get())

        # Too high
        elif x > num:
            hint.set("That’s high! Try a lower number 👇")
            score.set(score.get() - 1)
            final_score.set(score.get())

    else:
        hint.set("❌ You’re out of chances! Better luck next time!")


# -----------------------
# GUI DESIGN -----------------------
Label(
    win,
    text='Guess the Secret Number!',
    font=("Courier", 28)
).place(relx=0.5, rely=0.09, anchor=CENTER)

Entry(
    win, textvariable=guess, width=3,
    font=('Ubuntu', 50), relief=GROOVE
).place(relx=0.5, rely=0.3, anchor=CENTER)

Button(
    win, width=8, text='CHECK',
    font=('Courier', 25), command=fun,
    relief=GROOVE, bg='light blue'
).place(relx=0.5, rely=0.5, anchor=CENTER)

Entry(
    win, textvariable=hint, width=50,
    font=('Courier', 15), relief=GROOVE, bg='orange'
).place(relx=0.5, rely=0.7, anchor=CENTER)

Label(
    win, text='Score (Out of 5)', font=("Courier", 25)
).place(relx=0.3, rely=0.85, anchor=CENTER)

Entry(
    win, textvariable=final_score, width=2,
    font=('Ubuntu', 24), relief=GROOVE
).place(relx=0.61, rely=0.85, anchor=CENTER)

 #-----------------------
# START THE GAME -----------------------
win.mainloop()