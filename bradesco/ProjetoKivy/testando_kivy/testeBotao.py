from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()
    
    def onPressButton(self):
        print('Você apertou o botão!!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()


# no def build(self), em vez de fazermos:
#     button = Button(text: 'Aperte o botão!',
#                     size_hint: (.5, .5)
#                     pos_hint: {'center_x': .5, 'center_y': .5}
#                     )
#     button.bind(on_press=onPressButton)

# Fazemos apes: return Button() e referenciamos o botão em um arquivo .kv