from PyQt6.QtWidgets import QMessageBox

from rent.exel import create_rent
from scripts.resource_path import resource_path
from scripts.windows import WindowBase


class MetersDataWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/meters_data.ui')
        self.form.send.clicked.connect(self.send)
        self.form.menu.clicked.connect(self.back_to_menu)

    def send(self):
        try:
            cold_water = self.form.cw.value()
            hot_water = self.form.hw.value()
            electricity = self.form.electricity.value()
            month = self.form.mh.currentIndex()
            year = self.form.year.value()
            res_price = WindowBase.db.count_meters(WindowBase.user_id, cold_water, hot_water, electricity)
            cold_price = round(24.8*cold_water, 2)
            hot_price = round(27.72*hot_water, 2)
            electricity_price = round(3.58*electricity, 2)
            price = round(cold_price + electricity_price + hot_price, 2)
            rent_id = WindowBase.db.send_meters_data(hot_water, cold_water, month, WindowBase.user_id, year, res_price[0], electricity)
            user_data = WindowBase.db.get_user(WindowBase.user_id)
            create_rent(rent_id, user_data[2], user_data[1], month, year, cold_water, hot_water, electricity, res_price[1], res_price[2], res_price[3])
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("Данные отправлены успешно!")
            msgBox.setWindowTitle("Отправка данных")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

            returnValue = msgBox.exec()
            self.window.hide()
            WindowBase.windows[4].open(res_price[0], month, year, rent_id, user_data[2], user_data[1])
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("Ошибка " + str(e))
            msgBox.setWindowTitle("Отправка данных")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

            returnValue = msgBox.exec()
    def back_to_menu(self):
        self.window.hide()



