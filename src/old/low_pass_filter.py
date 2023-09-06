"""
程式碼功能:

"""
import re
from math import sqrt, atan2
from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/0118/stand_left.csv"

    f = open(FILE_NAME)

    start_line = 1              # 讀取數據的起始行
    end_line = 3                # 讀取數據的结束行

    # Set the length of CSI
    csi_length = 104

    # 設定取樣頻率和截止頻率
    fs = 20  # 取樣頻率
    cutoff_freq = 2  # 截止頻率

    # 計算歸一化的截止頻率
    nyquist_freq = 0.5 * fs
    normalized_cutoff_freq = cutoff_freq / nyquist_freq

    # 使用Butterworth濾波器設計低通濾波器
    order = 6
    b, a = butter(order, normalized_cutoff_freq, btype='low')

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
        # print('原本的子載波為:', csi_raw)

        # data subcarrier
        data_sub = csi_raw[12:64] + csi_raw[66:118]
        # print('data 子載波為:', data_sub)

        if len(csi_raw) != csi_length * 2:
            continue

        # Reshape array into 2D matrix
        csi_raw = np.array(csi_raw).reshape((104, 2))

        # Apply filter to real and imaginary parts separately
        real_filtered = filtfilt(b, a, data_sub[:, 0])
        imaginary_filtered = filtfilt(b, a, data_sub[:, 1])

        # Combine the real and imaginary parts
        csi_filtered = real_filtered + 1j * imaginary_filtered

        # Calculate the amplitude and phase
        amplitudes = np.abs(csi_filtered)
        phases = np.angle(csi_filtered, deg=True)

        # 計算FFT
        frequencies, amplitudes = fft(csi_filtered, fs)

        # 繪製圖形
        plt.plot(frequencies, amplitudes)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
        plt.show()

