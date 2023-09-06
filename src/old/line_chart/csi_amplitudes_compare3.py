"""
程式碼功能:
能夠讀取三個 csv 檔案的 csi data ，可以指定要從哪一行開始讀取並控制需要顯示的列數，再分別計算子載波的振幅和相位值，並呈現在 n*n 的子圖上
"""
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/0118/stand_left.csv"
    FILE_NAME2 = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/0118/stand_right.csv"
    FILE_NAME3 = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/0118/stand_center.csv"

    f1 = open(FILE_NAME1)
    f2 = open(FILE_NAME2)
    f3 = open(FILE_NAME3)

    j0 = 64                      # 要從第 n 行開始讀取需要設定為 loop == n-1

    loop = 100                   # 設定總共要顯示多少個子圖
    loop0 = int(sqrt(loop))     # 設定子圖為 loop0 * loop0 的形式
    loop1 = 0
    loop2 = 0
    loop3 = 0

    for j1, l1 in enumerate(f1.readlines()):
        if j1 >= j0:
            imaginary1 = []
            real1 = []
            amplitudes1 = []
            amplitudes1_data = []
            phase1 = []

            # Parse string to create integer list
            csi_string1 = re.findall(r"\[(.*)\]", l1)[0]
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
                amplitudes1.append(sqrt(imaginary1[i] ** 2 + real1[i] ** 2))
                phase1.append(atan2(imaginary1[i], real1[i]))

            if loop1 >= loop:
                break

            plt.subplot(loop0, loop0, loop1+1)
            plt.title("frame"+str(loop1), fontsize=8)
            plt.xlim(0, 51)             # 設定座標軸的範圍
            plt.ylim(0, 40)
            plt.xticks(fontsize=6)      # 設定座標軸刻度的文字大小
            plt.yticks(fontsize=6)
            plt.axvline(x=26, c='orange', ls="--", lw=0.5)   # 切割子載波的上下部分，參考 https://www.delftstack.com/zh-tw/howto/matplotlib/how-to-plot-horizontal-and-vertical-line-in-matplotlib/
            amplitudes1_data = amplitudes1[6:32] + amplitudes1[33:59]
            plt.plot(amplitudes1_data, 'r', linewidth=0.6, label='stand-left')

            loop1 += 1

    for j2, l2 in enumerate(f2.readlines()):
        if j2 >= j0:
            imaginary2 = []
            real2 = []
            amplitudes2 = []
            amplitudes2_data = []
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
                amplitudes2.append(sqrt(imaginary2[i] ** 2 + real2[i] ** 2))
                phase2.append(atan2(imaginary2[i], real2[i]))

            if loop2 >= loop:
                break

            plt.subplot(loop0, loop0, loop2+1)
            amplitudes2_data = amplitudes2[6:32] + amplitudes2[33:59]
            plt.plot(amplitudes2_data, 'b', linewidth=0.6, label='stand-right')

            loop2 += 1

    for j3, l3 in enumerate(f3.readlines()):
        if j3 >= j0:
            imaginary3 = []
            real3 = []
            amplitudes3 = []
            amplitudes3_data = []
            phases3 = []

            # Parse string to create integer list
            csi_string3 = re.findall(r"\[(.*)\]", l3)[0]
            csi_raw3 = [int(x) for x in csi_string3.split(" ") if x != '']

            # Create list of imaginary and real numbers from CSI
            for i in range(len(csi_raw3)):
                if i % 2 == 0:
                    imaginary3.append(csi_raw3[i])
                else:
                    real3.append(csi_raw3[i])

            # Transform imaginary and real into amplitude and phase
            for i in range(int(len(csi_raw3) / 2)):
                amplitudes3.append(sqrt(imaginary3[i] ** 2 + real3[i] ** 2))
                phases3.append(atan2(imaginary3[i], real3[i]))

            if loop3 >= loop:
                break

            plt.subplot(loop0, loop0, loop3+1)
            amplitudes3_data = amplitudes3[6:32] + amplitudes3[33:59]
            plt.plot(amplitudes3_data, 'g', linewidth=0.6, label='stand-center')

            loop3 += 1

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']    # 用來正常顯示中文標籤
    plt.rcParams['axes.unicode_minus'] = False                  # 用來正常顯示負號
    plt.suptitle('室內的狀態 - 振幅', fontsize=24)
    # plt.suptitle('動作差異', fontsize=24)
    plt.text(-290, -25, '子載波數 (單位:個)', fontsize=16, va='center')
    plt.text(-570, 235, '振幅 (單位:dB)', fontsize=16, va='center', rotation='vertical')
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')     # 圖例可以通過使用 bbox_to_anchor 放置在 Matplotlib 中的繪圖之外

plt.show(block=True)
