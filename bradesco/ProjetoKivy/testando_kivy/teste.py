from kivy.app import App #todo aplicativo Kivy precisa da subclasseApp e da função build()
from kivy.uix.label import Label

class MainApp(App):
    def build(self): #Neste caso, crie um widget do tipo label e passe comoparâmetro: text, size_hint, e pos_hint (estes dois últimosargumentos não são obrigatórios)
        label = Label(
                text='Olá, mundo!', 
                size_hint=(.5, .5), 
                pos_hint={'center_x': .5, 'cenet_y': .5}
                )
        
        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()