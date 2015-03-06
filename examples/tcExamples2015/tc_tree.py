#!/usr/bin/env python3
'''龜作圖範例集：

             tdemo_tree.py

顯示“廣度優先樹” - 對比
以經典的標誌樹繪圖程序，
其中使用一個深度優先算法。

用途：
（1）一個樹生成器，其中該圖是
準的副作用，而生成器
總是產生無。
（ 2 ）龜複製：在每個分支點
當前筆被複製。那麼到底
有1024龜。=== 以上由 Google 翻譯，請協助改善 ===
'''
from turtle_tc import *; from turtle_tc import 龜類, 主迴圈
from time import clock

def 樹(p列表, l, a, f):
    '''plist中是筆名單
    l為分支長度
    一個是半2分支之間的角度
    f是由哪個分支被縮短因子
    從一級到的水平。=== 以上由 Google 翻譯，請協助改善 ===
'''
    if l > 3:
        列表 = []
        for p in p列表:
            p.前進(l)
            q = p.複製()
            p.左轉(a)
            q.右轉(a)
            列表.append(p)
            列表.append(q)
        for x in 樹(列表, l*f, a, f):
            yield 無

def 製造樹():
    p = 龜類()
    p.設回復暫存區(無)
    p.藏龜()
    p.速度(0)
    p.取幕().追蹤(30,0)
    p.左轉(90)
    p.提筆()
    p.前進(-210)
    p.下筆()
    t = 樹([p], 200, 65, 0.6375)
    for x in t:
        pass
    印(len(p.取幕().龜群()))

def 主函數():
    a=clock()
    製造樹()
    b=clock()
    return "done: %.2f sec." % (b-a)

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()

# Above: "tc_tree.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "tree.py", by Gregor Lingl. 
