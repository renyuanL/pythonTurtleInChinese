'''
turtle_tc.py

Renyuan Lyu
2014/05/25

renyuan.lyu@gmail.com
google.com/+RenyuanLyu




Inspired by the MIT Scratch project,
a program language capable of supporting programmers' native language ,
will allow more people ( particularly non-English-speaking kids ) able to write the program more fluently.

Starting from Python version 3.0 ,  names of variables, functions, and classes  are encoded in utf-8 ,
that is to say, programmers can write programs in their mother languages.
I think this will be a key point to make Python overspread even broader and broader.

As long as we can get into many python's modules, provide a set of name aliases for each class, method, and import global variables, then kids or naive people can also write their own programs. Kids include those from K to 12 in non-English-speaking countries, who are not fluent nor possess enough vocabulary in English.

This program/module implementing the idea is one of the few first tries,
it is an appendix to the Python built-in modules turtle.py,
which is majorly a bunch of traditional Chinese alias of English name.

This file is named as turtle_tc.py, to emphasize it is majorly in traditional Chinese.

Similar modification can be made to make it suitable in any non-English language.

This file can be run by itself,
it can also be put in the path of Python library,
and be imported by the other application of turtle programs

To use Chinese names could not only make the program more readable for local Chinese speaking programmers,
it could also make the program more compact, dense and beautiful.

Renyuan Lyu
2014/05/24

renyuan.lyu@gmail.com
google.com/+RenyuanLyu

turtle_tc_01.py

開始超朝向自動翻譯方向前進。

先做出中英對照表。

2014/04/19


============================
用 Python 3，學中文程式設計。
============================

繁體中文龜
----------

使用這個模組，可以讓你使用繁體中文來控制龜畫圖。

作者：呂仁園。
-------------

受了 MIT Scratch project 的啟發，
讓 programming language 能夠以程式員的母語來表達，
將是讓更多人(特別是非英語為母語的小孩)能夠來寫程式的一個關鍵要素。

Python 3.0 以後， 變數、函數、以及物類名稱都使用  Utf-8 編碼，
允許 程式員 運用 其母語來寫作程式，
只要我們鑽進眾多模組內部，為每個物類的函數名稱給個母語別名，
再把相應的 doc 文件說明也轉成母語，
這個基本工程將建立起母語寫作程式的基礎環境，
程式教育就有可能向下紮根，到達高中，甚至是國中的階段。

本程式模組就是在這個想法之下的首次嘗試，
我們把 Python 中， 一個頗負盛名的模組，turtle.py，
為其提供一個繁體中文 (traditional Chinese) 的附加模組，
命名為 turtle_tc.py，

使用者只要把本程式模組放在 python環境下，模組的搜尋路徑內，
一般為當前程式碼的目錄 (current dir)或是 C:/Python3.x/Lib/，
那麼，你就可以用
import turtle_tc
來取代
import turtle

進而，運用中文來寫基於 龜 的作圖程式，就成為可能。




'''

import math
import time
import random


#'''
#import turtle as tt
from turtle import *
from turtle import _CFG, _Screen, _Root, TK, _TurtleImage, Tbuffer, TurtleGraphicsError
from turtle import TurtleScreenBase, TurtleScreen, TNavigator, TPen, RawTurtle, Canvas #, Turtle, Screen
#'''

'''
#import ryTurtle as tt
from ryTurtle import *
from ryTurtle import _CFG, _Screen, _Root, TK, _TurtleImage, Tbuffer, TurtleGraphicsError
from ryTurtle import TurtleScreenBase, TurtleScreen, TNavigator, TPen, RawTurtle, Turtle, Screen
'''


import inspect as ip


import math
import random as rd

'''
隨機數= rd.random
隨機整數= rd.randint
時間= time.time
睡= time.sleep
'''

#
# 物類內別名，(Inside-class alias)
#


cListTurtleScreenBase=[
('TurtleScreenBase', '龜幕基類', '烏龜螢幕地基類', 'guimujilei'),
('mainloop'  ,   '主迴圈', '進入主迴圈', '做完了', '點擊X結束', '等待閉幕', '閉幕',  'zhuhuiquan'),
('numinput'  ,   '輸入數字',    'shurushuzi'),
('textinput' ,   '輸入文字',    'shuruwenzi'),
]



cListTurtleScreen=[
('TurtleScreen',                '龜幕類', '烏龜螢幕類', 'guimulei'),

('addshape',                    '加形狀',  'jiaxingzhuang'),
('bgcolor',                     '背景色',  'beijingse'),
('bgpic',                       '背景圖',  'beijingtu'),
('clear',                       '清除',   'cingchu'),
('clearscreen',                 '清除幕'),
('colormode',                   '色模式'),
('delay',                       '延遲'),
('getcanvas',                   '取畫布'),
('getshapes',                   '取形', '取形狀'),
('listen',                      '聽', '聽鍵盤'),
('mode',                        '模式'),

('onclick',                     '在點擊時','在點擊龜時'),
('onclick',                     '在滑鼠鍵點擊時'),
('onkey',                       '在按鍵時', '在按鍵鬆開時'),

('onkeypress',                  '在按著鍵時', '在按下鍵時'),
('onkeyrelease',                '在按鍵鬆開時'),
('onscreenclick',               '在點擊幕時', '在幕點擊時', '在滑鼠鍵點擊幕時' ),
('ontimer',                     '在計時後', '在計時器若干毫秒之後'),

('register_shape',              '登記形狀','註冊形狀'),
('reset',                       '重設', '重設所有龜'),
('resetscreen',                 '重設幕'),
('screensize',                  '幕大小', '重設幕寬高', '重設幕大小'),
('setworldcoordinates',         '設座標系統', '座標系統'),
('tracer',                      '追蹤','追蹤更新畫面', '追蹤器'),
('turtles',                     '龜群', '取龜列表', '龜列表'),
('update',                      '更新', '更新畫面'),
('window_height',               '取幕高', '幕高','窗高'),
('window_width',                '取幕寬', '幕寬','窗寬')
]



cListTNavigator= [
('TNavigator', '龜行類', '烏龜航行類','guixinglei'),

('reset',                       '重設','chongshe'),
('forward',                     '前進','qianjin'),
('back',                        '後退','houtui'),
('right',                       '右轉','youzhuan'),
('left',                        '左轉','zuozhuan'),
('pos',                         '位置','weizhi'),
('goto',                        '前往', '設位置', '去到','qianwang'),
('setheading',                  '設頭向','shetouxiang'),
('home',                        '回家','huijia'),

('circle',                      '畫圓', '圓','huayuan'),
('speed',                       '速度','sudu'),

('degrees',                     '角度','設角為度', '設圓為360度', '設角的單位為角度'),
('radians',                     '弳度', '弧度' ,'半徑數', '設角為弧', '設角的單位為半徑數', '設圓為2pi弧'),

('xcor',                        'x座標','座標x'),
('ycor',                        'y座標','座標y'),
('setx',                        '設x座標','設座標x'),
('sety',                        '設y座標','設座標y'),
('distance',                    '距離'),
('heading',                     '頭向'),
('towards',                     '朝向', '朝向xy' ),


('setpos',                      '設位置'),
('setposition',                 '設位置')

]



cListTPen= [
('TPen', '龜筆類', '烏龜畫筆類'),

('pensize',                     '筆粗', '筆粗細', '筆大小'),
('width',                       '筆寬', '寬'),
('penup',                       '提筆'),
('pendown',                     '下筆'),
('showturtle',                  '顯龜','顯示','顯'),
('hideturtle',                  '藏龜','隱藏','藏'),
('color',                       '顏色'),
('pencolor',                    '筆色'),
('speed',                       '速度'),
('pen',                         '筆', '筆屬性'),
('fillcolor',                   '填色'),

('isdown',                      '下筆嗎', '是否下筆', '下筆狀態'),
('isvisible',                   '顯龜嗎', '是否可見', '可見狀態'),

('pendown',                     '下筆'),
('fillcolor',                   '填色'),
('penup',                       '提筆'),



('resizemode',                  '重設大小模式', '設成可伸縮模式')


]



cListRawTurtle=[
('RawTurtle',                       '原龜類', '粗龜類', '原生龜類'),

('shapesize',                       '形狀大小', '大小', '龜大小'),
('shape',                           '形狀'),
('write',                           '寫'),
('begin_fill',                      '開始填', '開始填色'),
('end_fill',                        '結束填', '結束填色'),
('begin_poly',                      '開始多邊形'),
('clear',                           '清除'),
('clearstamp',                      '清除蓋章'),
('clearstamps',                     '清除蓋章群'),
('clone',                           '複製'),
('dot',                             '點', '畫點'),
('end_poly',                        '結束多邊形'),
('filling',                         '是否正在填色', '正在填色', '填色狀態'),
('get_poly',                        '取多邊形'),
('get_shapepoly',                   '取形狀多邊形'),
('getpen',                          '取筆'),
('getscreen',                       '取幕'),
('getturtle',                       '取龜'),

('onclick',                         '在點擊時', '在滑鼠點擊龜時'),
('ondrag',                          '在拖曳時', '在滑鼠拖曳龜時'),
('onrelease',                       '在鬆開時', '在滑鼠鬆開龜時', '在釋放時', '在滑鼠釋放龜時'),

('reset',                           '重設'),

#('screens',                         '幕群', '幕列表'),

('settiltangle',                    '設傾角', '設傾斜角度'),
('setundobuffer',                   '設回復暫存區'),
('shapetransform',                  '形狀轉換'),
('shearfactor',                     '扭曲因子', '設取扭曲因子'),
('stamp',                           '蓋章', '蓋印', '戳印'),
('tilt',                            '傾斜'),
('tiltangle',                       '傾斜角度'),
('turtlesize',                      '龜大小'), # 是否為 shapesize 的別名。
('undo',                            '回復'),
('undobufferentries',               '回復暫存區的個數', '回復暫存區的長度', '取回復暫存區的長度' ),
('write',                           '寫')

]


cList_Screen= [
('_Screen',     '_幕類','_螢幕類'),
('setup',       '設立'),
('title',       '設標題', '標題'),
('bye',         '再見'),
('exitonclick', '在點擊時離開', '離開在點擊時')
]


cListTurtle=[
('Turtle', '龜類', '烏龜類','生一隻龜'),
#('None', '無')
]

cListScreen=[
('Screen', '幕類', '螢幕類', '開幕'),
#('None', '無')
]

classBeChanged= ['TurtleScreenBase', 'TurtleScreen', 'TNavigator', 'TPen', 'RawTurtle', '_Screen',  'Screen', 'Turtle']

#
# 印出 物類內 別名表，可供 程式員 參考，以及作為 自動翻譯 的依據
#
def 印出物類內別名表():
    global classBeChanged

    for y in classBeChanged:
        cList= 'cList'+y
        ec= eval(cList)

        print('\n'+'-'*20)
        print('class ', y)
        print('-'*20+'\n')

        for x in ec:
            print(x)

    print('='*60+'\n')

#印出物類內別名表()



aClassL=[]
bClassL=[]
cClassL=[]
for y in classBeChanged: #= 'TurtleScreenBase'

    ey= eval(y)
    aClass= ip.getsource(ey)
    aClassL+= [aClass]

    #classTurtleScreenBase=''

    cList= 'cList'+y
    ec= eval(cList)
    #bClassL=[]
    for x in ec[1:]:
        for n in range(1,len(x)):
            bClass= ' '*4 + x[n] +'= '  + x[0] +'\n'
            #
            # 物類 內， 有 4 個空白
            #
            aClass+= bClass
            bClassL+= [bClass]

    x= ec[0]
    #cClassL=[]
    for n in range(1,len(x)):
        cClass= x[n] +'= '  + x[0] +'\n'
        #
        # 物類 外， 無 4 個空白。
        #
        aClass+= cClass
        cClassL+= [cClass]

    #print(aClass)

    exec(aClass)




#
# 全區別名，(global  alias)
#


字串別名表= [
 ('"Delete"',   '清除鍵'),
 ('"Down"',     '向下鍵'),
 ('"Home"',     '回家鍵'),
 ('"Left"',     '向左鍵'),
 ('"Right"',    '向右鍵'),
 ('"Up"',       '向上鍵'),
 ('"space"',    '空白鍵'),
 ('"Escape"',   '脫離鍵'),
 ('"black"',    '黑','黑色'),
 ('"blue"',     '藍','藍色'),
 ('"cyan"',     '青','青色'),
 ('"gray"',     '灰','灰色'),
 ('"green"',    '綠','綠色'),
 ('"magenta"',  '紫','紫色'),
 ('"orange"',   '橙','橙色'),
 ('"red"',      '紅','紅色'),
 ('"white"',    '白','白色'),
 ('"yellow"',   '黃','黃色'),
 ('"turtle"',   '龜形','烏龜形狀'),
 ('"square"',   '方形'),
 ('"logo"',     '角度從北開始順時針')
 ]


#
# 常用的就把它加在這裡
#

函數別名表= [
 ('None',               '無'),
 ('True',               '真'),
 ('False',              '假'),

 ('print',              '印'),
 ('range',              '範圍'),

 ('random.random',      '隨機數', '亂數'),
 ('random.choice',      '隨機選', '亂選'),
 ('random.randint',     '隨機整數', '亂整數'),
 ('random.sample',      '隨機取樣', '亂取樣'),

 #("['red','orange','yellow','green','cyan','blue','magenta']", '彩虹', '彩虹色群'),

 ('time.ctime', '看時間', '取時間'),
 ('time.sleep', '睡', '等時間'),
 ('time.time',  '時間'),

 ('Turtle', '龜類', '生龜','生一隻龜'),
 ('Screen', '幕類', '開幕'),

 ('Pen',                '筆類'),
 ('RawPen',             '原生筆類'),
 ('RawTurtle',          '原生龜類'),
 ('ScrolledCanvas',     '可捲畫布類'),
 ('Shape',              '形狀類'),
 ('TurtleScreen',       '龜幕類'),
 ('Vec2D',              '向量2D類', '二維向量類')

]


#
# 這一行是「別名」的關鍵語句
#

#'''

別名表 = 字串別名表 + 函數別名表

aCmd=''
for e in 別名表:
    #exec(e[1] + '=' + e[0] )
    for n in range(1,len(e)):
        aCmd += e[n] + '='+ e[0] + '\n'


#print(aCmd)

exec(aCmd)


中英對照表=[
    cListTurtleScreenBase,
    cListTurtleScreen,
    cListTNavigator,
    cListTPen,
    cListRawTurtle,
    cList_Screen,
    cListTurtle,
    cListScreen,
    字串別名表,
    函數別名表
    ]

def 印中英對照表():

    print('-'*20)
    print('中英對照表')
    print('-'*20)

    i= 0
    for x in 中英對照表:
        for y in x:
            print(i,y)
            i+=1

#印中英對照表()

#
#
#


#'''
#
# 設法來寫 help ...
#

def read_docstrings(lang=''):
    """Read in docstrings from lang-specific docstring dictionary.

    Transfer docstrings, translated to lang, from a dictionary-file
    to the methods of classes Screen and Turtle and - in revised form -
    to the corresponding functions.
    """

    #modname = "turtle_docstringdict_%(language)s" % {'language':lang.lower()}
    modname = "turtle_docstringdict_tc"
    #
    # turtle_docstringdict_tc.py
    #
    # 這是繁體中文說明文件，還在翻譯當中，先有個版本來寫程式。
    # 2014/03/22
    #

    bMsg= '''這是繁體中文說明文件，
    還在翻譯當中，尚未完成，先行請您試閱並包容錯誤，
    一切仍以英文說明為主。 2014/03/22
    '''
    aMsg='中文說明'

    module = __import__(modname)

    docsdict = module.docsdict

    i= 0
    for key in docsdict:
        try:
             #eval(key).im_func.__doc__ = docsdict[key] # 這行本來就 被原作者 mark 掉。

             #
             # 原作者用這行。
             #
             #eval(key).__doc__ =  docsdict[key]   # original version

             #
             # 我把它改成如下。
             #

             #eval(key).__doc__ += '\n\n'+ docsdict[key]  # renyuan make it += from =

             eval(key).__doc__ = '『%04d  '%(i)+ aMsg + '』\n'+ docsdict[key] + '\n\n' + eval(key).__doc__ # 出現次序調一下。
             #
             # 從原始 turtle.py 挖出這行程式碼，很珍貴。把 = 改成 += 就可把中文 help 黏進去
             #
             i+= 1

        except:
            print('''%s 說明文件輸入有誤，檢查： %s
            '''% (modname, key))

#'''
讀入繁體中文說明文件= read_docstrings
try:
    讀入繁體中文說明文件()
except:
    print('讀入繁體中文說明文件()， 失敗，跳過。' )
#'''



'''


for methodname in _tg_screen_functions:
    pl1, pl2 = getmethparlist(eval('_Screen.' + methodname))
    if pl1 == "":
        print(">>>>>>", pl1, pl2)
        continue
    defstr = ("def %(key)s%(pl1)s: return _getscreen().%(key)s%(pl2)s" %
                                   {'key':methodname, 'pl1':pl1, 'pl2':pl2})
    exec(defstr)
    eval(methodname).__doc__ = _screen_docrevise(eval('_Screen.'+methodname).__doc__)

'''

#
# 把類別內 函數 釋放到 類別外
#
#
# 從 turtle.py 學來的，還沒消化。
#

#
# 主要是把 物類內函數 的 (self, ...) 變成  (...)
#

from turtle import __all__, getmethparlist #, _getpen, _getscreen, _turtle_docrevise, _screen_docrevise #, _Screen, Turtle

'''
_龜= 龜類()
_幕= 幕類()
'''
def _取筆():
    """Create the 'anonymous' turtle if not already present."""

    if 龜類._pen is None:
        龜類._pen= 龜類()

    return 龜類._pen

def _取幕():
    """Create a TurtleScreen if not already present."""
    if 龜類._screen is None:
        龜類._screen = _幕類()  ###### 會不會就是這行搞鬼？？ 有無底線之分！

    return 龜類._screen

memberOfTurtle= ip.getmembers(龜類)

memberOfScreen= ip.getmembers(_幕類)

methodPutToMain=[]

cmdString=''
for mem in memberOfTurtle:

    m, mid= mem
    methodname= m

    #
    # 暴力 debug
    #
    if methodname == 'screens':
        continue

    if ord(m[0])>= ord('a'): #128: # 這一行是為了 僅要 中文 部分，英文部分原作者已經有，不需我多寫。
        '''
        cmd= m + '= ' + 'Turtle.' + m + '\n'
        cmdString += cmd
        '''

        methodPutToMain += [m]

        try:

            pl1, pl2 = getmethparlist(eval('龜類.' + methodname))
            if pl1 == "":
                print(">>>>>>", pl1, pl2)
                continue
            defstr = ("def %(key)s%(pl1)s: return _取筆().%(key)s%(pl2)s" %
                                           {'key':methodname, 'pl1':pl1, 'pl2':pl2})
            cmdString += defstr +'\n\n'

            exec(defstr)
            eval(methodname).__doc__ = eval('龜類.'+methodname).__doc__ # _turtle_docrevise(eval('龜類.'+methodname).__doc__)

        except:
            print('龜類.' + methodname +' No put to main')

for mem in memberOfScreen:

    m, mid= mem
    methodname= m

    #
    # 暴力 debug
    #
    if methodname == 'screens':
        continue

    if ord(m[0])>= ord('a'): #128:
        '''
        cmd= m + '= ' + 'Turtle.' + m + '\n'
        cmdString += cmd
        '''

        methodPutToMain += [m]

        try:

            pl1, pl2 = getmethparlist(eval('_幕類.' + methodname))
            if pl1 == "":
                print(">>>>>>", pl1, pl2)
                continue
            defstr = ("def %(key)s%(pl1)s: return _取幕().%(key)s%(pl2)s" %
                                           {'key':methodname, 'pl1':pl1, 'pl2':pl2})
            cmdString += defstr +'\n\n'

            exec(defstr)
            eval(methodname).__doc__ = eval('_幕類.'+methodname).__doc__# _screen_docrevise(eval('_幕類.'+methodname).__doc__)
        except:
            print('_幕類.' + methodname +' No put to main')

#print(cmdString)
#exec(cmdString)

__all__ += methodPutToMain


for x in 別名表:
    for y in x[1:]:
        __all__ +=  [y]


__all__ += ['中英對照表']

#'''
def 印可用的詞彙別名表():

    print('-'*10)
    print('可用的詞彙別名表')
    print('-'*10)
    print('__all__= ',sorted(__all__))

#印可用的詞彙別名表():

#'''

#
# 模組到此結束。以下為測試。
#
#################################################################

def 展示00_程序性程式設計():

    開幕()

    標題('「無名」小烏龜。')

    W= 100

    設座標系統(-W,-W,W,W)


    形狀(龜形)
    顏色(紅)

    速度(10)

    寫('大家好，我是「無名」小烏龜。')

    for i in range(10):
        前進(100)
        左轉(170)
        顏色(隨機數(), 隨機數(), 隨機數())
        畫點 ()

    回家()
    清除()
    畫圓(50)
    寫('''
    我做完了，
    幕進入主迴圈等你吩咐，
    你可以點擊 X 結束。
    ''')

    #在點擊時離開()  # 會再開出新螢幕，不知為何？？
    閉幕()



def 展示01_物件導向程式設計():


    幕= 螢幕類()
    幕.標題('一群小烏龜。')

    W= 100
    幕.設座標系統(-W,-W,W,W)

    for i in 範圍(7):

        龜= 烏龜類()

        龜.形狀(龜形)
        龜.顏色(彩虹[i%7])
        睡(1)

        龜.速度(10)

        龜.寫('大家好，我是小烏龜 %d 。'%(i))
        龜.提筆()
        龜.前往((隨機數()-.5)*W/2, (隨機數()-.5)*W/2)
        龜.下筆()

        for i in range(10):
            龜.前進(100)
            龜.左轉(170)
            #龜.顏色(隨機數(), 隨機數(), 隨機數())
            龜.畫點 ()

        #龜.回家()
        #龜.清除()
        龜.畫圓(10)

    龜.寫('''
    我做完了，
    幕進入主迴圈等你吩咐，
    你可以點擊 X 結束。
    ''')

    幕.主迴圈()

def 展示02():
    '''
    星形
    '''

    for N in 範圍(5,9):
        for k in 範圍(1,6):

            清除()
            下筆()
            寫('(N,k)= (%d, %d)'%(N, k))

            for i in 範圍(N):
                前進(100)
                左轉(k*360/N)

            回家()

    主迴圈()




def 陰陽():

    def 半陰陽(半徑, 色1, 色2):

        形狀(龜形); 
        顏色(色1, 色2); 開始填色();
        畫圓(半徑/2, 180); 畫圓(半徑, 180); 左轉(180); 畫圓(-半徑/2, 180);
        結束填色()

        左轉(90); 提筆(); 前進(半徑/3); 右轉(90); 下筆();
        顏色(色2, 色1); 開始填色();
        畫圓(半徑/6);
        結束填色()

        左轉(90); 提筆(); 後退(半徑/3);左轉(90); 下筆();

    重設(); 半陰陽(200,  白, 黑);  半陰陽(200,  黑, 白);

    提筆();後退(200); 左轉(90); 後退(200);
    顏色(紅); 寫(ip.getsource(陰陽))

    進入主迴圈()

    return "完成!"

demo= 展示=  陰陽

if __name__ == "__main__":

    #展示00_程序性程式設計()
    #展示01_物件導向程式設計()

    #展示02()

    展示()

    pass

