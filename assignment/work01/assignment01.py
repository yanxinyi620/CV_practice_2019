import cv2
import numpy as np
from matplotlib import pyplot as plt


# -----------------------------------------------
# 利用 cv2.imread 读取图片并利用 cv2.imshow 打印出来
img = cv2.imread('../../data/photo/people.jpg')
cv2.imshow('people',img)
cv2.waitKey()
print(img.shape)  # h, w, c

# 利用 cv2.imread 读取图片并利用 plt.imshow 打印出来
# 在新窗口打印图片
# %matplotlib
# 在 notebook 中打印图片
# %matplotlib inline
img = cv2.imread('../../data/photo/people.jpg')
# as opencv loads in BGR format by default, we want to show it in RGB.
# 读进来的是BGR格式，而plt使用RGB格式。要将img转换为RGB格式
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 
plt.axis("off")  #去除坐标轴
plt.title('zhoujieqiong')  # 添加标题
plt.show()  #可以不加，不加时输出时会多一行信息

# 手动将BGR转换为RGB格式
img = cv2.imread('../../data/photo/people.jpg')
img_2 = img[:,:,[2,1,0]]
print(img_2.shape)
plt.imshow(img_2)
plt.axis("off")
plt.show()


# -----------------------------------------------
# scale+rotation+translation = similarity transform
img = cv2.imread('../../data/photo/night.jpg')
M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 30, 0.5) # center, angle, scale
img_rotate = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

plt.imshow(cv2.cvtColor(img_rotate, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
print(M)

# 缩放使用cv2.resize()函数，resize函数里的size第一个是宽（列），第二个是高（行）
imgg = cv2.resize(img,(300,100),cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(imgg, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

# 操作像素, 255-原通道
img = cv2.imread('../../data/photo/night.jpg')
height = img.shape[0]
weight = img.shape[1]
channels = img.shape[2]
 
for row in range(height):  # 遍历高
    for col in range(weight):  # 遍历宽
        for c in range(channels):  # 遍历各通道
            value = img[row, col, c]
            img[row, col, c] = 255-img[row, col, c]  # 操作像素

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()


# -----------------------------------------------
# Affine Transform
rows, cols, ch = img.shape
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9]])
 
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()


