"""
程式碼功能:
能夠讀取一個 csv 檔案的 csi data ，可以指定要從哪一行開始讀取並控制需要顯示的列數，再分別計算子載波的振幅值，並呈現在 n*n 的子圖上
"""
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/0118/stand_left.csv"

    f = open(FILE_NAME)

    j0 = 0                      # 要從第 n 行開始讀取需要設定為 loop == n-1

    loop = 16                # 設定總共要顯示多少個子圖
    loop0 = int(sqrt(loop))     # 設定子圖為 loop0 * loop0 的形式
    loop1 = 0

    for j, l in enumerate(f.readlines()):
        if j >= j0:
            imaginary = []
            real = []
            amplitudes = []
            phases = []

            # Parse string to create integer list
            csi_string = re.findall(r"\[(.*)\]", l)[0]
            # print(type(csi_string))
            # csi_raw = (csi_string.split()[1]).split()
            csi_raw = [int(x) for x in csi_string.split(" ") if x != '']

            # Create list of imaginary and real numbers from CSI
            for i in range(len(csi_raw)):
                if i % 2 == 0:
                    imaginary.append(csi_raw[i])
                else:
                    real.append(csi_raw[i])

            # Transform imaginary and real into amplitude and phase
            for i in range(int(len(csi_raw) / 2)):
                amplitudes.append(sqrt(imaginary[i] ** 2 + real[i] ** 2))
                # amplitudes.append(format(sqrt(imaginary[i] ** 2 + real[i] ** 2), '.3f'))
                phases.append(atan2(imaginary[i], real[i]))

            if loop1 >= loop:
                break

            plt.subplot(loop0, loop0, loop1+1)
            plt.title("frame"+str(loop1), fontsize=8)
            plt.xlim(0, 54)             # 設定座標軸的範圍
            plt.ylim(0, 50)
            plt.xticks(fontsize=12)      # 設定座標軸刻度的文字大小
            plt.yticks(fontsize=12)
            # plt.plot(amplitudes[6:59])
            plt.plot(amplitudes[5:60], 'b', linewidth=0.8)

            loop1 += 1

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']    # 用來正常顯示中文標籤
    plt.rcParams['axes.unicode_minus'] = False                  # 用來正常顯示負號
    plt.suptitle('stand left - 振幅', fontsize=24)
    # plt.text(-370, -50, '子載波數 (單位:個)', fontsize=16, va='center')
    # plt.text(-750, 350, '振幅 (單位:dB)', fontsize=16, va='center', rotation='vertical')

plt.show(block=True)
