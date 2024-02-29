from PyQt6.QtWidgets import QTableWidgetItem, QAbstractItemView, QTableWidget

from scripts.resource_path import resource_path
from scripts.windows import WindowBase


months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

class ReportForUserWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/table.ui')
        self.form.payment.clicked.connect(self.open_payment)
        self.form.tableWidget.cellClicked.connect(self.payment_button)
        self.currentrow=None

    def open(self):
        showdata = WindowBase.db.show_data(WindowBase.user_id)
        self.form.tableWidget.setRowCount(0)
        self.form.tableWidget.setRowCount(len(showdata))
        for i, row in enumerate(showdata):
            self.form.tableWidget.setItem(i, 0, QTableWidgetItem(
                f"{row[2]} м3 холодной воды, {row[3]} м3 горячей воды, {row[7]} квт/ч электроэнергии за {months[row[4]]}"))
            self.form.tableWidget.setItem(i, 1, QTableWidgetItem(
                f"{months[row[4]]} {row[5]}"))
            self.form.tableWidget.setItem(i, 2, QTableWidgetItem(
                f"{row[6]} руб"))
            if row[8] is not None:
                self.form.tableWidget.setItem(i, 3, QTableWidgetItem(
                    f"Оплачен"))
                self.form.tableWidget.setItem(i, 4, QTableWidgetItem(
                    f"{row[10]}"))
            else:
                self.form.tableWidget.setItem(i, 3, QTableWidgetItem(
                    f"Не оплачен"))
                self.form.tableWidget.setItem(i, 4, QTableWidgetItem(
                    f""))
        self.form.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.form.payment.hide()


        self.window.show()
    def payment_button(self, row, column):
        self.currentrow=row
        if self.form.tableWidget.item(row, 3).text()=='Не оплачен':
            self.form.payment.show()
        else:
            self.form.payment.hide()
    def open_payment(self):
        row=self.currentrow
        month, year = self.form.tableWidget.item(row,1).text().split()
        month=months.index(month)
        price = self.form.tableWidget.item(row, 2).text().split()[0]
        user_data = WindowBase.db.get_user(WindowBase.user_id)
        rent = WindowBase.db.get_metersdata(WindowBase.user_id, month,year,price)
        WindowBase.windows[4].open(price, month, year, rent[0], user_data[1], user_data[2])




