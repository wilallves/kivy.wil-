from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from functools import partial
from kivy.uix.modalview import ModalView


class Login(BoxLayout):
    def __init__(self, arg1=None, arg2=None, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__(**kwargs)
        self.arg1 = arg1
        self.arg2 = arg2
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        self.add_widget(Image(source='data:image/png;base64,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'))
        
        self.add_widget(Label(text="LOGIN", font_size=40, font_name='Georgia', color=get_color_from_hex('##0f0360')))

        
        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)
        

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('##0f0360'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('##0f0360'), font_size=20))
        self.add_widget(self.senha_input)
        
        
        self.cadastrar_button = Button(text="Entrar", background_color=(0, 1, 0, 0.75))
        self.login_button = Button(text="Não possui uma conta? Cadastre-se", background_color=(0, 0, 1))
        self.login_button.bind(on_release=partial(self.create_new_window, self.arg1, self.arg2))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

    def create_new_window(self, arg1, arg2, instance):
            new_window = NewWindow(arg1, arg2)
            new_window.open()
            Window.clearcolor = (1, 1, 1, 1)

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class NewWindow(BoxLayout):
    def __init__(self, arg1, arg2, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__(**kwargs)
        self.arg1 = 'value1'
        self.arg2 = 'value2'
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=40, font_name='Georgia', color=get_color_from_hex('##e6e5ee')))

        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.email_input = TextInput(hint_text="Digite seu email ...")
        self.celular_input = TextInput(hint_text="Digite o número do seu celular ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Celular:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.celular_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=(0, 0, 1))
        self.button_cadastrar.bind(on_release=partial(self.entrar_interface_login, self.arg1, self.arg2))
        self.add_widget(self.button_cadastrar)

    def entrar_interface_login(self, arg1, arg2, instance):
            entrar_login = Login(arg1, arg2)
            entrar_login.open()
            Window.clearcolor = (1, 1, 1, 1)


    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()
