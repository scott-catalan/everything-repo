'''
# Project Creation Date: 10:23:16 PM, 2/19/2026
'''

import customtkinter as ctk

def button_clicked(index):
    print(f"Button {index} clicked!")

app = ctk.CTk()
app.geometry("300x400")
app.title("Scrollable Buttons Example")

# Scrollable frame
scroll_frame = ctk.CTkScrollableFrame(app, width=280, height=380)
scroll_frame.pack(pady=10, padx=10)

# Make a list of button labels
button_labels = [f"Option {i}" for i in range(1, 21)]

# Populate buttons
for i, label in enumerate(button_labels):
    btn = ctk.CTkButton(scroll_frame, text=label, command=lambda i=i: button_clicked(i))
    btn.pack(pady=5, padx=10, fill="x")

app.mainloop()