import csv
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME1 = "people.csv"
    FILE_NAME2 = "no-people.csv"

    f1 = open(FILE_NAME1)
    f2 = open(FILE_NAME2)

    imaginary1 = []
    imaginary2 = []
    real1 = []
    real2 = []
    amplitudes = []
    amplitudes1 = []
    amplitudes2 = []
    phases1 = []
    phases2 = []

    loop1 = 0
    loop2 = 0
    loop3 = 0

    for j1, l1 in enumerate(f1.readlines()):
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
            amplitudes1.append(round(sqrt(imaginary1[i] ** 2 + real1[i] ** 2), 3))
            phases1.append(atan2(imaginary1[i], real1[i]))

        if loop1 >= 8*8:
            break

        loop1 += 1


    for j2, l2 in enumerate(f2.readlines()):
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
            amplitudes2.append(round(sqrt(imaginary2[i] ** 2 + real2[i] ** 2), 3))
            phases2.append(atan2(imaginary2[i], real2[i]))

        if loop2 >= 8*8:
            break

        loop2 += 1

    for a, b in zip(amplitudes1, amplitudes2):
        x = {}
        x['有人'] = a
        x['沒人'] = b
        amplitudes.append(x)

        with open('compare.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['有人', '沒人'])
            # writer.writerow(amplitudes)
            for n in amplitudes:
                writer.writerow(n.values())
            # if loop3 >= 63:
            #    break

            # loop3 += 1

    print("寫入完成!")
