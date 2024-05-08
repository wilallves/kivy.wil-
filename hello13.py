from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label  import Label

class MinhaApp(App):
    def build(self):

        # Layout principal
        layout_principal = GridLayout(cols=2)

        # Coluna à esquerda (30% da tela)
        coluna_esquedar = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        menu_itens = ['Arquivado', 'Editar', 'Seleção', 'Ver', 'Acessar', 'Sair']
        labe11 = Label(text='Menu')
        coluna_esquedar.add_widget(labe11)
        for item in menu_itens:
            botao = Button(text=item)
            coluna_esquedar.add_widget(botao)

        # Coluna à direita dividida em três partes iguais
        coluna_direita = GridLayout(cols=1, rows=3)
        for i in range(3):
            botao = Button(text=f'Botão {i+7}')
            coluna_direita.add_widget(botao)

        # Adicionando as coluna ao layout principal
        layout_principal.add_widget(coluna_esquedar)
        layout_principal.add_widget(coluna_direita)

        return layout_principal
    
if __name__ == "__main__":
    MinhaApp().run()
