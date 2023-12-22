# print("Hello world")
# for i in range(1000):
#     print(f"this is No.{i} hello world")

# asdad

# tou 35, zu 94, 
# ji 1, 2  tuzi 1, 4

# (0-35)
# [0 36)

# 今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？
for ji in range(36):
    print(f'now ji is {ji} zhi')
    tu = 35 - ji
    print(f'now tu is {tu} zhi')
    print(f"now total legs  is {ji * 2 + tu * 4}")
    if ji * 2 + tu * 4 == 94:
        print(f"chiken has {ji} zhi, tuzi has {tu} zhi")
        print(f"ji suan jie shu")
        break




# 基础类型
# 1. 123
# 2. '今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何', "今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？" 
# 3. list a = []
"""
    a = []
    a.append(1)
    print(a)
"""
# 4. set 
# b = set([1, 2, 3, 1])
# print(b)

# 5. dict {}
# c = {}
# c['wangqing'] = '182'
# c['lei'] = '181'
# print(c)

import csv

# data = [["name", "age", "math", "English"], ["lei", 30, 90, 90], ["qing", 30, 80, 80]]
data = [["asdas", "asd", "math", "English", "average"], ["lei", 30, 90, 90], ["qing", 30, 80, 80]]

# data = [['1'], ['2'], ['3']]


file_path = 'output.csv'
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(data[0])
    writer.writerows(data[1:])

print(f"Data has been written to {file_path}")




csv_reader = csv.reader(open('output.csv'))
for row in csv_reader:
    print(row)



