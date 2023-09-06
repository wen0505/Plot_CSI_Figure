"""
程式碼功能:
能夠讀取一個 csv 檔案的 csi data ，可以指定要從哪一行開始讀取並控制需要顯示的列數，再分別計算子載波的振幅和相位值，然後呈現在同一張圖片上
"""
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    # FILE_NAME = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/0118/no-people.csv"
    FILE_NAME = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/0729/stand.csv"
    # unmanned、walk、stand、sit、squat

    f = open(FILE_NAME)

    start_line = 600              # 讀取數據的起始行
    end_line = start_line + 100                # 讀取數據的结束行
    sub_index = list(range(1, 53))
    # sub_index = list(range(1, 65))
    # print(sub_index)

    for j, l in enumerate(f.readlines()):
        if j < start_line:
            continue
        if j > end_line:
            break
        imaginary = []
        real = []
        amplitudes = []
        phases = []

        # Parse string to create integer list
        csi_string = re.findall(r"\[(.*)\]", l)[0]
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
            phases.append(atan2(imaginary[i], real[i]))

        amplitudes_data = amplitudes[6:32] + amplitudes[33:59]
        # print(len(amplitudes_data))

        plt.plot(sub_index, amplitudes_data, 'b', linewidth=0.6)
        plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']    # 用來正常顯示中文標籤
        plt.rcParams['axes.unicode_minus'] = False                  # 用來正常顯示負號
        plt.ylim(0, 40)
        # plt.ylim(-5, 5)
        plt.title('站立', fontsize=24)
        # 無人、行走、站立、坐下、蹲下
        # unmanned、walk、stand、sit、squat
        plt.xlabel('子載波數 (單位:個)', fontsize=18)
        plt.ylabel('振幅 (單位:dB)', fontsize=18)
        # plt.ylabel('相位 (單位:°)', fontsize=18)
        plt.axvline(x=26, c='red', ls="--", lw=0.5)   # 切割子載波的上下部分，參考 https://www.delftstack.com/zh-tw/howto/matplotlib/how-to-plot-horizontal-and-vertical-line-in-matplotlib/

    plt.show()
