from scripts.windows import WindowBase


class RegistrationWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/registration.ui')
        self.form.registration.clicked.connect(self.register)
        self.form.alreadyregistered.clicked.connect(self.return_enter)
    def register(self):
        pass
    def return_enter(self):
        self.window.hide()
        WindowBase.windows[0].open()

