from scripts.resource_path import resource_path
from scripts.windows import WindowBase
from PyQt6.QtWidgets import QMessageBox


class NotoficationsWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/notifications.ui')
        self.form.details.clicked.connect(self.open_details)
    def open_details(self):
        WindowBase.windows[9].open()