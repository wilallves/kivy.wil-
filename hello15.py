from kivy.app import App
from kivy.uix.image import Image,AsyncImage

class MinhaApp(App):
    def build(self):

        return AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png')
    
if __name__ == '__main__':
    MinhaApp().run()
