import matplotlib.pyplot as plt
from PIL import Image # 导入Image

img = Image.open('/home/jy/pict/1.png')
print(len(img.split()))

