import tkinter as tk
from style import styles


class MainMenu(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager 
        self.configure(
            background=styles.BACKGROUND
        )
        self.init_widgets()
    def init_widgets(self):
        tk.Button(
            self,
            text="CARGAR UNA OPERACIÓN",
            command=lambda: print('Has indicado que vas a cargar una operación'),
            **styles.STYLE,
            relief=tk.RAISED,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="ESTADO DE CUENTA DEL CLIENTE",
            command=lambda: print('Has indicado para ver el estado de cuenta del cliente '),
            **styles.STYLE,
            relief=tk.RAISED,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="PROYECCIONES DE INGRESOS",
            command=lambda: print('Has indicado que queres ver las proyecciones de ingresos'),
            **styles.STYLE,
            relief=tk.RAISED,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="STOCK DE VEHICULOS",
            command=lambda: print('Has indicado que queres ver el stock de vehiculos'),
            **styles.STYLE,
            relief=tk.RAISED,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="STOCK DE INMUEBLES",
            command=lambda: print('Has indicado que queres ver el stock de inmuebles'),
            **styles.STYLE,
            relief=tk.RAISED,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )