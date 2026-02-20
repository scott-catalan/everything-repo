'''
# Project Creation Date: 9:17:12 PM, 2/19/2026
'''

import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Stopwatch")
        self.geometry("400x400")
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        
        self.label = ctk.CTkLabel(self, text=f"{self.hours}:{self.minutes}:{self.seconds}")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Start", command=self.start_timer)
        self.button.pack(pady=10)

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def start_timer(self):
        self.update_time()

    def update_time(self):
        self.seconds += 1
        if self.seconds % 60 == 0:
            self.seconds = 0
            self.minutes += 1
            if self.minutes % 60 == 0:
                self.minutes = 0
                self.hours += 1

        self.label.configure(text=self.get_time())
        self.after(1000, self.update_time)

if __name__ == "__main__":
    app = App()
    app.mainloop()