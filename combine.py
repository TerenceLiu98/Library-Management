import os
import pandas as pd


def combineCSV():
    path = 'Data/CSV/'  # 设置csv所在文件夹
    files = os.listdir(path)  # 获取文件夹下所有文件名
    df1 = pd.read_csv(path + files[0], encoding='utf-8')  # 读取首个csv文件，保存到df1中

    for file in files[1:]:
        df2 = pd.read_csv(path + file, encoding='utf-8')  # 打开csv文件，注意编码问题，保存到df2中
        df1 = pd.concat([df1, df2], axis=0, ignore_index=True, sort=False)  # 将df2数据与df1合并

    df1 = df1.drop_duplicates()  # 去重
    df1 = df1.reset_index(drop=True)  # 重新生成index
    df1.to_csv(path + 'total.csv')  # 将结果保存为新的csv文件
    return ("Combination done!")


combineCSV()
