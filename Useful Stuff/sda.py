import customtkinter as ctk

app = ctk.CTk()
app.geometry("200x400")

# The trick: set from_ to the high value and to to the low value
inverted_slider = ctk.CTkSlider(
    app, 
    from_=100, 
    to=0, 
    orientation="vertical",
    command=lambda v: print(f"Value: {v}")
)
inverted_slider.pack(pady=50, expand=True)

# Set the initial position to "top" (which is now 0)
inverted_slider.set(0)

app.mainloop()