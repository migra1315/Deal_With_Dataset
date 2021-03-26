from numpy import *
import numpy as np
import math
import torch
import os                #遍历文件夹
import imageio           #转换成图像
import matplotlib.pyplot as plt
from skimage import data,img_as_float,img_as_ubyte

from PIL import Image # 导入Image


def modality_reverse_fun(path):
    os.chdir(path) # 进入图像的目录
    filenames = os.listdir(path)  #读取文件夹内容

    for f in filenames:

        img = Image.open(f) # 使用Image.open 方法打开当前目录的图像赋值---->IM 对象
        img = torch.tensor(img_as_float(img))

        if torch.cuda.is_available():
            img.cuda()

        print(shape(img))
        img_r = img_as_ubyte(np.cos(math.pi*img))
        imageio.imwrite(os.path.join(savepath,'{}_reverse.png'.format(f)), img_r)


     

if __name__ == '__main__':

    # imgfile = '/home/jy/pict'
    imgfile = '/home/jy/1_WorkSpace/MUNIT/Dataset/CT2SMod/testA'
    savepath = '/home/jy/1_WorkSpace/MUNIT/Dataset/CT2SMod/testB'
    modality_reverse_fun(imgfile)
