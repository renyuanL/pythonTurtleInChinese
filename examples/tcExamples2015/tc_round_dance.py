'''龜作圖範例集：

         tdemo_round_dance.py

（需要烏龜模塊1.1版本
自帶的Python 3.1 ）

跳舞龜有複合形狀
由一系列的三角形
減小尺寸。

龜沿著遊行一圈旋轉時
兩兩方向相反，與一個
例外。是否對稱，違反
增強例子的吸引力？

按任意鍵停止動畫。

技術上：演示使用的化合物
形狀，形狀的變換以及
複製龜。動畫是
通過更新控制（ ） 。=== 以上由 Google 翻譯，請協助改善 ===
'''

from turtle_tc import *

def 停止():
    global 正在跑
    正在跑 = 假

def 主函數():
    global 正在跑
    清除幕()
    背景色("gray10")
    追蹤(假)
    形狀("triangle")
    f =   0.793402
    φ = 9.064678
    s = 5
    c = 1
    # 創建複合形狀
    sh = 形狀類("compound")
    for i in 範圍(10):
        形狀大小(s)
        p =取形狀多邊形()
        s *= f
        c *= f
        傾斜(-φ)
        sh.加成員(p, (c, 0.25, 1-c), 黑)
    登記形狀("multitri", sh)
    # 創建舞者
    形狀大小(1)
    形狀("multitri")
    提筆()
    設位置(0, -200)
    舞者們 = []
    for i in 範圍(180):
        前進(7)
        傾斜(-4)
        左轉(2)
        更新()
        if i % 12 == 0:
            舞者們.append(複製())
    回家()
    # 舞蹈
    正在跑 = 真
    在按著鍵時(停止)
    聽()
    cs = 1
    while 正在跑:
        ta = -4
        for 舞者 in 舞者們:
            舞者.前進(7)
            舞者.左轉(2)
            舞者.傾斜(ta)
            ta = -4 if ta > 0 else 2
        if cs < 180:
            右轉(4)
            形狀大小(cs)
            cs *= 1.005
        更新()
    return "DONE!"

if __name__=='__main__':
    印(主函數())
    主迴圈()

# Above: "tc_round_dance.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "round_dance.py", by Gregor Lingl. 
