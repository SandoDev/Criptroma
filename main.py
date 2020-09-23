import tkinter as tk
import constants


class Application:
    def __init__(self, window):
        self.wind = window
        self.wind.title(constants.NAME_APP)
        self.create_widgets()

    def create_widgets(self):
        # Creating a Frame container
        frame = tk.LabelFrame(self.wind, text='Crear un nuevo Criptroma')
        frame.grid(row=0, column=0, columnspan=3, pady=10)

        # Text input
        text_area = tk.Text(frame, height=10, width=50)
        text_area.grid(row=1, column=0)

        # Button Generate
        bt_generate = tk.Button(frame, text='Generar')
        bt_generate.grid(row=3, columnspan=2, sticky=tk.W+tk.E)


def main():
    window = tk.Tk()
    application = Application(window=window)
    window.mainloop()


if __name__ == "__main__":
    main()
