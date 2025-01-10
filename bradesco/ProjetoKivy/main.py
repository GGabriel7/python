from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase

class createAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.addUser(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"

            else:
                invalidForm()
            
        else:
            invalidForm()

    
    def login(self):
        self.reset()
        sm.current = "login"

    
    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class loginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        
        else:
            invalidLogin()
    

    def createBtn(self):
        self.reset()
        sm.current = "create"


    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    
    def on_enter(self, *args):
        user_data = db.getUser(self.current)
        if user_data:
            password, name, created = user_data
            self.n.text = "Nome da Conta: " + name
            self.email.text = "Email: " + self.current
            self.created.text =  "Criado em: " + created


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(
        title = "Login Inválido",
        content = Label(text = "Nome ou senha inválidos."),
        size_hint = (None, None), size = (400, 400)
    )
    pop.open()


def invalidForm():
    pop = Popup(
        title = "Formulário Inválido",
        content = Label(text = "Preencha todas as entradas com informações válidas."),
        size_hint = (None, None), size = (400, 400)
    )
    pop.open()

kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [
    loginWindow(name="login"),
    createAccountWindow(name="create"),
    MainWindow(name="main")
]

for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm
    

if __name__ == "__main__":
    MyMainApp().run()
