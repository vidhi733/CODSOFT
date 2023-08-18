import tkinter
from tkinter import messagebox
import random
import json

def generate_pw():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', '=', '_', '-', '/', '?', '\\', '.', ',', '<', '>', '"', '\'']
    pw_list = [random.choice(characters) for _ in range(25)]
    random.shuffle(pw_list)
    pw_str = ''.join(pw_list)
    password_output.delete(0, tkinter.END)
    password_output.insert(0, pw_str)

def find_pw():
    try:
        read_handler = open('usernames_and_passwords.json', 'r')
    except:
        messagebox.showinfo(message = "Can't search. No info stored yet.")
    else:
        json_dict = json.load(read_handler)
    

window = tkinter.Tk()
window.title('Password Manager')
window.config(padx = 35, pady = 35)


username_label = tkinter.Label(text = 'Username:')
username_label.grid(row = 2, column = 1)
username_input = tkinter.Entry(width = 38)
username_input.grid(row = 2, column = 2, columnspan = 2)

password_label = tkinter.Label(text = 'Password:')
password_label.grid(row = 3, column = 1)
password_output = tkinter.Entry(width = 27)
password_output.grid(row = 3, column = 2)
password_generator_button = tkinter.Button(text = 'Generate', command = generate_pw)
password_generator_button.grid(row = 3, column = 3)


window.mainloop()