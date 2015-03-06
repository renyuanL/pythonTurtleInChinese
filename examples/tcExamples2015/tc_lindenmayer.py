#!/usr/bin/env python3
'''龜作圖範例集：

        xtx_lindenmayer_indian.py

每天早晨女性在泰米爾納德邦，南
印度，地點的設計，通過利用水稻創建
麵粉和稱為鵬遠上的閾值
他們的家園。

這些可以通過Lindenmayer系統進行描述，
它可以很容易地與龜實施
圖形和Python 。

兩個例子如下所示：
（ 1）Kolam蛇
克里希納（ 2 ）腳鐲

摘自瑪西婭Ascher的：數學
在其他地方，思想的探索跨
文化=== 以上由 Google 翻譯，請協助改善 ===
'''
# 
# 迷你Lindenmayer工具
# 

from turtle_tc import *

def replace( 序列, 取代規則們, n ):
    for i in 範圍(n):
        新序列 = ""
        for 元素 in 序列:
            新序列 = 新序列 + 取代規則們.get(元素,元素)
        序列 = 新序列
    return 序列

def 畫( 指令們, 規則們 ):
    for b in 指令們:
        try:
            規則們[b]()
        except TypeError:
            try:
                畫(規則們[b], 規則們)
            except:
                pass


def 主函數():
    # 
    # 例1 ：蛇Kolam
    # 


    def r():
        右轉(45)

    def l():
        左轉(45)

    def f():
        前進(7.5)

    蛇規則 = {"-":r, "+":l, "f":f, "b":"f+f+f--f--f+f+f"}
    蛇取代規則們 = {"b": "b+f+b--f--b+f+b"}
    蛇開始 = "b--f--b--f"

    正在畫 = replace(蛇開始, 蛇取代規則們, 3)

    重設()
    速度(3)
    追蹤(1,0)
    藏龜()
    提筆()
    後退(195)
    下筆()
    畫(正在畫, 蛇規則)

    from time import sleep
    sleep(3)

    # 
    # 例2 ：克里希納腳鍊
    # 

    def A():
        顏色(紅)
        畫圓(10,90)

    def B():
        from math import sqrt
        顏色(黑)
        l = 5/sqrt(2)
        前進(l)
        畫圓(l, 270)
        前進(l)

    def F():
        顏色(綠)
        前進(10)

    克里希納規則們 = {"a":A, "b":B, "f":F}
    克里希納取代規則們 = {"a" : "afbfa", "b" : "afbfbfbfa" }
    克里希納開始 = "fbfbfbfb"

    重設()
    速度(0)
    追蹤(3,0)
    藏龜()
    左轉(45)
    正在畫 = replace(克里希納開始, 克里希納取代規則們, 3)
    畫(正在畫, 克里希納規則們)
    追蹤(1)
    return "Done!"

if __name__=='__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()

# Above: "tc_lindenmayer.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "lindenmayer.py", by Gregor Lingl. 
