# 实现将nii格式的3D图像转为png格式的2D图像
# 
# 
# 
from numpy import *
import numpy as np
import os                #遍历文件夹
import nibabel as nib    #nii格式一般都会用到这个包
import imageio           #转换成图像
import matplotlib.pyplot as plt
from skimage import data,img_as_float,img_as_ubyte

 
def nii_to_image(niifile,num):
    filenames = os.listdir(filepath)  #读取nii文件夹
    # slice_trans = []
 
    for f in filenames:
        #开始读取nii文件
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)                #读取nii

        img_fdata = img.get_fdata()
        fname = f.replace('.nii','')            #去掉nii的后缀名
  
        #开始转换为图像
        (x,y,z) = img.shape
        # for i in range(x):                      #z是图像的序列
        #     silce = img_fdata[i, :, :]          #选择哪个方向的切片都可以
        #     silce = img_as_ubyte(silce)
        #     imageio.imwrite(os.path.join(imgfile1,'{}_x_{}.png'.format(fname,i)), silce)

        # for i in range(y):                      #z是图像的序列
        #     silce = img_fdata[:, i, :]          #选择哪个方向的切片都可以
        #     silce = img_as_ubyte(silce)
        #     imageio.imwrite(os.path.join(imgfile2,'{}_y_{}.png'.format(fname,i)), silce)

        for i in range(z):                      #z是图像的序列
            silce = img_fdata[:, :, i]          #选择哪个方向的切片都可以
            imageio.imwrite(os.path.join(imgfile,'{}_z_{}.png'.format(fname,i)), silce)
 
if __name__ == '__main__':
    for num in range(5,6):
        filepath = os.path.join('/home/jy/3_Storage/DIRLAB/4DCT-resample','Case{}Pack'.format(num))
        imgfile = '/home/jy/1_WorkSpace/MUNIT/Dataset/CT2SMod/testA'
        nii_to_image(filepath,num)
