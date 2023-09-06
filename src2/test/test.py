import csv
import os
import re
from os.path import basename

import pandas as pd

import matplotlib.pyplot as plt

from pathlib import Path

files = Path('/src2').glob('*.csv')

################################################
#for file in files:
#    df = pd.read_csv(file)
#    print(df)
################################################

################################################
no_people = []
people = []
for file in files:
    filename = basename(file).rsplit('.', 1)[0]         #用.来分割文件名，取前半部分，例如XX.csv，取XX
    #     print('\r'+ filename + "  ", flush = True)
    with open(file) as f:
        csvreader = csv.reader(f, delimiter = ",", quotechar='"')
        for line in range(0):  #0代表从文件第一行开始读取
            next(csvreader)
        for row in csvreader:
            n = no_people.append(row[0])
            p = people.append(row[1])          #读取数据，放入list
        # Parse string to create integer list
        csi_string1 = re.findall(r"\[(.*)\]", n)[0]
        csi_string2 = re.findall(r"\[(.*)\]", p)[0]
################################################

################################################
# https://ithelp.ithome.com.tw/questions/10199712
#path = "./" #路徑位置"./"為相對路徑

#i = 0
#files = os.walk(path) #遞迴印出資料夾中所有目錄及檔名
#for root, folder, file in files: #把他接起來
#    i = i+1
#    print("\n第",i,"次迴圈")
#    print("路徑：", root)
#    print("子目錄：", folder)
#    print("檔案：", file)

#    for file_name in file:
#        if file_name.split(".", 1)[-1] == "csv": #判斷附檔名 你也可以用正規表達式
#            print("開啟",file_name)
#            df = pd.read_csv(file_name)
################################################
