from genericpath import isfile
import tkinter as tk
from tkinter import Place, filedialog, Text
import os

root = tk.Tk()
apps = list()

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        temp_apps = f.read()
        temp_apps = temp_apps.split(',')
        apps = [x for x in temp_apps if x.strip()]


def add_app():
    for widget in frame.winfo_children():
        widget.destroy()
    file_name = filedialog.askopenfilename(
        initialdir='/',
        title='Select a file',
        filetypes=(
            ('executables', '*.exe'),
            ('all files', '*.*')
        )
    )
    apps.append(file_name)
    print(f'file:{file_name}')

    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()


def clear_apps():
    with open('save.txt', 'w') as f:
        f.close()
    apps.clear()
    for widget in frame.winfo_children():
        widget.destroy()


def run_apps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=500, width=700, bg='#2c2c2c')
canvas.pack()

frame = tk.Frame(root, bg='#fff')
frame.place(relheight=.8, relwidth=.8, relx=.1, rely=.1)

open_file = tk.Button(
    root,
    text='Open file',
    padx=10,
    pady=5,
    fg='white',
    bg='#2c2c2c',
    command=add_app
)

open_file.pack()

run_apps = tk.Button(
    root,
    text='Run Apps',
    padx=10,
    pady=5,
    fg='white',
    bg='#2c2c2c',
    command=run_apps
)

run_apps.pack()

clear_button = tk.Button(
    root,
    text='Clear',
    padx=10,
    pady=5,
    fg='white',
    bg='crimson',
    command=clear_apps
)

clear_button.pack()

for app in apps:
    lable = tk.Label(frame, text=app)
    lable.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
