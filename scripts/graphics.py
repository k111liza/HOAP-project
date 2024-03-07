from PyQt6 import QtCharts
import math
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QPainter
from PyQt6.QtWidgets import QTableWidgetItem, QAbstractItemView, QTableWidget, QGraphicsScene, QGraphicsLineItem, \
    QWidget, QVBoxLayout

from scripts.resource_path import resource_path
from scripts.windows import WindowBase


months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

def update_month_number(month):
    month += 1
    if len(str(month)) == 1:
        return  "0" + str(month)
    return str(month)





class GraphicsWindow(WindowBase):
    def __init__(self):
        super().__init__('designs/graphics.ui')
    def open(self):
        result = WindowBase.db.get_graphic(WindowBase.user_id)
        seriesColdtWater = QtCharts.QLineSeries()
        seriesHotWater = QtCharts.QLineSeries()
        seriesElectricity = QtCharts.QLineSeries()
        dates = []
        max_cw = 0
        max_hw = 0
        max_el = 0

        for month, year, _,_,_ in result:
            dates.append(f"{update_month_number(month)}.{year%100}")


        for month, year, cold_water, hot_water, electricity in result:
            ind_date = dates.index(f"{update_month_number(month)}.{year%100}")
            seriesHotWater.append(ind_date, hot_water)
            seriesColdtWater.append(ind_date, cold_water)
            seriesElectricity.append(ind_date, electricity)
            max_cw = max(max_cw,cold_water)
            max_hw = max(max_hw,hot_water)
            max_el = max(max_el, electricity)


        chart_layout = self.form.tab1layout

        chart_view = QtCharts.QChartView(self.form.tab)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        chart = QtCharts.QChart()
        chart.addSeries(seriesColdtWater)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(dates)
        axis_x.setTitleText('Временной промежуток')
        chart.addAxis(axis_x,Qt.AlignmentFlag.AlignBottom)
        seriesColdtWater.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, round(max_cw)+1 )
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%.1f")
        axis_y.setTitleText("Показатель")
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        seriesColdtWater.attachAxis(axis_y)


        chart_view.setChart(chart)
        chart_layout.addWidget(chart_view)

        chart_layout = self.form.tab2layout

        chart_view = QtCharts.QChartView(self.form.tab_2)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        chart = QtCharts.QChart()
        chart.addSeries(seriesHotWater)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(dates)
        axis_x.setTitleText('Временной промежуток')
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        seriesHotWater.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, round(max_hw) + 1)
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%.1f")
        axis_y.setTitleText("Показатель")
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        seriesHotWater.attachAxis(axis_y)

        chart_view.setChart(chart)
        chart_layout.addWidget(chart_view)

        chart_layout = self.form.tab3layout

        chart_view = QtCharts.QChartView(self.form.tab3)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        chart = QtCharts.QChart()
        chart.addSeries(seriesElectricity)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(dates)
        axis_x.setTitleText('Временной промежуток')
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        seriesElectricity.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, round(max_el) + 1)
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%.1f")
        axis_y.setTitleText("Показатель")
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        seriesElectricity.attachAxis(axis_y)

        chart_view.setChart(chart)
        chart_layout.addWidget(chart_view)

        self.window.show()

