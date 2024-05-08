from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

layout_stack = StackLayout()

botao1 = Button(text='Botão 1')
botao2 = Button(text='Botão 2')
layout_stack.add_widget(botao1)
layout_stack.add_widget(botao2)
