#Josiah Hendley
#4/17/26
#Favorite Saying


import tkinter

class FavoriteSayingGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Favorite Saying")

        self.label = tkinter.Label(
            self.main_window,
            text="Hard work beats talent when talent doesn't work hard."
        )
        self.label.pack()

        tkinter.mainloop()

if __name__ == "__main__":
    gui = FavoriteSayingGUI()
