import tkinter as tk
import time
import pyautogui
from tkinter import filedialog
from tkinter import ttk
import keyboard
from PIL import Image, ImageTk
file_path = ""
val=0.5

def clicking():
    global file_path
    click_speed = val_speed.get()
    time.sleep(10)
    if file_path:
        autof = pyautogui.locateOnScreen(file_path, confidence=val)
        print(autof)
        if autof is not None:
            while True:
                pyautogui.click(autof, button="left")
                time.sleep(click_speed)

def upload_file():
    global file_path
    selected_file = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
    if selected_file:
        file_path = selected_file
        print("Selected file:", file_path)
def standart_clicker():
    while True:
        mouse_pos = pyautogui.position()
        pyautogui.click(mouse_pos,button="left")
def get_translation(rus_text, eng_text):
    if language_var.get() == 1:
        return eng_text
    return rus_text
def open_popup():
    popup = tk.Toplevel(root)
    popup.title(get_translation("Помощь", "Help"))
    popup.geometry("1200x100")
    label = tk.Label(popup, text=get_translation("Для правильной работы используйте картинку формата png с обрезанными излишками, для запуска стандартного автокликера в реальном времени используйте клавишу F5",
                                                "To work correctly, use a png image with trimmed excesses, use the F5 key to run the standard auto clicker in real-time."))
    label.pack(pady=10)
    close_button = tk.Button(popup, text=get_translation("Закрыть", "Close"), command=popup.destroy)
    close_button.pack(pady=10)

root = tk.Tk()
root.title("AutoAutoClicker")
root.geometry("500x500")
language_var = tk.IntVar()
language_checkbox = tk.Checkbutton(root, text="English", variable=language_var, command=lambda: update_interface())
language_checkbox.pack(pady=10, anchor="nw")
button_soveti = tk.Button(root, text=get_translation("Помощь", "Help"), command=open_popup)
button_soveti.pack(pady=20, anchor="n")
button_start = tk.Button(root, text=get_translation("Запуск", "Start"), command=clicking)
button_start.pack(pady=20, anchor="center")
button_upload = tk.Button(root, text=get_translation("Загрузка изображения", "Upload Image"), command=upload_file)
button_upload.pack(pady=20, anchor="s")
val = tk.DoubleVar(value=0.5)
scale = ttk.Scale(root, orient="horizontal", length=100, from_=0.5, to=1, variable=val)
scale.pack(anchor="s")
label_scale = tk.Label(root, text=get_translation("Различие картинки (0,5 to 1)", "Image Difference (0.5 to 1)"), textvariable=val)
label_scale.pack(pady=20, anchor="center")
keyboard.add_hotkey('f5', standart_clicker)
val_speed = tk.DoubleVar(value=0.1)  # Начальная скорость клика
speed_scale = ttk.Scale(root, orient="horizontal", length=100, from_=0.1, to=1, variable=val_speed)
speed_scale.pack(pady=10, anchor="s")
label_speed_scale = ttk.Label(root,text = get_translation("Интервал между кликами", "Interval between clicking"))
label_speed_scale.pack(pady=20,anchor="s")
label_speed_tip = ttk.Label(root,textvariable=val_speed)
label_speed_tip.pack(pady=20,anchor="s")
def update_interface():
    button_start.config(text=get_translation("Запуск", "Start"))
    button_upload.config(text=get_translation("Загрузка изображения", "Upload Image"))
    label_scale.config(text=get_translation("Различие картинки (0,5 to 1)", "Image Difference (0.5 to 1)"))
    button_soveti.config(text=get_translation("Помощь", "Help"))
    label_speed_scale.config(text=get_translation("Интервал между кликами", "Interval between clicking"))

root.mainloop()