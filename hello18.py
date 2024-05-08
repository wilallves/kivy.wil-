from kivy.app import App
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        return Button(text='Clique Aqui', size_hint=(0.5, 0.2))
    # Botão ocupará mateda da largura e 20% da altura do layout pai

if __name__ == '__main__':
    MinhaApp().run()
