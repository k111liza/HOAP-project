from scripts.resource_path import resource_path
from scripts.windows import WindowBase


class LoginWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/login.ui')
        self.form.enter.clicked.connect(self.enter)
        self.form.registration.clicked.connect(self.register)

    def enter(self):
        login = self.form.login.text()
        password = self.form.password.text()
        if login == 'admin' and password == 'admin':
            self.window.hide()
            WindowBase.windows[1].open()
            if self.form.rememberme.isChecked():
                f = open(resource_path('../rememberme.txt'), 'w')
                f.write(login)
                f.close()

        else:
            self.form.message.setText('Неверный логин или пароль')
    def register(self):
        self.window.hide()
        WindowBase.windows[2].open()



    