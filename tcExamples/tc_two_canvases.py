'''turtledemo.two_canvases

使用TurtleScreen和RawTurtle繪製兩個
鮮明的畫布在一個單獨的窗口。該
新窗口必須單獨關閉
除了按STOP按鈕。=== 以上由 Google 翻譯，請協助改善 ===
'''

from turtle_tc import *; from turtle_tc import 龜幕類, 原龜類, TK

def 主函數():
    根 = TK.Tk()
    畫布1 = TK.Canvas(根, width=300, height=200, bg="#ddffff")
    畫布2 = TK.Canvas(根, width=300, height=200, bg="#ffeeee")
    畫布1.pack()
    畫布2.pack()

    s1 = 龜幕類(畫布1)
    s1.背景色(0.85, 0.85, 1)
    s2 = 龜幕類(畫布2)
    s2.背景色(1, 0.85, 0.85)

    p = 原龜類(s1)
    q = 原龜類(s2)

    p.顏色(紅, (1, 0.85, 0.85))
    p.筆寬(3)
    q.顏色(藍, (0.85, 0.85, 1))
    q.筆寬(3)

    for t in p,q:
        t.形狀(龜形)
        t.左轉(36)

    q.左轉(180)

    for t in p, q:
        t.開始填()
    for i in 範圍(5):
        for t in p, q:
            t.前進(50)
            t.左轉(72)
    for t in p,q:
        t.結束填()
        t.左轉(54)
        t.提筆()
        t.後退(50)

    return "EVENTLOOP"


if __name__ == '__main__':
    主函數()
    TK.mainloop()  # 保持窗口打開，直到使用者關閉

# Above: "tc_two_canvases.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "two_canvases.py", by Gregor Lingl. 
