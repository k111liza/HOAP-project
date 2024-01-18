from PyQt6.QtWidgets import QApplication

from scripts.calculator import CalculatorWindow
from scripts.login import LoginWindow
from scripts.registration import RegistrationWindow
from scripts.resource_path import resource_path

win = QApplication([])
loginwindow=LoginWindow()
calculatorwindow=CalculatorWindow()
registrationwindow=RegistrationWindow()
f=open(resource_path('rememberme.txt'), 'r')
if f.read().strip()=='':
    loginwindow.open()
else:
    calculatorwindow.open()
win.exec()