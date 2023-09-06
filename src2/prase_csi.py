import csv
import re
from math import sqrt, atan2
from os.path import basename
from pathlib import Path

import pandas as pd
from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """
    loop = 0

    no_people = []
    people = []

    imaginary1 = []
    imaginary2 = []
    real1 = []
    real2 = []
    amplitudes1 = []
    amplitudes2 = []

    files = Path('C:/PythonProject/plot_csi_figure/src2').glob('*.csv')
    for file in files:
        filename = basename(file).rsplit('.', 1)[0]
        with open(file) as f:
            csvreader = csv.reader(f, delimiter=',', quotechar='"')
            for line in range(0):  # 0代表从文件第一行开始读取
                next(csvreader)

    for j, l in enumerate(f.readlines()):
        for row in f:
            n = no_people.append(row[0:63])
            p = people.append(row[64:127])

        # Parse string to create integer list
        csi_string1 = re.findall(r"\[(.*)\]", n)[0]
        csi_string2 = re.findall(r"\[(.*)\]", p)[0]
        csi_raw1 = [int(x) for x in csi_string1.split(" ") if x != '']
        csi_raw2 = [int(x) for x in csi_string2.split(" ") if x != '']

        # Create list of imaginary and real numbers from CSI
        for i in range(len(csi_raw1)):
            if i % 2 == 0:
                imaginary1.append(csi_raw1[i])
            else:
                real1.append(csi_raw1[i])
        for j in range(len(csi_raw2)):
            if j % 2 == 0:
                imaginary2.append(csi_raw2[j])
            else:
                real2.append(csi_raw2[j])

        # Transform imaginary and real into amplitude
        for i in range(int(len(csi_raw1) / 2)):
            amplitudes1.append(sqrt(imaginary1[i] ** 2 + real1[i] ** 2))
        for j in range(int(len(csi_raw2) / 2)):
            amplitudes2.append(sqrt(imaginary2[j] ** 2 + real2[j] ** 2))

        if loop >= 4:
            break

        plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']    # 用來正常顯示中文標籤
        plt.rcParams['axes.unicode_minus'] = False                  # 用來正常顯示負號
        plt.suptitle('室內的狀態')
        plt.subplot(2*2, loop+1)
        plt.title("frame"+str(loop))
        plt.xlim(0, 54)
        plt.ylim(0, 50)
        # plt.plot(amplitudes[6:59])
        plt.plot(amplitudes1[5:60], 'r', linewidth=5, label='沒人')
        plt.plot(amplitudes2[5:60], 'c', linewidth=5, label='有人')

        loop += 1

plt.show(block=True)
