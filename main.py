# !/usr/bin/env python
# coding=utf-8
# author: zhangjelly@pku.edu.cn

from turtle import *
import math

# Node radius
NodeRadius = 10
# how much length decreses every level
Radio = 0.5

# move pen without draw anything
def jumpTo(x, y):
    penup()
    goto(x, y)
    pendown()

def drawCircle(x, y):
    jumpTo(x, y)
    begin_fill()
    circle(NodeRadius)
    end_fill()


def drawLine(x1, y1, x2, y2):
    jumpTo(x1, y1)
    pendown()
    goto(x2,y2)
    penup()

def drawTreeHelper(x, y, len, level):
    drawCircle(x,y)
    if level == 0:
        return
    # compute child position
    leftX = x-len
    leftY = y-len
    rightX = x+len
    rightY = y-len
    # connect and draw child
    drawLine(x,y+NodeRadius,leftX,leftY+NodeRadius)
    drawTreeHelper(leftX,leftY,len*Radio,level-1)
    drawLine(x,y+NodeRadius,rightX,rightY+NodeRadius)
    drawTreeHelper(rightX,rightY,len*Radio,level-1)


if __name__ == '__main__':
    screensize(800,600, "#f0f0f0")
    pensize(1)  # 画笔宽度
    speed(9)    # 画笔速度
    drawTreeHelper(0,400,200,4)
    done()
