#!/usr/bin/env python3
'''龜作圖範例集：

              tdemo_peace.py

適合作為初學者的一個簡單的繪圖
程式設計實例。除了
peacecolors分配和循環，
它僅使用龜命令。=== 以上由 Google 翻譯，請協助改善 ===
'''

from turtle_tc import *

def 主函數():
    和平顏色們 = ("red3",  橙, 黃,
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")

    重設()
    幕類()
    提筆()
    前往(-320,-195)
    筆寬(70)

    for p顏色 in 和平顏色們:
        顏色(p顏色)
        下筆()
        前進(640)
        提筆()
        後退(640)
        左轉(90)
        前進(66)
        右轉(90)

    筆寬(25)
    顏色(白)
    前往(0,-170)
    下筆()

    畫圓(170)
    左轉(90)
    前進(340)
    提筆()
    左轉(180)
    前進(170)
    右轉(45)
    下筆()
    前進(170)
    提筆()
    後退(170)
    左轉(90)
    下筆()
    前進(170)
    提筆()

    前往(0,300) # 消失，如果hideturtle （ ）不可用; - ）
    return "Done!"

if __name__ == "__main__":
    主函數()
    主迴圈()

# Above: "tc_peace.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "peace.py", by Gregor Lingl. 
