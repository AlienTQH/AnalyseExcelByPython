#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/26 12:38
# @Author  : Tianqunhui
# @contact : tqunhui@163.com
# @File    : AnalyExcelMain.py
# @Software: PyCharm
import sys
from PyQt5.Qt import *
from IndexPane import IndexPane
from ResultPane import ResultPane


def open_result_pane(result_str):
    print(result_str)
    key_difference = ''
    val_difference = ''
    key_dict = result_str['key_diff']
    val_dict = result_str['val_diff']
    max_file_path = result_str['max_file_path']

    key_difference += '在文件[ %s ]' % max_file_path +'中多了以下内容:\n'
    for k, v in key_dict.items():
        key_difference += str(k) + ' : ' + str(v) + '\n'


    result_pane.textEdit.setText(key_difference)

    for k, v in val_dict.items():
        val_difference += str(k) + ' : ' + str(v) + '\n'

    result_pane.textEdit_2.setText(val_difference)
    result_pane.show()


if __name__ =='__main__':
    app = QApplication(sys.argv)
    index_pane = IndexPane()
    index_pane.call_result_signal.connect(open_result_pane)

    result_pane = ResultPane()

    index_pane.show()
    sys.exit(app.exec_())




