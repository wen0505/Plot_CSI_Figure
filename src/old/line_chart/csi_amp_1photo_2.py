"""
程式碼功能:
能夠讀取兩個 csv 檔案的 csi data ，可以指定要從哪一行開始讀取並控制需要顯示的列數，再分別計算子載波的振幅和相位值，然後呈現在同一張圖片上
"""
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/csv_raw/manned.csv"
    FILE_NAME2 = "C:/PythonProject/plot_csi_figure/src/old/csv_raw/unmanned.csv"

    f1 = open(FILE_NAME1)
    f2 = open(FILE_NAME2)

    start_line = 1              # 讀取數據的起始行
    end_line = 50                # 讀取數據的结束行

    for j1, l1 in enumerate(f1.readlines()):
        if j1 < start_line:
            continue
        if j1 > end_line:
            break

        imaginary1 = []
        real1 = []
        amplitudes1 = []
        phase1 = []

        # Parse string to create integer list
        csi_string1 = re.findall(r"\[(.*)\]", l1)[0]
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

        amplitudes_data1 = amplitudes1[6:32] + amplitudes1[33:59]
        plt.plot(range(len(amplitudes_data1)), amplitudes_data1, 'b', linewidth=0.6, label='manned')

    for j2, l2 in enumerate(f2.readlines()):
        if j2 < start_line:
            continue
        if j2 > end_line:
            break

        imaginary2 = []
        real2 = []
        amplitudes2 = []
        phase2 = []

        # Parse string to create integer list
        csi_string2 = re.findall(r"\[(.*)\]", l2)[0]
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

        amplitudes_data2 = amplitudes2[6:32] + amplitudes2[33:59]
        plt.plot(range(len(amplitudes_data2)), amplitudes_data2, 'r', linewidth=0.6, label='unmanned')

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']    # 用來正常顯示中文標籤
    plt.rcParams['axes.unicode_minus'] = False                  # 用來正常顯示負號
    plt.title('室內的狀態 - 振幅', fontsize=24)
    plt.xlabel('子載波數 (單位:個)', fontsize=18)
    plt.ylabel('振幅 (單位:dB)', fontsize=18)
    plt.axvline(x=26, c='orange', ls="--", lw=0.5)   # 切割子載波的上下部分，參考 https://www.delftstack.com/zh-tw/howto/matplotlib/how-to-plot-horizontal-and-vertical-line-in-matplotlib/

    # 在 for 迴圈外添加圖例，並指定為不重複的圖例
    handles, labels = plt.gca().get_legend_handles_labels()
    unique_labels = list(set(labels))
    handles = [handles[labels.index(label)] for label in unique_labels]
    plt.legend(handles, unique_labels)

    plt.show()
