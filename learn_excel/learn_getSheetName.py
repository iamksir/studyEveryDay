# -*- coding:utf-8 -*-

'''
本代码的目的是获取多个excl的sheet名，并输出到指定文件中
'''

import sys
import xlrd
import os
import logging


# 设置logging.basicConfig()方法的参数和配置logging.basicConfig函数
FORMAT = '[%(funcName)s: %(lineno)d]: %(message)s'
LEVEL = logging.INFO
logging.basicConfig(level = LEVEL, format=FORMAT)

# 保存输出sheet name
output_file = 'D:/国电投/外围与核心交互点/SheetNameList.txt'

# init function
def get_obj_list(dir_name):
    filelist = os.listdir(dir_name)
    for item in filelist :
        item = dir_name + item
        if os.path.isfile(item) and ( item[-4:] == '.xls' or item[-5:] == '.xlsx'):
            if item.find("$") != -1 or item.find("csr_example") != -1 :
                continue
            GetSheetNameList(item)
        elif os.path.isdir(item):
            item = item + '/'
            new_obj_list = []
            new_obj_list = get_obj_list(item)


# get sheet name and save in output_file
def GetSheetNameList(excelName):
    fd = open(output_file, 'a+')
    fd.write(excelName + '\n')
    excelfd = xlrd.open_workbook(excelName)
    for sheetName in excelfd.sheet_names():
        fd.write(sheetName + '\n')
    fd.close()


if __name__ == "__main__":
    if os.path.exists(output_file):
        os.remove(output_file)
    get_obj_list('D:/国电投/外围与核心交互点/')