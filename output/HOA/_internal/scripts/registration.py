from PyQt6.QtWidgets import QMessageBox

from scripts.windows import WindowBase


class RegistrationWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/registration.ui')
        self.form.registration.clicked.connect(self.register)
        self.form.alreadyregistered.clicked.connect(self.return_enter)
        self.form.error.hide()
    def open(self):
        self.form.error.hide()
        self.form.name.setText('')
        self.form.surname.setText('')
        self.form.email.setText('')
        self.form.password.setText('')
        self.window.show()
    def register(self):
        name = self.form.name.text()
        surname = self.form.surname.text()
        email = self.form.email.text()
        password = self.form.password.text()
        res = WindowBase.db.registration(email, name, surname, password)
        if res is None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("Регистрация прошла успешно!")
            msgBox.setWindowTitle("Регистрация")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.StandardButton.Ok:
                self.window.hide()
                WindowBase.windows[0].open()
        else:
            self.form.error.show()

    def return_enter(self):
        self.window.hide()
        WindowBase.windows[0].open()


