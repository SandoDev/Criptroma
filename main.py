import tkinter as tk
import criptroma


class Application:
    def __init__(self, window):
        self.wind = window
        self.wind.title(criptroma.NAME_APP)
        self.create_widgets()

    def create_widgets(self):
        # Creating a Frame container
        frame = tk.LabelFrame(self.wind, text='Ingrese el texto')
        frame.grid(row=0, column=0, columnspan=3, pady=10)
        # Text input
        self.text_in = tk.Text(frame, height=6, width=100)
        self.text_in.grid(row=1, column=0)
        # Button Generate
        bt_generate = tk.Button(
            frame,
            text='Generar',
            command=lambda: self.retrieve_input(),
            bg='green'
        )
        bt_generate.grid(row=3, columnspan=2, sticky=tk.W+tk.E)

        # Creating a Frame container output
        frame_out = tk.LabelFrame(self.wind, text='Criptroma generado')
        frame_out.grid(row=4, column=0, columnspan=3, pady=10)
        # Text output
        self.text_out = tk.Text(frame_out, height=20, width=100)
        self.text_out.grid(row=5, column=0)

    def retrieve_input(self):
        # TODO este metodo debe tomar la entrada del textarea
        # y mostrar la imagen de salida con el criptroma
        out_text = self.text_in.get("1.0", "end-1c")
        out_text = out_text + '\n' + criptroma.main()
        self.text_out.insert(tk.END, out_text + '\n')


if __name__ == "__main__":
    window = tk.Tk()
    application = Application(window=window)
    window.mainloop()
