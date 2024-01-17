from PyQt6.QtWidgets import QApplication

from scripts.calculator import CalculatorWindow
from scripts.login import LoginWindow
from scripts.resource_path import resource_path

win = QApplication([])
loginwindow=LoginWindow()
calculatorwindow=CalculatorWindow()
f=open(resource_path('rememberme.txt'), 'r')
if f.read().strip()=='':
    loginwindow.open()
else:
    calculatorwindow.open()
win.exec()