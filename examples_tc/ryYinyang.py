'''
ryYinyang.py

用 中文龜模組 ryTurtle
示範龜畫陰陽太極圖。

by 呂仁園
2014/03/24

'''

"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""
#from  turtle import *

from  turtle_tc import *

def 陰陽(半徑, 色01, 色02):

    筆大小(3)
    顏色(黑, 色01)
    開始填色()
    畫圓(半徑/2, 180)
    畫圓(半徑, 180)
    左轉(180)
    畫圓(-半徑/2, 180)
    結束填色()
    左轉(90)
    提筆()
    前進(半徑*0.35)
    右轉(90)
    下筆()
    顏色(色01, 色02)
    開始填色()
    畫圓(半徑*0.15)
    結束填色()
    左轉(90)
    提筆()
    後退(半徑*0.35)
    下筆()
    左轉(90)

def 主函數():

    重設()
    陰陽(200,  黑, 白)
    陰陽(200,  白, 黑)
    藏龜()

    進入主迴圈()

    return "完成!"

if __name__ == '__main__':

    主函數()

