from scripts.resource_path import resource_path
from scripts.windows import WindowBase


class CalculatorWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/design.ui')
        self.form.exit.clicked.connect(self.exit)
        self.form.metersdata.clicked.connect(self.open_meters_data)
        self.form.Bill_history.clicked.connect(self.open_report_user)
        self.form.notifications.clicked.connect(self.open_notifications)
        self.form.graphics.clicked.connect(self.open_graphic)



    def open(self, user_id):
        user = WindowBase.db.get_user(user_id)
        self.form.welcome.setText(f'Добро пожаловать, {user[1]} !')
        self.window.show()

    def open_meters_data(self):
        WindowBase.windows[3].open()
    def calculation(self):
        count = self.form.counts.value()
        price = self.form.price.value()
        result = count * price
        self.form.result.setText(f'{result} руб')

    def open_report_user(self):
        WindowBase.windows[5].open()

    def exit(self):
        self.close()
        WindowBase.windows[0].open()
        f = open(resource_path('rememberme.txt'), 'w')
        f.write('')
        f.close()
    def open_notifications(self):
        WindowBase.windows[6].open()
    def open_graphic(self):
        WindowBase.windows[7].open()
