from scripts.resource_path import resource_path
from scripts.windows import WindowBase
from PyQt6.QtWidgets import QMessageBox


class DetailsWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/details.ui')
