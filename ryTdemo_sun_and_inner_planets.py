'''
ryTdemo_sun_and_inner_planets.py

4 顆 行星 (水、金、地、火) 的 繞日運動
基於真實的物理常數。

中文程式翻譯： 呂仁園。
2014/05/26

'''
#!/usr/bin/python
"""        turtle-example-suite:

      tdemo_sun_and_inner_planets.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol.1, p.9-8, using turtlegraphics

This example uses real phyisical data of
our planetary system: simulates the four
inner planets orbiting around the sun.

Demonstrates the use of (user defined)
worldcoordinates.
"""

from turtle_tc import *

#
# 一些 物理常數, some Constants of  Physics
#
天文單位= AU= 1.5e11
重力常數= G=  6.67e-11

#
# 質量, mass
#
m太陽= 2.0e30
m地球= 6.0e24
m水星= 3.3e23
m金星= 4.869e24
m火星= 6.419e23

#
# 大小 (約略值), size (relative values)
#
s太陽= 2.0
s地球= 1.0
s水星= 0.4
s金星= 0.8
s火星= 0.6

#
# 軌道半徑, radii of the orbits
#
r地球= 1.0   *天文單位
r水星=  .307 *天文單位
r金星=  .732 *天文單位
r火星= 1.524 *天文單位

#
# 初速度, initial velocities
#
v0地球= 3.e4
v0水星= 5.9e4
v0金星= 3.502e4
v0火星= 2.413e4

#
# 位置，速度 向量, position, velocity vector
#
x太陽, v太陽= 二維向量類(     0,0), 二維向量類( 0,      0)
x地球, v地球= 二維向量類( r地球,0), 二維向量類( 0, v0地球)
x水星, v水星= 二維向量類( r水星,0), 二維向量類( 0, v0水星)
x金星, v金星= 二維向量類( r金星,0), 二維向量類( 0, v0金星)
x火星, v火星= 二維向量類( r火星,0), 二維向量類( 0, v0火星)


座標範圍= 1.01 * r火星

幕寬= 幕高= 500

class 星系類:

    生命期= 1000
    DT=     100000 #10000 #10800

    def __init__(我):

        我.行星群= []
        我.dt= 我.DT

    def init(我):

        for p in 我.行星群:
            p.啟動()

    def start(我):

        幕.追蹤更新畫面(False)

        for i in 範圍(我.生命期):
            for p in 我.行星群:
                p.步進()
            幕.更新()

    啟動= init
    開始= 開始運行= start

class 星球類(龜類):

    def __init__(我, m, x, v, 星系, 形狀):

        龜類.__init__(我, 形狀)

        星系.行星群 += [我]

        我.星系= 星系
        我.dt= 我.星系.dt
        我.m= m
        我.v= v

        我.提筆()
        我.設位置(x)
        我.下筆()

    def init(我):

        我.v = 我.v + 0.5 * 我.dt * 我.acc()

    def acc(我):

        a = 二維向量類(0,0)
        for p in 我.星系.行星群:
            if p != 我:
                #
                # 最重要的 牛頓 物理公式在此
                #
                r = p.位置() - 我.位置()
                a += (G * p.m / abs(r)**3) *r

        return a

    def step(我):

        global 太陽

        我.設位置(我.位置() + 我.dt * 我.v)

        我.設頭向(我.朝向(太陽))

        我.v = 我.v + 我.dt * 我.acc()

    啟動=   init
    加速度= acc
    步進=   step


def 創造行星形狀():
    '''
    為行星創造複合形狀，含「黃、藍」色，
    「黃」色朝向太陽。
    '''
    global 幕

    幕.追蹤更新畫面(0,0)

    行星= 龜類()

    行星.顯示()
    行星.提筆()
    行星.前進(6)
    行星.左轉(90)

    行星.開始多邊形()
    行星.畫圓(6, 180)
    行星.結束多邊形()
    面日形狀= 行星.取多邊形()

    行星.開始多邊形()
    行星.畫圓(6,180)
    行星.結束多邊形()
    背日形狀= 行星.取多邊形()

    行星形狀= 形狀類("compound")
    行星形狀.addcomponent(面日形狀, 黃)
    行星形狀.addcomponent(背日形狀, 灰)

    幕.登記形狀('行星形', 行星形狀)

    幕.追蹤更新畫面(True,0)


def 主函數():

    global 幕, 太陽

    幕= 幕類()

    幕.設立(幕寬, 幕高)
    幕.背景色(黑)

    幕.設座標系統(-座標範圍, -座標範圍, +座標範圍,  +座標範圍)

    創造行星形狀()

    太陽系= 星系類()

    太陽= 星球類(m太陽, x太陽, v太陽, 太陽系, 'circle')
    地球= 星球類(m地球, x地球, v地球, 太陽系, '行星形')
    水星= 星球類(m水星, x水星, v水星, 太陽系, '行星形')
    金星= 星球類(m金星, x金星, v金星, 太陽系, '行星形')
    火星= 星球類(m火星, x火星, v火星, 太陽系, '行星形')

    太陽.顏色(黃)
    地球.筆色(綠)
    水星.筆色(紫)
    金星.筆色(藍)
    火星.筆色(紅)

    太陽.大小(s太陽)
    地球.大小(s地球)
    水星.大小(s水星)
    金星.大小(s金星)
    火星.大小(s火星)

    太陽系.啟動()
    太陽系.開始運行()

    return "完了！"

if __name__ == '__main__':

    m= 主函數()
    印(m)

    進入主迴圈()
