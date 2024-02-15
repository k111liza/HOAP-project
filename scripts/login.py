from scripts.resource_path import resource_path
from scripts.windows import WindowBase


class LoginWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/login.ui')
        self.form.enter.clicked.connect(self.enter)
        self.form.registration.clicked.connect(self.register)
        self.form.loginerror.hide()

    def enter(self):
        login = self.form.login.text()
        password = self.form.password.text()
        data = WindowBase.db.get_login(login, password)
        if data:
            self.window.hide()
            WindowBase.windows[1].form.welcome.setText(f'Добро пожаловать, {data[1]}')
            WindowBase.windows[1].open()
            WindowBase.user_id = int(data[0])
            self.form.loginerror.hide()
            if self.form.rememberme.isChecked():
                f = open(resource_path('../rememberme.txt'), 'w')
                f.write(str(data[0]))
                f.close()
        else:
            self.form.loginerror.show()
    def register(self):
        self.window.hide()
        WindowBase.windows[2].open()



    