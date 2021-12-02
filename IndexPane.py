#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 21:34
# @Author  : Tianqunhui
# @contact : tqunhui@163.com
# @File    : IndexPane.py
# @Software: PyCharm

import os
import pandas as pd

from PyQt5.Qt import *
from resource.index_ui import Ui_Form


class IndexPane(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.init_parm()


    def init_parm(self):
        print('初始化参数')
        self.file_path_a = None
        self.file_path_b = None
        self.key_a_col = None
        self.key_b_col = None
        self.a_col = None
        self.b_col = None
        #
        # self.lineEdit_a.setText(self.file_path_a)
        # self.lineEdit_b.setText(self.file_path_b)
        # self.lineEdit_key_a_col.setText(self.key_a_col)
        # self.lineEdit_key_b_col.setText(self.key_b_col)
        # self.lineEdit_a_col.setText(self.a_col)
        # self.lineEdit_b_col.setText(self.b_col)

    def select_a_file(self):
        print('[ 打开文件 ] A')
        file_paths = QFileDialog.getOpenFileName(self, '打开A文件', './',("Tables (*.xlsx *.xls *.csv)"))
        self.file_path_a = file_paths[0]
        if self.file_path_a is not '':
            self.lineEdit_a.setText(self.file_path_a)


    def select_b_file(self):
        print('[ 打开文件 ] B')
        file_paths = QFileDialog.getOpenFileName(self, '打开B文件', './', ("Tables (*.xlsx *.xls *.csv)"))
        self.file_path_b = file_paths[0]
        if self.file_path_b is not '':
            self.lineEdit_b.setText(self.file_path_b)


    def get_path_a(self):
        self.file_path_a = self.lineEdit_a.text()
        print('A path')

    def get_path_b(self):
        self.file_path_b = self.lineEdit_b.text()
        print('B path')

    def get_key_a_col(self):
        print('[输入列数] key a col')
        self.key_a_col = self.lineEdit_key_a_col.text()

    def get_key_b_col(self):
        print('[输入列数] key b col')
        self.key_b_col = self.lineEdit_key_b_col.text()


    def get_a_col(self):
        print('[输入列数] a col')
        self.a_col = self.lineEdit_a_col.text()

    def get_b_col(self):
        print('[输入列数] b col')
        self.b_col = self.lineEdit_b_col.text()

    def check_input(self):
        print('[读取数据]')
        data_a = pd.read_excel(self.file_path_a)
        data_b = pd.read_excel(self.file_path_b)

        print(data_a)

        key_a_col = int(self.key_a_col)-1
        key_b_col = int(self.key_b_col)-1
        print(self.a_col, self.b_col)
        compare_a_cols = [int(x) for x in self.a_col.split(' ')]
        compare_b_cols = [int(x) for x in self.b_col.split(' ')]

        print('[读取完毕]')
        # print(data_a, data_b)
        print(compare_a_cols,compare_b_cols)
        print(key_a_col, key_b_col)

        data_key_a_list = list(data_a.iloc[:, key_a_col])
        data_key_b_list = list(data_b.iloc[:, key_b_col])

        max_list = data_key_a_list
        max_data = data_a
        max_compare_a_cols = compare_a_cols

        min_list = data_key_b_list
        min_data = data_b
        min_compare_b_cols = compare_b_cols

        if len(data_key_a_list) == len(data_key_b_list):
            pass
        elif len(data_key_a_list) < len(data_key_b_list):
            max_list = data_key_b_list
            max_data = data_b
            max_compare_b_cols = compare_b_cols

            min_list = data_key_a_list
            min_data = data_a
            min_compare_a_cols = compare_a_cols

        key_different = {}
        val_different = {}

        for i in range(len(max_list)):
            current_key = max_list[i]
            if current_key not in min_list:
                key_different[i+2] = current_key
            else:
                cur_index_key_min = min_list.index(current_key)
                for j in range(len(max_compare_a_cols)):
                    current_val_max = max_data.iloc[i, max_compare_a_cols[j]-1]
                    current_val_min = min_data.iloc[cur_index_key_min, min_compare_b_cols[j]-1]
                    if pd.isna(current_val_max) and pd.isna(current_val_min):
                        print('nan')
                    elif current_val_max != current_val_min:
                        val_different[i+2] = current_key

        print('[比较结束]')
        print(key_different)
        print(val_different)

        QMessageBox.information(self, '结果', '缺失 %s, 值不同的是 %s' % (str(key_different), str(val_different)))



    def run_the_compare(self):
        print('[执行对比]Run')
        if (not str.isdigit(self.key_a_col.replace(' ',''))) \
                or (not str.isdigit(self.key_b_col.replace(' ',''))) \
                or not( str.isdigit(self.a_col.replace(' ',''))) \
                or (not str.isdigit(self.b_col.replace(' ',''))):
            QMessageBox.warning(self, '错误', '输入的列数不是数字')

        elif not os.path.exists(self.file_path_a) or not os.path.exists(self.file_path_b):
            QMessageBox.warning(self, '错误', '输入的路径不存在')
        else:
            print('[ 输入正确 ]')
            self.check_input()



if __name__ =='__main__':
    import sys
    app = QApplication(sys.argv)
    window = IndexPane()
    window.show()
    sys.exit(app.exec_())


