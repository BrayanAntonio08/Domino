import tkinter as tk

class Ventana:
    def __init__(self):
        # Inicializar la ventana y realizar configuraciones iniciales
        self.ventana = tk.Tk()
        self.configurar_ventana()
        self.crear_canvas()

    def configurar_ventana(self):
        # Configuraciones adicionales de la ventana
        self.ventana.title("Ventana Principal")
        # Agrega más configuraciones según sea necesario
        self.ventana.minsize(800,700)
        self.ventana.resizable(0,0)

    def crear_canvas(self):
        self.canvas = tk.Canvas(self.ventana, width=800, height=700)
        self.canvas.pack()

    def get_canvas(self):
        return self.canvas
    
    def mostrar_ventana(self):
        # Muestra la ventana
        self.ventana.mainloop()
