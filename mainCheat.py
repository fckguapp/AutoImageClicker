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
    time.sleep(10)
    if file_path:
        autof = pyautogui.locateOnScreen(file_path, confidence=val)
        print(autof)
        if autof is not None:
            while True:
                pyautogui.click(autof, button="left")

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
    # Проверка состояния чекбокса для выбора языка
    if language_var.get() == 1:  # 1 соответствует английскому
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

# Переменная для чекбокса изменения языка
language_var = tk.IntVar()

# Чекбокс для переключения языка
language_checkbox = tk.Checkbutton(root, text="English", variable=language_var, command=lambda: update_interface())
language_checkbox.pack(pady=10, anchor="nw")

# Кнопка запуска
button_start = tk.Button(root, text=get_translation("Запуск", "Start"), command=clicking)
button_start.pack(pady=20, anchor="center")

# Кнопка загрузки изображения
button_upload = tk.Button(root, text=get_translation("Загрузка изображения", "Upload Image"), command=upload_file)
button_upload.pack(pady=20, anchor="s")

# Ползунок для настройки
val = tk.DoubleVar(value=0.5)
scale = ttk.Scale(root, orient="horizontal", length=100, from_=0.5, to=1, variable=val)
scale.pack(anchor="s")

# Метка для ползунка
label_scale = tk.Label(root, text=get_translation("Различие картинки (0,5 to 1)", "Image Difference (0.5 to 1)"), textvariable=val)
label_scale.pack(pady=20, anchor="center")

# Кнопка помощи
button_soveti = tk.Button(root, text=get_translation("Помощь", "Help"), command=open_popup)
button_soveti.pack(pady=20, anchor="se")

# Горячая клавиша для стандартного кликера
keyboard.add_hotkey('f5', standart_clicker)

def update_interface():
    # Обновление интерфейса для отражения нового языка
    button_start.config(text=get_translation("Запуск", "Start"))
    button_upload.config(text=get_translation("Загрузка изображения", "Upload Image"))
    label_scale.config(text=get_translation("Различие картинки (0,5 to 1)", "Image Difference (0.5 to 1)"))
    button_soveti.config(text=get_translation("Помощь", "Help"))

root.mainloop()