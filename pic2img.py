import cv2
import os
import random
import glob

img = cv2.imread('/你的文件路径/[任意图片].jpg')  # 读取保存的任意一张图片的路径
fps = 30 # 视频的fps
size = (img.shape[1],img.shape[0])  #获取视频中图片宽高度信息
print(size)
fourcc = cv2.VideoWriter_fourcc(*"MP4V") # 视频编码格式
videoWrite = cv2.VideoWriter('./new_2.mp4',fourcc,fps,size)# 根据图片的大小，创建写入对象 （文件名，支持的编码器，帧率，视频大小（图片大小））

fileName = glob.glob('/你的文件路径/*.jpg')
fileName.sort()
for i in fileName:
    img = cv2.imread(i)
    videoWrite.write(img)# 将图片写入所创建的视频对象
videoWrite.release() # 释放了才能完成写入，连续写多个视频的时候这句话非常关键


