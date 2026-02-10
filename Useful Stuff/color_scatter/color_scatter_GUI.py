'''
# Project Creation Date: 6:21:32 PM, 2/8/2026
'''

from color_scatter_logic import validate_hex, scatter_color, hex_to_hsl
import customtkinter as ctk
import ctypes

#----------------------|Initial|----------------------#

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = ctk.CTk()
app.title("ColorScatter")
app.geometry("400x500")
app.resizable(False, False)

app.after(201, lambda : app.iconbitmap("C:/Scott/Code/everything-repo/Useful Stuff/color_scatter/icon.ico"))

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
UNIVERSAL_FONT2 = ctk.CTkFont(family="Unispace", size=13, weight="bold")
UNIVERSAL_FONT3 = ctk.CTkFont(family="Unispace", size=18, weight="bold")
hex = None

ctk.set_appearance_mode("dark")

#----------------------|Scatter Results Screen|----------------------#

screen_scatter_results = add_screen("scatter_results")

def execute_scatter():
    global hex
    hex = user_input_entry.get()

    h_pos = h_pos_slider.get()
    h_neg = h_neg_slider.get()
    s_pos = s_pos_slider.get()
    s_neg = s_neg_slider.get()
    l_pos = l_pos_slider.get()
    l_neg = l_neg_slider.get()
    results = scatter_color(hex, h_pos, h_neg, l_pos, l_neg, s_pos, s_neg)

    col1.configure(fg_color=f"#{results[0]}")
    col2.configure(fg_color=f"#{results[1]}")
    col3.configure(fg_color=f"#{results[2]}")
    col4.configure(fg_color=f"#{results[3]}")
    col5.configure(fg_color=f"#{results[4]}")
    col6.configure(fg_color=f"#{results[5]}")
    col7.configure(fg_color=f"#{results[6]}")
    col8.configure(fg_color=f"#{results[7]}")
    col9.configure(fg_color=f"#{results[8]}")

    col1_hex.configure(text=f"#{results[0]}")
    col2_hex.configure(text=f"#{results[1]}")
    col3_hex.configure(text=f"#{results[2]}")
    col4_hex.configure(text=f"#{results[3]}")
    col5_hex.configure(text=f"#{results[4]}")
    col6_hex.configure(text=f"#{results[5]}")
    col7_hex.configure(text=f"#{results[6]}")
    col8_hex.configure(text=f"#{results[7]}")
    col9_hex.configure(text=f"#{results[8]}")

    show_screen("scatter_results")

def copy_to_clipboard(event):
    widget = event.widget
    app.clipboard_clear()
    app.clipboard_append(widget.cget("text"))

def back_to_screen2():
    show_screen("scatter")

col1 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col1.place(relx=0.15, rely=0.12, anchor="center")
col2 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col2.place(relx=0.15, rely=0.31, anchor="center")
col3 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col3.place(relx=0.15, rely=0.50, anchor="center")
col4 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col4.place(relx=0.15, rely=0.69, anchor="center")
col5 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col5.place(relx=0.15, rely=0.88, anchor="center")

col6 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col6.place(relx=0.625, rely=0.12, anchor="center")
col7 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col7.place(relx=0.625, rely=0.31, anchor="center")
col8 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col8.place(relx=0.625, rely=0.50, anchor="center")
col9 = ctk.CTkLabel(screen_scatter_results, text="", width=80, height=80, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
col9.place(relx=0.625, rely=0.69, anchor="center")

col1_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col1_hex.place(relx=0.38, rely=0.07, anchor="center")
col1_hex.bind("<Button-1>", copy_to_clipboard)
col2_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col2_hex.place(relx=0.38, rely=0.26, anchor="center")
col2_hex.bind("<Button-1>", copy_to_clipboard)
col3_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col3_hex.place(relx=0.38, rely=0.45, anchor="center")
col3_hex.bind("<Button-1>", copy_to_clipboard)
col4_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col4_hex.place(relx=0.38, rely=0.64, anchor="center")
col4_hex.bind("<Button-1>", copy_to_clipboard)
col5_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col5_hex.place(relx=0.38, rely=0.83, anchor="center")
col5_hex.bind("<Button-1>", copy_to_clipboard)

col6_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col6_hex.place(relx=0.85, rely=0.07, anchor="center")
col6_hex.bind("<Button-1>", copy_to_clipboard)
col7_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col7_hex.place(relx=0.85, rely=0.26, anchor="center")
col7_hex.bind("<Button-1>", copy_to_clipboard)
col8_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col8_hex.place(relx=0.85, rely=0.45, anchor="center")
col8_hex.bind("<Button-1>", copy_to_clipboard)
col9_hex = ctk.CTkButton(screen_scatter_results, text="#EEEEEE", width=60, font=UNIVERSAL_FONT3)
col9_hex.place(relx=0.85, rely=0.64, anchor="center")
col9_hex.bind("<Button-1>", copy_to_clipboard)

regenerate = ctk.CTkButton(screen_scatter_results, text="REGEN", font=UNIVERSAL_FONT, command=execute_scatter)
regenerate.place(relx=0.75, rely=0.835, anchor="center")

back_button_results = ctk.CTkButton(screen_scatter_results, text="BACK", font=UNIVERSAL_FONT, command=back_to_screen2)
back_button_results.place(relx=0.75, rely=0.93, anchor="center")


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
def back_to_screen1():
    show_screen("input")

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

# --- HUE --- #
h_pos_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=hpos_feedback)
h_neg_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=hneg_feedback)
h_pos_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
h_neg_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
h_pos_slider.place(relx=0.14, rely=0.3, anchor="center")
h_neg_slider.place(relx=0.26, rely=0.3, anchor="center")
h_pos_val.place(relx=0.14, rely=0.5, anchor="center")
h_neg_val.place(relx=0.26, rely=0.5, anchor="center")

# --- SATURATION --- #
s_pos_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=spos_feedback)
s_neg_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=sneg_feedback)
s_pos_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
s_neg_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
s_pos_slider.place(relx=0.44, rely=0.3, anchor="center")
s_neg_slider.place(relx=0.56, rely=0.3, anchor="center") 
s_pos_val.place(relx=0.44, rely=0.5, anchor="center")
s_neg_val.place(relx=0.56, rely=0.5, anchor="center")

# --- LIGHTNESS --- #
l_pos_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=lpos_feedback)
l_neg_slider = ctk.CTkSlider(screen_scatter, orientation="vertical", height=170, command=lneg_feedback)
l_pos_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
l_neg_val = ctk.CTkLabel(screen_scatter, text="0", font=UNIVERSAL_FONT2)
l_pos_slider.place(relx=0.74, rely=0.3, anchor="center")
l_neg_slider.place(relx=0.86, rely=0.3, anchor="center")
l_pos_val.place(relx=0.74, rely=0.5, anchor="center")
l_neg_val.place(relx=0.86, rely=0.5, anchor="center")

generate = ctk.CTkButton(screen_scatter, text="GENERATE", font=UNIVERSAL_FONT, command=execute_scatter)
generate.place(relx=0.75, rely=0.61, anchor="center")

back_button = ctk.CTkButton(screen_scatter, text="BACK", font=UNIVERSAL_FONT, command=back_to_screen1)
back_button.place(relx=0.75, rely=0.71, anchor="center")

color_maintained_preview = ctk.CTkLabel(screen_scatter, text="", width=180, height=180, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
color_maintained_preview.place(relx=0.3, rely=0.76, anchor="center")

current_hsl = ctk.CTkLabel(screen_scatter, text="", font=UNIVERSAL_FONT3)
current_hsl.place(relx=0.75, rely=0.86, anchor="center")

HUE_TITLE = ctk.CTkLabel(screen_scatter, text="Hue", font=UNIVERSAL_FONT)
HUE_TITLE.place(relx=0.2, rely=0.075, anchor="center")

SAT_TITLE = ctk.CTkLabel(screen_scatter, text="Sat", font=UNIVERSAL_FONT)
SAT_TITLE.place(relx=0.5, rely=0.075, anchor="center")

LIGHT_TITLE = ctk.CTkLabel(screen_scatter, text="Light", font=UNIVERSAL_FONT)
LIGHT_TITLE.place(relx=0.8, rely=0.075, anchor="center")

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
        h, s, l = hex_to_hsl(hex)
        color_maintained_preview.configure(fg_color=f"#{hex}")
        current_hsl.configure(text=f"Input HSL:\nH:{h}\nS:{s}\nL:{l}")
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

app_title = ctk.CTkLabel(screen_input, text="ColorScatter", font=ctk.CTkFont(family="Unispace", size=45, weight="bold"))
app_title.place(relx=0.5, rely=0.12, anchor="center")

color_preview = ctk.CTkLabel(screen_input, text="", width=180, height=180, fg_color="#ffffff", corner_radius=CORNER_RADIUS)
color_preview.place(relx=0.3, rely=0.6, anchor="center")

scatter_button = ctk.CTkButton(screen_input, text="SCATTER", font=UNIVERSAL_FONT, command=initiate_scatter)
scatter_button.place(relx=0.75, rely=0.45, anchor="center")
#other_button = ctk.CTkButton(screen_input, text="OTHER", font=UNIVERSAL_FONT) #other buttons for eventual future function additions (maybe complementary colors or whatever)
#other_button.place(relx=0.75, rely=0.55, anchor="center")
#other_button = ctk.CTkButton(screen_input, text="OTHER", font=UNIVERSAL_FONT)
#other_button.place(relx=0.75, rely=0.65, anchor="center")
#other_button = ctk.CTkButton(screen_input, text="OTHER", font=UNIVERSAL_FONT)
#other_button.place(relx=0.75, rely=0.75, anchor="center")

validation_label = ctk.CTkLabel(screen_input, text="", font=UNIVERSAL_FONT)
validation_label.place(relx=0.5, rely=0.2, anchor="center")

user_input_entry = ctk.CTkEntry(screen_input, placeholder_text="#808080", font=UNIVERSAL_FONT, corner_radius=CORNER_RADIUS, validate="key", validatecommand=(vcmd, "%P"))
user_input_entry.place(relx=0.5, rely=0.3, anchor="center")
user_input_entry.bind("<KeyRelease>", update_color_preview)
user_input_entry.bind("<KeyRelease>", validation_check)

#----------------------|Start Program|----------------------#

show_screen("input")
app.mainloop()