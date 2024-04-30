from scripts.resource_path import resource_path
from scripts.windows import WindowBase
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget


class NotoficationsWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/notifications.ui')
        self.form.detailsbutton.clicked.connect(self.open_details)
        self.form.report.cellClicked.connect(self.show_detailsbutton)
        self.currentrow = None

    def open(self):
        self.form.detailsbutton.hide()
        self.showdata = WindowBase.db.get_notification()
        self.form.report.setRowCount(0)
        self.form.report.setRowCount(len(self.showdata))
        for i, row in enumerate(self.showdata):
            self.form.report.setItem(i, 0, QTableWidgetItem(self.showdata[i][1]))
        self.form.report.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.window.show()
    def open_details(self):
        WindowBase.windows[8].open(self.showdata[self.currentrow])
    def show_detailsbutton(self, row, column):
        self.currentrow=row
        self.form.detailsbutton.show()
