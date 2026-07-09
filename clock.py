import tkinter as tk
import time

root = tk.Tk()
root.configure(bg="black")

# gui
def apply_regular():
    clock_label.configure(bg="black", fg="#FFFFFF")
    date_label.configure(bg="black", fg="#FFFFFF")
    button_label.configure(bg="black",fg="#FFFFFF")

def apply_Matrix_Terminal():
    clock_label.configure(bg="black", fg="#00FF66")
    date_label.configure(bg="black", fg="#00FF66")
    button_label.configure(bg="black",fg="#00FF66")

def apply_Cyber_Ice():
    clock_label.configure(bg="black", fg="#00E5FF")
    date_label.configure(bg="black", fg="#00E5FF")
    button_label.configure(bg="black",fg="#00E5FF")

def apply_Stealth_Ember():
    clock_label.configure(bg="black", fg="#FF3B30")
    date_label.configure(bg="black", fg="#FF3B30")
    button_label.configure(bg="black",fg="#FF3B30")


def apply_Midnight_Amber():
    clock_label.configure(bg="black", fg="#FF9100")
    date_label.configure(bg="black", fg="#FF9100")
    button_label.configure(bg="black",fg="#FF9100")

def apply_Ultraviolet():
    clock_label.configure(bg="black", fg="#CC66FF")
    date_label.configure(bg="black", fg="#CC66FF")
    button_label.configure(bg="black",fg="#CC66FF")

def apply_Liquid_Mercury():
    clock_label.configure(bg="black", fg="#E0E0E0")
    date_label.configure(bg="black", fg="#E0E0E0")
    button_label.configure(bg="black",fg="#E0E0E0")

sidebar_pannel = tk.Frame(root, width=250,bg="#121212",cursor="hand2")
sidebar_pannel.pack(side="right",fill="y")
sidebar_pannel.pack_propagate(False)

theme_window_label = tk.Label(sidebar_pannel, text="Themes", font=("Trebuchet MS",25),bg="#121212" ,fg="white")
theme_window_label.pack(side="top",padx=15,pady=20, fill="x")

theme_button_label = tk.Button(sidebar_pannel, text="24:00:00", font=("Digital-7",25), bg="black", fg="#FFFFFF",command=apply_regular)
theme_button_label.pack(side="top",pady=20, fill="x")

theme_button_label = tk.Button(sidebar_pannel, text="24:00:00", font=("Digital-7",25), bg="black", fg="#00FF66", command=apply_Matrix_Terminal)
theme_button_label.pack(side="top", pady=20, fill="x")

theme_button_label = tk.Button(sidebar_pannel, text="24:00:00", font=("Digital-7",25), bg="black", fg="#00E5FF", command=apply_Cyber_Ice)
theme_button_label.pack(side="top", pady=20, fill="x")

theme_button_label = tk.Button(sidebar_pannel, text="24:00:00", font=("Digital-7",25), bg="black", fg="#FF3B30", command=apply_Stealth_Ember)
theme_button_label.pack(side="top", pady=20, fill="x")

theme_button_label = tk.Button(sidebar_pannel, text="24:00:00", font=("Digital-7",25), bg="black", fg="#FF9100", command=apply_Midnight_Amber)
theme_button_label.pack(side="top", pady=20, fill="x")

theme_button_label = tk.Button(sidebar_pannel, text="24:00:00", font=("Digital-7",25), bg="black", fg="#CC66FF", command=apply_Ultraviolet)
theme_button_label.pack(side="top", pady=20, fill="x")

theme_button_label = tk.Button(sidebar_pannel, text="24:00:00", font=("Digital-7",25), bg="black", fg="#E0E0E0", command=apply_Liquid_Mercury)
theme_button_label.pack(side="top", pady=20, fill="x")

# logic
def date():
    current_date = time.strftime("%B %d, %Y")
    date_label.configure(text=f"{current_date}")
    date_label.pack()

is24hr_time=False
def switch_time():
    global is24hr_time
    if is24hr_time is True:
        current24hr_time = time.strftime("%H:%M:%S")
        clock_label.configure(text=f"{current24hr_time}")
        clock_label.after(1000, switch_time)
    else:
        current12hr_time = time.strftime("%I:%M:%S %p")
        clock_label.configure(text=f"{current12hr_time}")
        clock_label.after(1000, switch_time)

def toggle():
    global is24hr_time
    if is24hr_time is not True:
        is24hr_time = True
        button_label.configure(text="12 hr")
    else:
        is24hr_time = False
        button_label.configure(text="24 hr")

window_label = tk.Label(root, text="Digital-Clock", font=("Impact",50) , bg="black", fg="white")
window_label.pack(side="top",padx=20, pady=50)

clock_container = tk.Frame(root, bg="black")
clock_container.pack(pady=10)

date_label = tk.Label(root, text="", font=("Century Gothic",20), bg="black", fg="white")
date_label = tk.Label(clock_container, text="", font=("Century Gothic",20), bg="black", fg="white")
date_label.pack(pady=10)

clock_label = tk.Label(root, text="", anchor="center",width=12, font=("Digital-7",100),bg="black", fg="white")
clock_label = tk.Label(clock_container, text="", anchor="center", width=12, font=("Digital-7",100),bg="black", fg="white")
clock_label.pack(pady=10)

button_label = tk.Button(root, text="24hr",font=("Century Gothic",25) ,bg="#1c1c1c", fg="white", command=toggle)
button_label = tk.Button(clock_container, text="24hr", font=("Courier New",25) ,bg="#1c1c1c", fg="white", command=toggle)
button_label.pack(pady=10)

date()
switch_time()
root.mainloop()