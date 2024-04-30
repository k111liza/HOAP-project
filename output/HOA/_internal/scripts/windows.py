from PyQt6 import uic

from database import DataBase
from scripts.resource_path import resource_path


class WindowBase:
    windows = []
    db = DataBase()


    def __init__(self, path):
        Form, Windows = uic.loadUiType(resource_path(path))
        self.window = Windows()
        self.form = Form()
        self.form.setupUi(self.window)
        WindowBase.windows.append(self)

    def open(self):
        self.window.show()

    def close(self):
        self.window.hide()
