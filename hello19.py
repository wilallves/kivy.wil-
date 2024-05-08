from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20)

        # Slider
        Slider = Slider(min=0, max=100, value=50, step=1)
        # Definido step=1 para permitir apenas valores inteiros
        Slider.bind(value=self.atualizar_label)

        # Label para mostrar o valor do slider
        self.label = Label(text="Valor do Slider: {}".format(int(Slider.value)))
        # Exibir apenas o valor inteiro

        # Adicionando os widgets ao layout
        layout.add_widget(Slider)
        layout.add_widget(self.label)

        return layout
    
    def atualizar_label(self, instance, valor):
        # Atualizar o texto do label com o valor inteiro atual do slider
        self.label.text = "Valor do Slider: {}".format(int(valor))

if __name__ == "__main__":
    MinhaApp().run()
