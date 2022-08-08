import tkinter as tk
from tkinter import messagebox
import random as rd

window = tk.Tk()
window.geometry("900x800")
window.resizable(width=False, height=False)

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
computer_choice = ["Rock", "Paper", "Scissors"]
c_v = rd.choice(computer_choice)


def reset_game():
    btn["state"] = "active"
    btn1["state"] = "active"
    btn2["state"] = "active"
    entry.delete(0, "end")


# Disable the Button
def button_disable():
    btn["state"] = "disable"
    btn1["state"] = "disable"
    btn2["state"] = "disable"


def is_rock():
    if c_v == "Rock":
        # entry.insert(tk.END, "draw")
        messagebox.showinfo(title="Draw", message=f"Draw!! {Rock}")
    elif c_v == "Scissors":
        # entry.insert(tk.END, "Player win")
        messagebox.showinfo(title="You win!!", message=f"You win {Scissors} \ncomputer chose {Scissors}")
    else:
        # entry.insert(tk.END, "You lose!!")
        messagebox.showinfo(title="You lose!!", message=f"You lose {Rock} \ncomputer chose {Paper}")
    button_disable()


def is_paper():
    if c_v == "Paper":
        # entry.insert(tk.END, "draw")
        messagebox.showinfo(title="Draw", message=f"Draw!! {Paper}")
    elif c_v == "Scissors":
        # entry.insert(tk.END, "Player win")
        messagebox.showinfo(title="You lose!!", message=f"You lose {Paper} \ncomputer chose {Scissors}")
    else:
        # entry.insert(tk.END, "You win!!")
        messagebox.showinfo(title="You win!!", message=f"You win! {Paper} \ncomputer chose {Rock}")
    button_disable()


def is_scissors():
    if c_v == "Scissors":
        # entry.insert(tk.END, "draw")
        messagebox.showinfo(title="Draw", message=f"Draw!! {Scissors}")
    elif c_v == "Paper":
        # entry.insert(tk.END, "Player win")
        messagebox.showinfo(title="You win!!", message=f"You win! {Scissors} \ncomputer chose {Paper}")
    else:
        # entry.insert(tk.END, "Computer wins")
        messagebox.showinfo(title="You lose!!", message=f"You lose! {Scissors} \ncomputer chose {Rock}")
    button_disable()


label = tk.Label(text="""

██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
""")

label.pack()
empty_label = tk.Label()
empty_label1 = tk.Label()
empty_label2 = tk.Label()

empty_label.pack()
empty_label1.pack()
empty_label2.pack()
entry = tk.Entry(width=50)
entry.pack()

btn = tk.Button(text="Rock", bg="brown", width=8, command=is_rock)
btn1 = tk.Button(text="Paper", bg="white", width=8, command=is_paper)
btn2 = tk.Button(text="Scissors", bg="orange", width=8, command=is_scissors)
btn3 = tk.Button(text="Reset game", width=10, command=reset_game)
btn.place(x=250, y=440)
btn1.place(x=400, y=440)
btn2.place(x=550, y=440)
btn3.place(x=390, y=540)

window.mainloop()
