#!/usr/bin/env python3
'''龜作圖範例集：

         tdemo_minimal_hanoi.py

動畫一個最小的“河內塔” ：
塔的6碟從轉移
左到右的PEG 。

恕我直言，一個很優雅而簡潔
使用塔類，其中實現
從內置類型列表中導出。

光盤是龜與形“廣場” ，但
通過shapesize延伸到矩形（ ）
 ---------------------------------------
       要退出，請按STOP按鈕
 ---------------------------------------=== 以上由 Google 翻譯，請協助改善 ===
'''
from turtle_tc import *

class 盤類(龜類):
    def __init__(我, n):
        龜類.__init__(我, shape=方形, visible=假)
        我.提筆()
        我.形狀大小(1.5, n*1.5, 2) # 廣場 - >矩形
        我.填色(n/6., 0, 1-n/6.)
        我.顯龜()

class 塔類(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(我, x):
        "create an empty tower. x is x-position of peg"
        我.x = x
    def push(我, d):
        d.設x座標(我.x)
        d.設y座標(-150+34*len(我))
        我.append(d)
    def pop(我):
        d = list.pop(我)
        d.設y座標(150)
        return d

def 河內(n, 從_, 伴隨_, 去_):
    if n > 0:
        河內(n-1, 從_, 去_, 伴隨_)
        去_.push(從_.pop())
        河內(n-1, 伴隨_, 從_, 去_)

def 玩():
    在按鍵時(無,空白鍵)
    清除()
    try:
        河內(6, t1, t2, t3)
        寫("press STOP button to exit",
              align="center", font=("Courier", 16, "bold"))
    except Terminator:
        pass  # turtledemo使用者按STOP

def 主函數():
    global t1, t2, t3
    藏龜(); 提筆(); 前往(0, -225)   # 作家龜
    t1 = 塔類(-250)
    t2 = 塔類(0)
    t3 = 塔類(250)
    # 使塔的6碟
    for i in 範圍(6,0,-1):
        t1.push(盤類(i))
    # 準備spartanic使用者界面; - ）
    寫("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    在按鍵時(玩, 空白鍵)
    聽()
    return "EVENTLOOP"

if __name__=="__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()

# Above: "tc_minimal_hanoi.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "minimal_hanoi.py", by Gregor Lingl. 
