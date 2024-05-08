from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class MinhaApp(App):
    def build():
        # Definindo a cor de fundo da janela como branco
        Window.clearcolor = (1, 1, 1, 1)
        # (R, G, B, A) -> R = G = B = 0 para branco, A = 1 para opacidade total

        # Criando um rótulo com texto preto
        label = Label(text='Esta é uma tela com o fundo branco', color=(0, 0, 0, 1))
        # (R, G, B, A) -> R = G = B = 0 pzrz preto, A = 1 para opacidade total

        return label
    
if __name__ == "__main__":
    MinhaApp().run()
