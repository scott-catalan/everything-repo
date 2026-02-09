from color_tool_logic import validate_hex, scatter_color, hex_to_hsl
import customtkinter as ctk
import colorsys

#----------------------|Initial|----------------------#

app = ctk.CTk()
app.geometry("400x500")
app.resizable(False, False)

container = ctk.CTkFrame(app)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

screens = {}

def add_screen(name):
    frame = ctk.CTkFrame(container)
    frame.grid(row=0, column=0, sticky="nsew")
    screens[name] = frame
    return frame

def show_screen(name):
    screens[name].tkraise()

#----------------------|Constants & Appearance|----------------------#

CORNER_RADIUS = 5
UNIVERSAL_FONT = ctk.CTkFont(family="Unispace", size=22, weight="bold")
UNIVERSAL_FONT2 = ctk.CTkFont(family="Unispace", size=14, weight="bold")

ctk.set_appearance_mode("dark")

#----------------------|Scatter Results Screen|----------------------#

screen_scatter_results = add_screen("scatter_results")

#----------------------|Scatter Configure Screen|----------------------#

screen_scatter = add_screen("scatter")

def initialize_sliders(hex):
    h, s, l = hex_to_hsl(hex)
    s_pos_max = 100 - s
    s_neg_max = s
    l_pos_max = 100 - l
    l_neg_max = l

    h_pos_slider.configure(from_=0, to=180, number_of_steps=1800)
    s_pos_slider.configure(from_=0, to=max(s_pos_max, 0.01), number_of_steps=max(int(s_pos_max * 10), 1))
    l_pos_slider.configure(from_=0, to=max(l_pos_max, 0.01), number_of_steps=max(int(l_pos_max * 10), 1))

    h_neg_slider.configure(from_=180, to=0, number_of_steps=1800)
    s_neg_slider.configure(from_=max(s_neg_max, 0.01), to=0, number_of_steps=max(int(s_neg_max * 10), 1))
    l_neg_slider.configure(from_=max(l_neg_max, 0.01), to=0, number_of_steps=max(int(l_neg_max * 10), 1))

    h_pos_slider.set(0)
    s_pos_slider.set(0)
    l_pos_slider.set(0)
    h_neg_slider.set(0)
    s_neg_slider.set(0)
    l_neg_slider.set(0)

def hpos_feedback(event):
    h_pos_val.configure(text=f"{event:.1f}")
def hneg_feedback(event):
    prefix = "-" if event > 0 else ""
    h_neg_val.configure(text=f"{prefix}{event:.1f}")
def lpos_feedback(event):
    l_pos_val.configure(text=f"{event:.1f}")
def lneg_feedback(event):
    prefix = "-" if event > 0 else ""
    l_neg_val.configure(text=f"{prefix}{event:.1f}")
def spos_feedback(event):
    s_pos_val.configure(text=f"{event:.1f}")
def sneg_feedback(event):
    prefix = "-" if event > 0 else ""
    s_neg_val.configure(text=f"{prefix}{event:.1f}")

h_pos_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=hpos_feedback)
h_pos_slider.place(relx=0.14, rely=0.3, anchor="center")
h_neg_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=hneg_feedback)
h_neg_slider.place(relx=0.26, rely=0.3, anchor="center")
l_pos_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=lpos_feedback)
l_pos_slider.place(relx=0.44, rely=0.3, anchor="center")
l_neg_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=lneg_feedback)
l_neg_slider.place(relx=0.56, rely=0.3, anchor="center")
s_pos_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=spos_feedback)
s_pos_slider.place(relx=0.74, rely=0.3, anchor="center")
s_neg_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=sneg_feedback)
s_neg_slider.place(relx=0.86, rely=0.3, anchor="center")

h_pos_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
h_pos_val.place(relx=0.14, rely=0.5, anchor="center")
h_neg_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
h_neg_val.place(relx=0.26, rely=0.5, anchor="center")
l_pos_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
l_pos_val.place(relx=0.44, rely=0.5, anchor="center")
l_neg_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
l_neg_val.place(relx=0.56, rely=0.5, anchor="center")
s_pos_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
s_pos_val.place(relx=0.74, rely=0.5, anchor="center")
s_neg_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
s_neg_val.place(relx=0.86, rely=0.5, anchor="center")

generate = ctk.CTkButton(screen_scatter, text="GENERATE", font=UNIVERSAL_FONT)
generate.place(relx=0.3, rely=0.6, anchor="center")

#----------------------|Hex Input Home Screen|----------------------#

screen_input = add_screen("input")

def limit_length(user_input):
    if user_input.startswith("#"):
        user_input = user_input[1:]
    return len(user_input) <= 6
def initiate_scatter():
    hex = user_input_entry.get()
    if hex.startswith("#"):
        hex = hex[1:]
    if len(hex) == 6 and validate_hex(hex):
        initialize_sliders(hex)
        show_screen("scatter")
def validation_check(event):
    hex = user_input_entry.get()
    if hex.startswith("#"):
        hex = hex[1:]
    if len(hex) == 6:
        if validate_hex(hex):
            validation_label.configure(text="Valid hex code")
        else:
            validation_label.configure(text="Invalid hex code")
    else:
        validation_label.configure(text="")
def update_color_preview(event):
    hex = user_input_entry.get()
    if hex.startswith("#"):
        hex = hex[1:]
    if len(hex) == 6 and validate_hex(hex):
        color_preview.configure(fg_color=f"#{hex}")
    else: 
        color_preview.configure(fg_color="#ffffff")

vcmd = app.register(limit_length)

color_preview = ctk.CTkLabel(screen_input, text="", width=180, height=180, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
color_preview.place(relx=0.3, rely=0.6, anchor="center")

scatter_button = ctk.CTkButton(screen_input, text="SCATTER", font=UNIVERSAL_FONT, command=initiate_scatter)
scatter_button.place(relx=0.75, rely=0.45, anchor="center")
other_button = ctk.CTkButton(screen_input, text="OTHER", font=UNIVERSAL_FONT) #other buttons for eventual future function additions (maybe complementary colors or whatever)
other_button.place(relx=0.75, rely=0.55, anchor="center")
other_button = ctk.CTkButton(screen_input, text="OTHER", font=UNIVERSAL_FONT)
other_button.place(relx=0.75, rely=0.65, anchor="center")
other_button = ctk.CTkButton(screen_input, text="OTHER", font=UNIVERSAL_FONT)
other_button.place(relx=0.75, rely=0.75, anchor="center")

validation_label = ctk.CTkLabel(screen_input, text="", font=UNIVERSAL_FONT)
validation_label.place(relx=0.5, rely=0.2, anchor="center")

user_input_entry = ctk.CTkEntry(screen_input, placeholder_text="#808080", font=UNIVERSAL_FONT, corner_radius=CORNER_RADIUS, validate="key", validatecommand=(vcmd, "%P"))
user_input_entry.place(relx=0.5, rely=0.3, anchor="center")
user_input_entry.bind("<KeyRelease>", update_color_preview)
user_input_entry.bind("<KeyRelease>", validation_check)

#----------------------|Start Program|----------------------#

show_screen("input")
app.mainloop()