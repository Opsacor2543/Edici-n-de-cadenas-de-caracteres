import tkinter as tk
from tkinter import filedialog
import pandas as pd


class archivosLeer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Arrastrar y soltar archivos CSV")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Arrastra y suelta un archivo CSV aquí", bg="lightgray", font=("Arial", 12), pady=50)
        self.label.pack(fill=tk.BOTH, expand=True)

        # Asociar eventos de arrastrar y soltar
        self.label.bind("<DragEnter>", self.on_drag_enter)
        self.label.bind("<DragLeave>", self.on_drag_leave)
        self.label.bind("<DragDrop>", self.on_drag_drop)

    def on_drag_enter(self, event):
        self.label.configure(bg="lightblue")

    def on_drag_leave(self, event):
        self.label.configure(bg="lightgray")

    def on_drag_drop(self, event):
        self.label.configure(bg="lightgray")
        file_path = event.data

        try:
            dataframe = pd.read_csv(file_path)
            print(dataframe.head())
        except Exception as e:
            print("Error al leer el archivo CSV:", e)

app = archivosLeer()
app.mainloop()