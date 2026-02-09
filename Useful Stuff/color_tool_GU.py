from color_tool_logic import validate_hex
import customtkinter as ctk
import colorsys

#----------------------|Initial|----------------------#

app = ctk.CTk()
app.geometry("400x500")
app.resizable(False, False)
ctk.set_appearance_mode("dark")

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

#----------------------|Color Variation Results Screen|----------------------#

screen_vary_results = add_screen("results")

#----------------------|Color Variation Configure Screen|----------------------#

def hpos(event):
    h_pos_val.configure(text=event)

def hneg(event):
    h_neg_val.configure(text=event)

def lpos(event):
    l_pos_val.configure(text=event)

def lneg(event):
    l_neg_val.configure(text=event)

def spos(event):
    s_pos_val.configure(text=event)

def sneg(event):
    s_neg_val.configure(text=event)

screen_vary = add_screen("vary")

h_pos = ctk.CTkSlider(screen_vary, orientation="vertical", command=hpos, height=170)
h_pos.place(relx=0.15, rely=0.3, anchor="center")
h_neg = ctk.CTkSlider(screen_vary, orientation="vertical", command=hneg, height=170)
h_neg.place(relx=0.25, rely=0.3, anchor="center")
l_pos = ctk.CTkSlider(screen_vary, orientation="vertical", command=lpos, height=170)
l_pos.place(relx=0.45, rely=0.3, anchor="center")
l_neg = ctk.CTkSlider(screen_vary, orientation="vertical", command=lneg, height=170)
l_neg.place(relx=0.55, rely=0.3, anchor="center")
s_pos = ctk.CTkSlider(screen_vary, orientation="vertical", command=spos, height=170)
s_pos.place(relx=0.75, rely=0.3, anchor="center")
s_neg = ctk.CTkSlider(screen_vary, orientation="vertical", command=sneg, height=170)
s_neg.place(relx=0.85, rely=0.3, anchor="center")

h_pos_val = ctk.CTkLabel(screen_vary, text="0")
h_pos_val.place(relx=0.15, rely=0.5, anchor="center")
h_neg_val = ctk.CTkLabel(screen_vary, text="0")
h_neg_val.place(relx=0.25, rely=0.5, anchor="center")
l_pos_val = ctk.CTkLabel(screen_vary, text="0")
l_pos_val.place(relx=0.45, rely=0.5, anchor="center")
l_neg_val = ctk.CTkLabel(screen_vary, text="0")
l_neg_val.place(relx=0.55, rely=0.5, anchor="center")
s_pos_val = ctk.CTkLabel(screen_vary, text="0")
s_pos_val.place(relx=0.75, rely=0.5, anchor="center")
s_neg_val = ctk.CTkLabel(screen_vary, text="0")
s_neg_val.place(relx=0.85, rely=0.5, anchor="center")

current_hsl = ctk.CTkLabel(screen_vary, text="Current HSL: ")
current_hsl.place(relx=0.3, rely=0.95, anchor="center")

color_track = ctk.CTkLabel(screen_vary, text="", fg_color="white", width=150, height=150)
color_track.place(relx=0.3, rely=0.75, anchor="center")

generate = ctk.CTkButton(screen_vary, text="Generate")
generate.place(relx=0.75, rely=0.8, anchor="center")

#----------------------|Input Screen|----------------------#

def input_hex(event):
    hex = user.get().lstrip('#')
    if validate_hex(user.get()):
        r, g, b = [int(hex[i:i+2], 16) / 255 for i in (0, 2, 4)]
        h, l, s = colorsys.rgb_to_hls(r, g, b)

        h_val, l_val, s_val = int(h * 360), int(l * 100), int(s * 100)

        current_hsl.configure(text=f"Inputted Color HSL:\n{int(h_val)}, {int(l_val)}, {int(s_val)}")
        color_track.configure(fg_color=f"#{hex}")

        h_pos.configure(from_=0, to=2)
        h_neg.configure(from_=0, to=2)
        l_pos.configure(from_=0, to=2)
        l_neg.configure(from_=0, to=2)
        s_pos.configure(from_=s_val, to=100, number_of_steps=100-s_val)
        s_neg.configure(from_=0, to=2)
        
        show_screen("vary")
    else:
        valid.configure(text="Invalid Hex Code")

screen_input = add_screen("input")

valid = ctk.CTkLabel(screen_input, text="")
valid.place(relx=0.5, rely=0.3, anchor="center")
user = ctk.CTkEntry(screen_input, placeholder_text="#808080")
user.place(relx=0.5, rely=0.5, anchor="center")
user.bind("<Return>", input_hex)
#when more modes are added in the future (complementary colors, color palette, etc), remove user.bind and replace it with one button per function that submits user to input_hex

#----------------------|Start Program|----------------------#

show_screen("input")
app.mainloop()