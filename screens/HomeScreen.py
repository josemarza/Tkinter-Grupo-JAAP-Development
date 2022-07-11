import tkinter as tk
from style import styles

class HomeScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager=manager
        self.init_widgets()

    def init_widget(self):
        tk.Label(
            self,
            text='Bienvenido a Grupo JAAP',
            justify=tk.CENTER,
            **styles.STYLE
            ).pack(
                **style.PACK
            )

