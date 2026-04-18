#Josiah Hendley
#4/17/26
#Show Info




import tkinter

class InfoGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Info Display")

        self.info_label = tkinter.Label(self.main_window, text="")
        self.info_label.pack()

        self.show_button = tkinter.Button(
            self.main_window,
            text="Show Info",
            command=self.show_info
        )
        self.show_button.pack()

        self.quit_button = tkinter.Button(
            self.main_window,
            text="Quit",
            command=self.main_window.destroy
        )
        self.quit_button.pack()

        tkinter.mainloop()

    def show_info(self):
        self.info_label.config(
            text="Josiah Hendley\n1234 Maple Street\nSpringfield, USA"
        )

if __name__ == "__main__":
    gui = InfoGUI()
