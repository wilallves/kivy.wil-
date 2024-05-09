from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (720,350)

class FloatApp(App):
    def build(self):
        
        flo = FloatLayout()
        
        l1 = Label(
            text="usuário", size_hint=(.2, .1),
            pos=(200, 350), color = [1,1,1,1]
        )
        with l1.canvas:
            Color(0, 1, 0, 0.25)
            Rectangle(pos=l1.pos, size=(190, 50))

        flo.add_widget(l1)

        self.t1 = TextInput(size_hint=(.4, .1), pos=(400, 350))
        flo.add_widget(self.t1)
        
        l2 = Label(
            text="Senha", size_hint=(.2, .1),
            pos=(200, 250),color = [1,1,1,1]
        )
        with l2.canvas:
            Color(0, 1, 0, 0.25)
            Rectangle(pos=l2.pos, size=(190, 50))
        flo.add_widget(l2)

        t2 = TextInput(
            multiline=True, size_hint=(.4, .1), pos=(400, 250)
        )

        flo.add_widget(t2)
        
        b1 = Button(
            text='Entrar', size_hint = (.2, .1),
            pos_hint = {'center_x':.5, 'center_y':.07},
            on_press = self.entrar
        )
        b2 = Button(
            text='Cadastrar', size_hint = (.2, .1),
            pos_hint = {'center_x':.5, 'center_y':.20},
            on_press = self.cadastrar
        )
        
        self.label_cadastrar = Label()
        self.label_entrar = Label()
        
        flo.add_widget(b1)
        flo.add_widget(b2)
        flo.add_widget(self.label_cadastrar)
        flo.add_widget(self.label_entrar)
        
        return flo

    def cadastrar(self, instance):
        login = self.t1.text
        mensagem = f'O Login {login} foi cadastrado!'
        self.label_cadastrar.text = mensagem
    
    def entrar(self, instance):
        login = self.t1.text
        mensagem = f'O login {login} entrou no sistema!'
        self.label_cadastrar.text = mensagem
      
FloatApp().run()
