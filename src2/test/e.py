# https://blog.csdn.net/jinghhz/article/details/123107354

import csv

list_a = ['张三', '李四', '王五']
list_b = ['23', '36', '31']
list_c = ['大学', '大专', '初中']
list_d = ['2020', '2022', ' 2015']
data_list = []
for a, b, c, d in zip(list_a, list_b, list_c, list_d):
    x = {}
    x['姓名'] = a
    x['年龄'] = b
    x['學历'] = c
    x['入职时间'] = d
    data_list.append(x)
#print(data_list)

with open("多列表写入csv.csv", 'w', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(['姓名', '年龄', '学历', '入职时间'])
    for n1 in data_list:
        writer.writerow(n1.values())
print("写入完成!")
