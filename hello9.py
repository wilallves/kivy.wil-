from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

grid_layout = GridLayout(cols=2)

# Pagina:51
grid_layout.add_widget(widget=1)
grid_layout.add_widget(widget=2)

# Pagina:52
grid_layout.spacing = [10,10] # Define o espaçamento entre as células (horizontal, vertical)
grid_layout.padding = [20, 20] # Define o espaçamentointerno do grid (top, right, bottom, left)

# Pagina:53
Widget.size_hint_x = 0.5 # Widget se expandirá para ocupar metade da largura da célula
Widget.size_hint_y = None # widget não expandirá na altura
