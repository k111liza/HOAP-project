import urllib.request

import os
from pathlib import Path

from PyQt6.QtWidgets import QMessageBox, QFileDialog

from scripts.windows import WindowBase

import requests

import datetime



months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
class CheckWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/check.ui')
        self.form.download.clicked.connect(self.download)
        self.form.add_check.clicked.connect(self.open_document)
        self.form.save.clicked.connect(self.save)
        self.filepath = None
    def open(self, price, month, year, id, name, surname):
        self.form.price.setText(str(price) + ' руб')
        self.form.month_bill.setText(f'Счет за {months[month]} {year}')
        self.id = id
        self.name = name
        self.surname = surname
        self.month = months[month]
        self.year = year
        self.window.show()

    def download(self):
        fn = f"{self.id}_{self.surname}_{self.name}_{self.month}_{self.year}.xlsx"
        file_url = "https://api.innoprog.ru:3000/files/materials/py_beg/py_beg4.pdf/"

        try:
            downloads_folder = Path(os.path.expanduser("~")) / "Downloads"
            file_name = str(downloads_folder/fn)
            print(file_name)
            urllib.request.urlretrieve(file_url, file_name)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText(f"Файл успешно сохранен в {file_name} ")
            msgBox.setWindowTitle("Успешно!")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

            returnValue = msgBox.exec()
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("Ошибка при скачивании файла: " + str(e))
            msgBox.setWindowTitle("Ошибка скачивания!")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

            returnValue = msgBox.exec()

    def open_document(self):
        file_name, _ = QFileDialog.getOpenFileName(self.window, 'Open Document', '', 'PDF Files (*.pdf);;All Files (*)')
        if file_name:
            self.filepath = file_name
            file = file_name.split("/")[-1]
            self.form.path.setText(file)
    def save(self):
        if self.filepath is None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText('Требуется загрузить чек!')
            msgBox.setWindowTitle("Отсутствует чек!")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

            returnValue = msgBox.exec()
        else:
            try:
                url = f"http://127.0.0.1:80/uploadfile/{self.id}"

                with open(self.filepath, "rb") as file:
                    files = {"file": (self.filepath, file, "multipart/form-data")}
                    response = requests.post(url, files=files)
                WindowBase.db.add_check(self.id, datetime.datetime.now())
                WindowBase.windows[5].update()

                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setText('Данные успешно сохранены!')
                msgBox.setWindowTitle("Успешно!")
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

                returnValue = msgBox.exec()
                self.window.hide()
            except Exception as e:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setText('Error: ' + str(e))
                msgBox.setWindowTitle("Error!")
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

                returnValue = msgBox.exec()

