# COLORMIX

from turtle_tc import *; from turtle_tc import 幕類, 龜類, 主迴圈

class 顏色龜類(龜類):

    def __init__(我, x, y):
        龜類.__init__(我)
        我.形狀(龜形)
        我.重設大小模式("user")
        我.形狀大小(3,3,5)
        我.筆粗(10)
        我._color = [0,0,0]
        我.x = x
        我._color[x] = y
        我.顏色(我._color)
        我.速度(0)
        我.左轉(90)
        我.提筆()
        我.前往(x,0)
        我.下筆()
        我.設y座標(1)
        我.提筆()
        我.設y座標(y)
        我.筆色("gray25")
        我.在拖曳時(我.平移)

    def 平移(我, x, y):
        我.設y座標(max(0,min(y,1)))
        我._color[我.x] = 我.y座標()
        我.填色(我._color)
        設背景的顏色()

def 設背景的顏色():
    幕.背景色(red.y座標(), green.y座標(), blue.y座標())

def 主函數():
    global 幕, red, green, blue
    幕 = 幕類()
    幕.延遲(0)
    幕.設座標系統(-1, -0.3, 3, 1.3)

    red = 顏色龜類(0, .5)
    green = 顏色龜類(1, .5)
    blue = 顏色龜類(2, .5)
    設背景的顏色()

    寫手 = 龜類()
    寫手.藏龜()
    寫手.提筆()
    寫手.前往(1,1.15)
    寫手.寫("DRAG!",align="center",font=("Arial",30,("bold","italic")))
    return "EVENTLOOP"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()

# Above: "tc_colormixer.py", by Renyuan Lyu (呂仁園), 2015-03-06
# Original: "colormixer.py", by Gregor Lingl. 
