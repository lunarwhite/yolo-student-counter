import os
from os import listdir
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from lxml.etree import *
import xml.etree.ElementTree as ET

res_path = 'dataset/images/'
images = os.listdir(res_path)
res2_path = 'dataset/annotations/'
annotations = os.listdir(res_path)

# 数据探索
plt.figure(figsize=(15, 8))
plt.title('First 120 image in dataset')

row, col = 15, 8
for i in range(row*col):
    plt.subplot(col, row, i+1)
    img = Image.open(res_path + images[i])
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
plt.show()

# 数据清洗，刨除数据标签XML文件损坏的文件
def find_xml(image_id):
    in_file = open(dir_xml+'\%s.xml' % (image_id), encoding='UTF-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    if(w==0 or h==0): 
        print("此图片数据标签丢失：")
        print(image_id)
        s = image_id
        os.remove('/{res_path}/{s}.jpg') # 删除iamge
        os.remove('/{res2_path}/{s}.xml') # 删除xml 标签

img_xmls = os.listdir(dir_xml)
for img_xml in img_xmls:
    label_name = img_xml.split('.')[0]
    print(label_name)
    find_xml(label_name)