#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/26 12:29
# @Author  : Tianqunhui
# @contact : tqunhui@163.com
# @File    : ResultPane.py
# @Software: PyCharm


import os
import pandas as pd

from PyQt5 import QtCore,QtGui
from PyQt5.Qt import *
from resource.result_ui import Ui_Form


class ResultPane(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


    def close_the_widget(self):
        print('close')
        # self.close()
        self.hide()



if __name__ =='__main__':
    import sys
    app = QApplication(sys.argv)
    window = ResultPane()
    window.show()
    sys.exit(app.exec_())