import xlrd
import csv
import os
from xlrd import open_workbook

# 生成的csv文件名
csv_file_name = 'excel_to_csv.csv'

# 要转换的excel文件
excel_file = 'C:\\Users\\wangkep\\Desktop\\双轨数据\\10.29\\1029--财务公司-11.30.xlsx'

get_sheets = ['资金清理业务(超额上收)']

def get_excel_sheet(excel_file):
    # 获取Excel文件sheet页
    table = open_workbook(excel_file)
    print(get_sheets)
    for i in get_sheets:
        get_each_sheet = table.sheet_by_name(i)
        #print(get_each_sheet)
        count_rows = get_each_sheet.nrows
        count_cols = get_each_sheet.ncols
        print(count_rows,count_cols)
        for j in range(count_rows):
            col_values = get_each_sheet.row_values(j, start_colx=9, end_colx=10)
            print(col_values)


# def get_excel_header(excel_name_for_header):
#     # 获取表头，并将表头全部变为小写
#     workbook = xlrd.open_workbook(excel_name_for_header)
#     table = workbook.sheet_by_index(0)
#     # row_value = table.row_values(0)
#     row_value = [i.lower() for i in table.row_values(0)]
#     return row_value


def read_excel(excel_name):
    # 读取Excel文件每一行内容到一个列表中
    workbook = xlrd.open_workbook(excel_name)
    table = workbook.sheet_by_index(0)  # 读取第一个sheet
    nrows = table.nrows
    ncols = table.ncols
    # 跳过表头，从第一行数据开始读
    for rows_read in range(1, nrows):
        # 每行的所有单元格内容组成一个列表
        row_value = []
        for cols_read in range(ncols):
            # 获取单元格数据类型
            ctype = table.cell(rows_read, cols_read).ctype
            # 获取单元格数据
            nu_str = table.cell(rows_read, cols_read).value
            # 判断返回类型
            # 0 empty,1 string, 2 number(都是浮点), 3 date, 4 boolean, 5 error
            # 是2（浮点数）的要改为int
            if ctype == 2:
                nu_str = int(nu_str)
            row_value.append(nu_str)
        yield row_value


def xlsx_to_csv(csv_file_name, row_value):
    # 生成csv文件
    with open(csv_file_name, 'a', encoding='utf-8', newline='') as f:  # newline=''不加会多空行
        write = csv.writer(f)
        write.writerow(row_value)


if __name__ == '__main__':
    get_excel_sheet(excel_file)
