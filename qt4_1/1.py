#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *  # компоненты интерфейса
 
# Каждое приложение должно создать объект QApplication
# sys.argv - список аргументов командной строки
application = QApplication(sys.argv)
 
# QWidget - базовый класс для всех объектов интерфейса
# пользователя; если использовать для виджета конструктор
# без родителя, такой виджет станет окном
widget = QWidget()
 
widget.resize(320, 240)  # изменить размеры виджета
widget.setWindowTitle("Hello, World!")  # установить заголовок
widget.show()  # отобразить окно на экране
 
sys.exit(application.exec_()) 