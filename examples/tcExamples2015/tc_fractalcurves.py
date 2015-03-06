#!/usr/bin/env python3
'''龜作圖範例集：

        tdemo_fractalCurves.py

這個程序繪製了兩個分形曲線設計：
（ 1 ）希爾伯特曲線（在一個盒子）
（ 2 ）對科赫 - 曲線的組合。

該CurvesTurtle類和分形曲線 - 
方法是從PythonCard示例取
腳本烏龜圖形。=== 以上由 Google 翻譯，請協助改善 ===
'''
from turtle_tc import *
from time import sleep, clock

class 曲線龜類(筆類):
    # 例如源自
    # 龜幾何：計算機作為媒介的探索數學
    # 由哈羅德·阿貝爾森和Andrea diSessa
    # 頁。 96-98
    def hilbert(我, 尺寸, 等級, 對等性):
        if 等級 == 0:
            return
        # 旋轉並繪製第一subcurve具有相反奇偶性，以大曲線
        我.左轉(對等性 * 90)
        我.hilbert(尺寸, 等級 - 1, -對等性)
        # 接口和借鑒第二subcurve具有相同的奇偶大曲線
        我.前進(尺寸)
        我.右轉(對等性 * 90)
        我.hilbert(尺寸, 等級 - 1, 對等性)
        # 第三subcurve
        我.前進(尺寸)
        我.hilbert(尺寸, 等級 - 1, 對等性)
        # 第四subcurve
        我.右轉(對等性 * 90)
        我.前進(尺寸)
        我.hilbert(尺寸, 等級 - 1, -對等性)
        # 最後又需要作出烏龜
        # 最終朝外從大廣場
        我.左轉(對等性 * 90)

    # 可視化建模與標誌：一種結構方法見此
    # 由詹姆斯·克萊森
    # 科赫曲線，黑爾格·馮·科赫後誰介紹這個幾何圖形在1904年
    # 頁。 146
    def 碎形多邊形(我, n, 弳度, lev, dir):
        import math

        # 如果DIR = 1向外轉
        # 如果DIR = -1向內轉
        邊緣 = 2 * 弳度 * math.sin(math.pi / n)
        我.提筆()
        我.前進(弳度)
        我.下筆()
        我.右轉(180 - (90 * (n - 2) / n))
        for i in 範圍(n):
            我.碎形(邊緣, lev, dir)
            我.右轉(360 / n)
        我.左轉(180 - (90 * (n - 2) / n))
        我.提筆()
        我.後退(弳度)
        我.下筆()

    # 頁。 146
    def 碎形(我, 距離, 深度, dir):
        if 深度 < 1:
            我.前進(距離)
            return
        我.碎形(距離 / 3, 深度 - 1, dir)
        我.左轉(60 * dir)
        我.碎形(距離 / 3, 深度 - 1, dir)
        我.右轉(120 * dir)
        我.碎形(距離 / 3, 深度 - 1, dir)
        我.左轉(60 * dir)
        我.碎形(距離 / 3, 深度 - 1, dir)

def 主函數():
    ft = 曲線龜類()

    ft.重設()
    ft.速度(0)
    ft.藏龜()
    ft.取幕().追蹤(1,0)
    ft.提筆()

    尺寸 = 6
    ft.設位置(-33*尺寸, -32*尺寸)
    ft.下筆()

    ta=clock()
    ft.填色(紅)
    ft.開始填()
    ft.前進(尺寸)

    ft.hilbert(尺寸, 6, 1)

    # 框架
    ft.前進(尺寸)
    for i in 範圍(3):
        ft.左轉(90)
        ft.前進(尺寸*(64+i%2))
    ft.提筆()
    for i in 範圍(2):
        ft.前進(尺寸)
        ft.右轉(90)
    ft.下筆()
    for i in 範圍(4):
        ft.前進(尺寸*(66+i%2))
        ft.右轉(90)
    ft.結束填()
    tb=clock()
    res =  "Hilbert: %.2fsec. " % (tb-ta)

    sleep(3)

    ft.重設()
    ft.速度(0)
    ft.藏龜()
    ft.取幕().追蹤(1,0)

    ta=clock()
    ft.顏色(黑, 藍)
    ft.開始填()
    ft.碎形多邊形(3, 250, 4, 1)
    ft.結束填()
    ft.開始填()
    ft.顏色(紅)
    ft.碎形多邊形(3, 200, 4, -1)
    ft.結束填()
    tb=clock()
    res +=  "Koch: %.2fsec." % (tb-ta)
    return res

if __name__  == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()

# Above: "tc_fractalcurves.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "fractalcurves.py", by Gregor Lingl. 
