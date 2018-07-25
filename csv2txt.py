# -*- coding=utf-8 -*-
##############################
# description:
# 将官方的csv转换为txt，每行格式如下：
# car x_min x_max y_min y_max
##############################

import pandas as pd

InPath = "AITJIData/train_b.csv"
OutPath = "AITJIData/train_b_1k_txt"

train_data = pd.read_csv(InPath)

for i in range(len(train_data)):
    OutFilePath = OutPath + "/" + train_data['name'][i][:-4] + '.txt'
    try:
        coords = train_data['coordinate'][i].split(';')
    except:
        print('------------warning!! ' + train_data['name'][i] + ' has no coordinates!!------------')
        continue

    with open(OutFilePath,'w+') as f:
        for c in coords:
            # 先将str转换为float，再转换为int，csv中长宽可能有小数点
            if c == '':
                print('------------coordinate is empty!------------')
                continue
            x = float(c.split('_')[0])  # int(float(c.split('_')[0])) #框的左上角横坐标
            y = float(c.split('_')[1])  # int(float(c.split('_')[1])) #框的左上角纵坐标
            w = float(c.split('_')[2])  # int(float(c.split('_')[2])) #框的宽度
            h = float(c.split('_')[3])  # int(float(c.split('_')[3])) #框的高度
            x_min = x
            x_max = x + w
            y_min = y
            y_max = y + h
            f.write('car' + ' ' + str(x_min) + ' ' + str(x_max) + ' ' + str(y_min) + ' ' + str(y_max) + '\n')