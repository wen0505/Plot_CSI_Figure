import csv
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME = "C:/PythonProject/plot_csi_figure/src/old/CSI_DATA/1205/people/people-1.csv"

    f = open(FILE_NAME)

    loop = 0

    for j, l in enumerate(f.readlines()):
        imaginary = []
        real = []
        amplitudes = []
        phases = []

        # Parse string to create integer list
        csi_string = re.findall(r"\[(.*)\]", l)[0]
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
            phases.append(atan2(imaginary[i], real[i]))

        if loop >= 8*8:
            break

        loop += 1

with open('compare_p.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\n')
    writer.writerow(['有人'])
    writer.writerow(amplitudes)

print("寫入完成!")
