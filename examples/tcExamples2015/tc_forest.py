#!/usr/bin/env python3
'''turtlegraphics ，範例集：

             tdemo_forest.py

顯示3廣度優先樹一個'森林'
一個類似於在樹中。
為了進一步說明，見tree.py

這個例子是一個“廣度first'重寫的
徽標計劃寫的埃里希Neuwirth的。見
http://homepage.univie.ac.at/erich.neuwirth/=== 以上由 Google 翻譯，請協助改善 ===
'''
from turtle_tc import *; from turtle_tc import 龜類, 色模式, 追蹤, 主迴圈
from random import randrange
from time import clock

def 隨機符號(n):
    return randrange(-n,n+1)

def 隨機化( 分支列表, 角度距離, 邊距離 ):
    return [ (角度+隨機符號(角度距離),
              尺寸因子*1.01**隨機符號(邊距離))
                     for 角度, 尺寸因子 in 分支列表 ]

def 隨機前進( t, 距離, 部分, 角度距離 ):
    for i in 範圍(部分):
        t.左轉(隨機符號(角度距離))
        t.前進( (1.0 * 距離)/部分 )

def 樹(t列表, 尺寸, 等級, 寬度因子, 分支列表們, 角度距離=10, 邊距離=5):
    # 龜使用的列表和分支列出清單
    # 每個龜之一！
    if 等級 > 0:
        列表 = []
        brs = []
        for t, 分支列表 in list(zip(t列表,分支列表們)):
            t.筆粗( 尺寸 * 寬度因子 )
            t.筆色( 255 - (180 - 11 * 等級 + 隨機符號(15)),
                        180 - 11 * 等級 + 隨機符號(15),
                        0 )
            t.下筆()
            隨機前進(t, 尺寸, 等級, 角度距離 )
            yield 1
            for 角度, 尺寸因子 in 分支列表:
                t.左轉(角度)
                列表.append(t.複製())
                brs.append(隨機化(分支列表, 角度距離, 邊距離))
                t.右轉(角度)
        for x in 樹(列表, 尺寸*尺寸因子, 等級-1, 寬度因子, brs,
                      角度距離, 邊距離):
            yield 無


def 開始(t,x,y):
    色模式(255)
    t.重設()
    t.速度(0)
    t.藏龜()
    t.左轉(90)
    t.提筆()
    t.設位置(x,y)
    t.下筆()

def 做它1(等級, 筆):
    筆.藏龜()
    開始(筆, 20, -208)
    t = 樹( [筆], 80, 等級, 0.1, [[ (45,0.69), (0,0.65), (-45,0.71) ]] )
    return t

def 做它2(等級, 筆):
    筆.藏龜()
    開始(筆, -135, -130)
    t = 樹( [筆], 120, 等級, 0.1, [[ (45,0.69), (-45,0.71) ]] )
    return t

def 做它3(等級, 筆):
    筆.藏龜()
    開始(筆, 190, -90)
    t = 樹( [筆], 100, 等級, 0.1, [[ (45,0.7), (0,0.72), (-45,0.65) ]] )
    return t

# 這裡有3棵樹生成器：
def 主函數():
    p = 龜類()
    p.藏龜()
    追蹤(75,0)
    u = 做它1(6, 龜類(undobuffersize=1))
    s = 做它2(7, 龜類(undobuffersize=1))
    t = 做它3(5, 龜類(undobuffersize=1))
    a = clock()
    while 真:
        做完了 = 0
        for b in u,s,t:
            try:
                b.__next__()
            except:
                做完了 += 1
        if 做完了 == 3:
            break

    追蹤(1,10)
    b = clock()
    return "執行時間: %.2f 秒。" % (b-a)

if __name__ == '__main__':
    主函數()
    主迴圈()

# Above: "tc_forest.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "forest.py", by Gregor Lingl. 
