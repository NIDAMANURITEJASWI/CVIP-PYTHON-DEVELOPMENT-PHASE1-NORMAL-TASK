import tkinter as tk
class Calculator:
    def __init__(self, ma):
        self.ma = ma
        ma.geometry("450x480")
        ma.configure(bg='#ada692')
        ma.title("Calculator")
        # Entry field for displaying the result
        s.r = tk.Text(ma, width=25, height=2, font=('Arial', 16,'bold'))
        s.r.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        s.r.config(bg="#faeded", fg='black', borderwidth=5, relief='ridge', pady=10)
        # Create buttons for the calculator
        s.c("7", 2, 0)
        s.c("8", 2, 1)
        s.c("9", 2, 2)
        s.c("/", 2, 3)
        s.c("4", 3, 0)
        s.c("5", 3, 1)
        s.c("6", 3, 2)
        s.c("*", 3, 3)
        s.c("1", 4, 0)
        s.c("2", 4, 1)
        s.c("3", 4, 2)
        s.c("-", 4, 3)
        s.c("0", 5, 0)
        s.c(".", 5, 1)
        s.c("C", 5, 2)
        s.c("+", 5, 3)
        s.c("=", 6, 0, 1, 4)
        s.c("⌫", 1, 4)  # Backspace button
        #Bind the BackSpace key event to the delete_last() function
        self.ma.bind('<BackSpace>', lambda event: self.delete_last())
    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = tk.Button(self.ma, text=text, width=5, height=2, font=('Arial', 16,'bold'), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)
        button.config(bg="#a18948",fg='#e3df6f')
    def button_click(self, text):
        if text == "=":
            # Evaluate the expression entered by the user
            try:
                result = eval(s.r.get("1.0", tk.END))
            except:
                result = "Error"
            s.r.delete("1.0", tk.END)
            s.r.insert("1.0", result)
        elif text == "C":
            # Clear the entry field
            s.r.delete("1.0", tk.END)
        elif text == "⌫":  # Handle backspace button
            self.delete_last()
        else:
            # Append the clicked button's text to the entry field
            s.r.insert(tk.END, text)
    def delete_last(self):
        # Delete the last character from the entry field
        current = s.r.get("1.0", tk.END)
        if len(current) > 1:
            s.r.delete("end-2c")
r= tk.Tk()
calculator = Calculator(r)
r.mainloop()
