#!/usr/bin/env python3
'''龜作圖範例集：

        tdemo_planets_and_moon.py

使用重力系統仿真
從費曼-講座近似方法，
p.9-8 ，使用turtlegraphics 。

例如：沉重的中央機構，光的星球，
很輕的月亮！
地球上有一個圓形的軌道，月球穩定
軌道圍繞地球。

您可以暫時保持運動通過
按下鼠標左鍵與
鼠標移到畫布的滾動條。=== 以上由 Google 翻譯，請協助改善 ===
'''
from turtle_tc import *; from turtle_tc import 形狀類, 龜類, 主迴圈, 向量類 as 向量類
from time import sleep

G常數 = 8

class 重力系統類(object):
    def __init__(我):
        我.行星們 = []
        我.t = 0
        我.dt = 0.01
    def 起始化(我):
        for p in 我.行星們:
            p.起始化()
    def 開始(我):
        for i in 範圍(10000):
            我.t += 我.dt
            for p in 我.行星們:
                p.步進()

class 星類(龜類):
    def __init__(我, m, x, v, 重力系統, 形狀):
        龜類.__init__(我, shape=形狀)
        我.提筆()
        我.m = m
        我.設位置(x)
        我.v = v
        重力系統.行星們.append(我)
        我.重力系統 = 重力系統
        我.重設大小模式("user")
        我.下筆()
    def 起始化(我):
        dt = 我.重力系統.dt
        我.a = 我.加速度()
        我.v = 我.v + 0.5*dt*我.a
    def 加速度(我):
        a = 向量類(0,0)
        for 行星 in 我.重力系統.行星們:
            if 行星 != 我:
                v = 行星.位置()-我.位置()
                a += (G常數*行星.m/abs(v)**3)*v
        return a
    def 步進(我):
        dt = 我.重力系統.dt
        我.設位置(我.位置() + dt*我.v)
        if 我.重力系統.行星們.index(我) != 0:
            我.設頭向(我.朝向(我.重力系統.行星們[0]))
        我.a = 我.加速度()
        我.v = 我.v + dt*我.a

# 創建複合黃/藍turtleshape行星

def 主函數():
    s = 龜類()
    s.重設()
    s.取幕().追蹤(0,0)
    s.藏龜()
    s.提筆()
    s.前進(6)
    s.左轉(90)
    s.開始多邊形()
    s.畫圓(6, 180)
    s.結束多邊形()
    m1 = s.取多邊形()
    s.開始多邊形()
    s.畫圓(6,180)
    s.結束多邊形()
    m2 = s.取多邊形()

    行星形狀 = 形狀類("compound")
    行星形狀.加成員(m1,橙)
    行星形狀.加成員(m2,藍)
    s.取幕().登記形狀("planet", 行星形狀)
    s.取幕().追蹤(1,0)

    # 設置重力系統
    gs = 重力系統類()
    日 = 星類(1000000, 向量類(0,0), 向量類(0,-2.5), gs, "circle")
    日.顏色(黃)
    日.形狀大小(1.8)
    日.提筆()
    地球 = 星類(12500, 向量類(210,0), 向量類(0,195), gs, "planet")
    地球.筆色(綠)
    地球.形狀大小(0.8)
    月球 = 星類(1, 向量類(220,0), 向量類(0,295), gs, "planet")
    月球.筆色(藍)
    月球.形狀大小(0.5)
    gs.起始化()
    gs.開始()
    return "Done!"

if __name__ == '__main__':
    主函數()
    主迴圈()

# Above: "tc_planet_and_moon.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "planet_and_moon.py", by Gregor Lingl. 
