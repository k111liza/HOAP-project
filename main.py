from PyQt6.QtWidgets import QApplication

from scripts.Report_for_user import ReportForUserWindow
from scripts.calculator import CalculatorWindow
from scripts.check import CheckWindow
from scripts.details import DetailsWindow
from scripts.graphics import GraphicsWindow
from scripts.login import LoginWindow
from scripts.meters_data import MetersDataWindow
from scripts.notifications import NotoficationsWindow
from scripts.registration import RegistrationWindow
from scripts.resource_path import resource_path
from scripts.windows import WindowBase



win = QApplication([])
loginwindow=LoginWindow()
calculatorwindow=CalculatorWindow()
registrationwindow=RegistrationWindow()
metersdata = MetersDataWindow()
check = CheckWindow()
reportforuser=ReportForUserWindow()
notifications = NotoficationsWindow()
graphics = GraphicsWindow()
details = DetailsWindow()
f=open(resource_path('rememberme.txt'), 'r')
file_data = f.read()
if file_data.strip()=='':
    loginwindow.open()
else:
    WindowBase.user_id = int(file_data)
    calculatorwindow.open(WindowBase.user_id)
win.exec()