import pandas as pd

#读取文件
file_name = 'C:\\Users\\wangkep\\Desktop\\双轨数据\\10.29\\1029--财务公司-11.30.xlsx'
# 指定sheet
sheet_name = '资金清理业务(补足留存)'

out_file = 'C:\\Users\\wangkep\\Desktop\\双轨数据\\10.29\\0816.csv'

data = pd.read_excel(file_name,sheet_name,index_col=0)

data.to_csv(out_file,encoding='utf-8')