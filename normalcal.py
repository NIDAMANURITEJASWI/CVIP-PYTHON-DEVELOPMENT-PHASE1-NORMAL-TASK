import tkinter as tk
def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)
window = tk.Tk()
window.geometry("300x400")
window.title("Calculator")
window.configure(bg="black")
screen = tk.StringVar()
entry = tk.Entry(window, textvar=screen, font=("Calibri light", 22), bd=9, insertwidth=3, width=13, justify="right")
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, font=("Calibri light", 22), relief="ridge", bd=4)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", button_click)
window.grid_rowconfigure(5, weight=1)
window.columnconfigure(4, weight=1)
window.mainloop()
