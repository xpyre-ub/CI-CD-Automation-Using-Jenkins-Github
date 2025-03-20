import tkinter as tk

def on_click(button_text, entry_var):
    if button_text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)


# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right')
entry.pack(fill='both', ipadx=8, ipady=8, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    button_row = tk.Frame(frame)
    button_row.pack(side='top', fill='both', expand=True)
    for btn in row:
        button = tk.Button(button_row, text=btn, font=("Arial", 20), command=lambda b=btn: on_click(b, entry_var))
        button.pack(side='left', fill='both', expand=True, padx=5, pady=5)

root.mainloop()
