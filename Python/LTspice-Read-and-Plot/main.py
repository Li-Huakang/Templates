import chardet
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

import os
import re

# 数据文件名 LTspice输出.txt格式
txtfilename = 'data' + '.txt'

# 检测字符串编码
with open(txtfilename, 'rb') as f:
    txt = f.read(1000)
    c = chardet.detect(txt)
    print(c)
# 转换字符编码到utf-8
encoding = c['encoding']
if encoding != 'utf-8':
    with open(txtfilename, 'r', encoding=encoding) as f:
        text = f.read()
    with open(txtfilename, 'w', encoding='utf-8') as f:
        f.write(text)

###################################################
#   获取数据
###################################################
data = {}
keys = ["data"]  # 默认key为'data'
# 数据获取方法data[key[i]]
labels = {keys[0]: ["data", 0]}  # 标签名格式必须为[A-Za-z0-9_]，默认label为["data",0]
# 数据获取方法labels[key[i]]
# 将数据转换成列表 并且存储标签


def toNumList(linelist):  # 辅助方法，判断并保存标签信息和数据信息
    numlist = []
    regxLabelName = re.compile(r'[A-Za-z0-9_]+(?==)')  # 匹配标签名
    regexLabelValue = re.compile(r'(?<==)\w*')  # 匹配标签值
    if len(linelist) == 1:  # 如果只有一行文字，说明是是标签信息，如果没有，默认标签为'data'
        labelName = regxLabelName.findall(linelist[0])
        labelValue = regexLabelValue.findall(linelist[0])
        return [labelName, labelValue, "label"]  # 返回标签信息列表， 并做上标记"label"
    for i in linelist:
        numlist.append(eval(i))  # 如果是数据，就返回数据列表
    return numlist


with open(txtfilename, buffering=1) as file:
    header = next(file).strip('\n').split('\t')  # 获取表头（第一行）
    for line in file:
        linelist = line.strip('\n').split('\t')
        numlist = toNumList(linelist)
        if "label" in numlist:  # 是标签，提取标签信息
            labelName = numlist[0]
            labelValue = numlist[1]
            label = ""
            for i in range(len(labelName)):
                label = label + labelName[i] + "=" + labelValue[i]
            keys.append(label)
            labels[keys[-1]] = [labelName, labelValue]
            data[keys[-1]] = []
        else:
            data[keys[-1]].append(numlist)
# # 表头
# print(header)#['vg', '-I(Vds)']
# # 标签
# print(keys)#['data', 'tj=25Vds=1', 'tj=125Vds=1', 'tj=200Vds=1', 'tj=25Vds=3', 'tj=125Vds=3', 'tj=200Vds=3']
# print(labels)
# # 数据
# print(data[labels[-1]])

###################################################
#   绘图
###################################################

# 注意
# 可供处理的数据就是keys labels data header
# data[key] = [header[0], header[1], ...]
# labels[key] = [labelName, labelValue]
# labelName = [labelName1, labelName2, ...]
# labelValue = [labelValue1, labelValue2, ...]

# 数据预处理函数
# 可自定义一些函数
# def findsomething(vg, id):
#     return

# 绘图

with plt.style.context(['science', 'ieee', 'std-colors']):
    fig, ax = plt.subplots()
    if len(keys) > 1:
        keys.pop(0)
    # 通过颜色和线条样式区分tj和vds
    # labelValue : color
    colors = {"25": "r", "125": "b", "225": "y"}  # tj
    lss = {"1": "-", "3": "--"}
    for key in keys:  # 通过标签遍历数据
        plotdata = np.array(data[key]).transpose()  # 转换成ndarray
        #########################
        # 以下内容为特定数据处理与绘图
        vg = plotdata[0]  # x
        id = plotdata[1]  # y
        labelName = labels[key][0]
        labelValue = labels[key][1]
        label = " "
        for i, j in zip(labelName, labelValue):
            if i == "tj":
                label += "$T_j$=" + j + "℃, "
            if i == "Vds":
                label += "$V_{ds}$=" + j + "V"

        ax.plot(vg, id, label=label,
                color=colors[labelValue[0]], ls=lss[labelValue[1]])

    ax.legend()
    ax.set(xlabel = "vg")
    ax.set(ylabel = "id")
    # ax.autoscale(tight=True)

# save config

# save fig as pdf
savename = "savename" + ".pdf"
if not os.path.exists("./figures"):
    os.makedirs("./figures")
fig.savefig("./figures/" + savename)
cmd = "SumatraPDF " + "./figures/" + savename
os.system(cmd)

print("--------------- finished ---------------")