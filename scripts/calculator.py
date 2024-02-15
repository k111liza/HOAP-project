from scripts.resource_path import resource_path
from scripts.windows import WindowBase
class CalculatorWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/design.ui')
        self.form.calculate.clicked.connect(self.calculation)
        self.form.exit.clicked.connect(self.exit)
        self.form.metersdata.clicked.connect(self.open_meters_data)
    def open_meters_data(self):
        WindowBase.windows[3].open()
    def calculation(self):
        count = self.form.counts.value()
        price = self.form.price.value()
        result = count * price
        self.form.result.setText(f'{result} руб')

    def exit(self):
        self.close()
        WindowBase.windows[0].open()
        f = open(resource_path('../rememberme.txt'), 'w')
        f.write('')
        f.close()

