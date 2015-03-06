#!/usr/bin/env python3
'''xturtle ，範例集：

          xtx_kites_and_darts.py

構造兩個非週期性彭羅斯，平鋪，
由風箏和飛鏢，該方法
通脹的六個步驟。

出發點是圖案“太陽”
包括五個風箏和“明星”
由五個飛鏢。

欲了解更多信息，請參閱：
 http://en.wikipedia.org/wiki/Penrose_tiling
 -------------------------------------------=== 以上由 Google 翻譯，請協助改善 ===
'''
from turtle_tc import *
from math import cos, pi
from time import clock, sleep

f = (5**0.5-1)/2.0   # （ SQRT（ 5）-1 ）/ 2 - 黃金比例
d = 2 * cos(3*pi/10)

def 風箏(l):
    fl = f * l
    左轉(36)
    前進(l)
    右轉(108)
    前進(fl)
    右轉(36)
    前進(fl)
    右轉(108)
    前進(l)
    右轉(144)

def 飛鏢(l):
    fl = f * l
    左轉(36)
    前進(l)
    右轉(144)
    前進(fl)
    左轉(36)
    前進(fl)
    右轉(144)
    前進(l)
    右轉(144)

def 膨脹風箏(l, n):
    if n == 0:
        px, py = 位置()
        h, x, y = int(頭向()), round(px,3), round(py,3)
        瓦片字典[(h,x,y)] = 真
        return
    fl = f * l
    左轉(36)
    膨脹飛鏢(fl, n-1)
    前進(l)
    右轉(144)
    膨脹風箏(fl, n-1)
    左轉(18)
    前進(l*d)
    右轉(162)
    膨脹風箏(fl, n-1)
    左轉(36)
    前進(l)
    右轉(180)
    膨脹飛鏢(fl, n-1)
    左轉(36)

def 膨脹飛鏢(l, n):
    if n == 0:
        px, py = 位置()
        h, x, y = int(頭向()), round(px,3), round(py,3)
        瓦片字典[(h,x,y)] = 假
        return
    fl = f * l
    膨脹風箏(fl, n-1)
    左轉(36)
    前進(l)
    右轉(180)
    膨脹飛鏢(fl, n-1)
    左轉(54)
    前進(l*d)
    右轉(126)
    膨脹飛鏢(fl, n-1)
    前進(l)
    右轉(144)

def 畫(l, n, th=2):
    清除()
    l = l * f**n
    形狀大小(l/100.0, l/100.0, th)
    for k in 瓦片字典:
        h, x, y = k
        設位置(x, y)
        設頭向(h)
        if 瓦片字典[k]:
            形狀("風箏")
            顏色(黑, (0, 0.75, 0))
        else:
            形狀("飛鏢")
            顏色(黑, (0.75, 0, 0))
        蓋章()

def 日(l, n):
    for i in 範圍(5):
        膨脹風箏(l, n)
        左轉(72)

def 星(l,n):
    for i in 範圍(5):
        膨脹飛鏢(l, n)
        左轉(72)

def 製造形狀們():
    追蹤(0)
    開始多邊形()
    風箏(100)
    結束多邊形()
    登記形狀("風箏", 取多邊形())
    開始多邊形()
    飛鏢(100)
    結束多邊形()
    登記形狀("飛鏢", 取多邊形())
    追蹤(1)

def 開始():
    重設()
    藏龜()
    提筆()
    製造形狀們()
    重設大小模式("user")

def 測試(l=200, n=4, 函數=日, 開始位置=(0,0), th=2):
    global 瓦片字典
    前往(開始位置)
    設頭向(0)
    瓦片字典 = {}
    a = clock()
    追蹤(0)
    函數(l, n)
    b = clock()
    畫(l, n, th)
    追蹤(1)
    c = clock()
    印("Calculation:   %7.4f s" % (b - a))
    印("Drawing:  %7.4f s" % (c - b))
    印("Together: %7.4f s" % (c - a))
    nk = len([x for x in 瓦片字典 if 瓦片字典[x]])
    nd = len([x for x in 瓦片字典 if not 瓦片字典[x]])
    印("%d kites and %d darts = %d pieces." % (nk, nd, nk+nd))

def 展示(函數=日):
    開始()
    for i in 範圍(8):
        a = clock()
        測試(300, i, 函數)
        b = clock()
        t = b - a
        if t < 2:
            sleep(2 - t)

def 主函數():
    # 標題（“彭羅斯瓦片風箏和飛鏢。 ” ）
    模式(角度從北開始順時針)
    背景色(0.3, 0.3, 0)
    展示(日)
    sleep(2)
    展示(星)
    筆色(黑)
    前往(0,-200)
    筆色(0.7,0.7,1)
    寫("Please wait...",
          align="center", font=('Arial Black', 36, 'bold'))
    測試(600, 8, 開始位置=(70, 117))
    return "Done"

if __name__ == "__main__":
    訊息 = 主函數()
    主迴圈()

# Above: "tc_penrose.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "penrose.py", by Gregor Lingl. 
