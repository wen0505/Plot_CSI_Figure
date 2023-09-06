"""
程式碼功能:
能夠讀取兩個 csv 檔案的 csi data ，可以指定要從哪一行開始讀取並控制需要顯示的列數，再分別計算子載波的相位值，並呈現在 n*n 的子圖上
"""
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/1205/no-people/no-people-1.csv"
    FILE_NAME2 = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/1205/people/people-1.csv"

    f1 = open(FILE_NAME1)
    f2 = open(FILE_NAME2)

    loop = 144                   # 設定總共要顯示多少個子圖
    loop0 = int(sqrt(loop))     # 設定子圖為 loop0 * loop0 的形式
    loop1 = 0
    loop2 = 0

    for j1, l1 in enumerate(f1.readlines()):
        imaginary1 = []
        real1 = []
        phase1 = []

        # Parse string to create integer list
        csi_string1 = re.findall(r"\[(.*)\]", l1)[0]
        # print(type(csi_string))
        # csi_raw = (csi_string.split()[1]).split()
        csi_raw1 = [int(x) for x in csi_string1.split(" ") if x != '']

        # Create list of imaginary and real numbers from CSI
        for i in range(len(csi_raw1)):
            if i % 2 == 0:
                imaginary1.append(csi_raw1[i])
            else:
                real1.append(csi_raw1[i])

        # Transform imaginary and real into amplitude and phase
        for i in range(int(len(csi_raw1) / 2)):
            phase1.append(atan2(imaginary1[i], real1[i]))

        if loop1 >= loop:
            break

        plt.subplot(loop0, loop0, loop1+1)
        plt.title("frame"+str(loop1), fontsize=8)
        plt.xlim(0, 64)             # 設定座標軸的範圍
        plt.ylim(-5, 5)
        plt.xticks(fontsize=6)      # 設定座標軸刻度的文字大小
        plt.yticks(fontsize=6)
        plt.plot(phase1, 'r', linewidth=0.6, label='unmanned')

        loop1 += 1

    for j2, l2 in enumerate(f2.readlines()):
        imaginary2 = []
        real2 = []
        amplitudes2 = []
        phase2 = []

        # Parse string to create integer list
        csi_string2 = re.findall(r"\[(.*)\]", l2)[0]
        # print(type(csi_string))
        # csi_raw = (csi_string.split()[1]).split()
        csi_raw2 = [int(x) for x in csi_string2.split(" ") if x != '']

        # Create list of imaginary and real numbers from CSI
        for i in range(len(csi_raw2)):
            if i % 2 == 0:
                imaginary2.append(csi_raw2[i])
            else:
                real2.append(csi_raw2[i])

        # Transform imaginary and real into amplitude and phase
        for i in range(int(len(csi_raw2) / 2)):
            phase2.append(atan2(imaginary2[i], real2[i]))

        if loop2 >= loop:
            break

        plt.subplot(loop0, loop0, loop2+1)
        plt.plot(phase2, 'b', linewidth=0.6, label='manned')

        loop2 += 1

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']    # 用來正常顯示中文標籤
    plt.rcParams['axes.unicode_minus'] = False                  # 用來正常顯示負號
    plt.suptitle('室內的狀態 - 相位', fontsize=24)
    # plt.suptitle('動作差異', fontsize=24)
    # 12*12 用
    plt.text(-450, -12, '子載波數 (單位:個)', fontsize=16, va='center')
    plt.text(-880, 66, '相位 (單位:°)', fontsize=16, va='center', rotation='vertical')
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')     # 圖例可以通過使用 bbox_to_anchor 放置在 Matplotlib 中的繪圖之外

plt.show(block=True)
