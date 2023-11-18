from GUI.MainFrame import Ventana
from Domain.game import Juego

ventana = Ventana()
juego = Juego(ventana.get_canvas())

ventana.mostrar_ventana()