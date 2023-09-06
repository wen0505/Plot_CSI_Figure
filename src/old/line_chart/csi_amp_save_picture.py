"""
程式碼功能:
能夠讀取一個 csv 檔案的 csi data ，可以指定要從哪一行開始讀取並控制需要顯示的列數，，再分別計算子載波的振幅和相位值，並儲存成折線圖
p.s. 需要先建立儲存圖片的資料夾，否則會無法執行程式
參考 : https://blog.csdn.net/weixin_45736572/article/details/106423181?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-106423181-blog-111452807.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-106423181-blog-111452807.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=2
"""
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/0608/squat.csv"  # 原始 csv 檔案
    PATH = "C:/PythonProject/plot_csi_figure/src/old/dataset/0608/line/"  # 輸出圖片的路徑

    f = open(FILE_NAME)

    j0 = 0                      # 要從第 n 行開始讀取需要設定為 loop == n-1

    loop = 0
    loop_n = 4                        # 設定總共要輸出多少張圖片

    for j, l in enumerate(f.readlines()):
        if j >= j0:
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

            # 將數據子載波的上、下兩部分整合成一個 list
            data_sub = [element for e in [amplitudes[6:32], amplitudes[33:59]] for element in e]
            # print('數據子載波 : ', data_sub)

            if loop >= loop_n:
                break

            loop += 1

            plt.xlim(0, 51)
            plt.ylim(0, 40)
            plt.plot(data_sub, 'b', linewidth=1)
            address = PATH + "unmanned-{}.png".format(j)   # 編輯圖片的名稱
            plt.savefig(address)                            # 儲存圖片
            plt.clf()                                       # 清除 Matplotlib 中的整個內容，包含當前座標軸

    print("圖片儲存完成!")
