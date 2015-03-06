'''
turtle_tc_2015.py --> turtle_tc.py

Renyuan Lyu
2014/05/25,

last updated: 
2014/12/24, 
2015/01/18

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

Python 3.0 以後， 變數、函數、
以及物類、方法、屬性等名稱都使用  Utf-8 編碼，

允許 程式員 運用 其母語來寫作程式，
只要我們鑽進眾多模組內部，為每個物類的函數名稱給個母語別名，
再把相應的 doc 文件說明也轉成母語，
這個基本工程將建立起母語寫作程式的基礎環境，
程式教育就有可能向下紮根，到達高中，甚至是國中的階段。

本程式模組就是在這個想法之下的首次嘗試，
我們把 Python 中， 一個頗負盛名的模組，turtle.py，
為其提供一個繁體中文 (traditional Chinese) 的附加模組，
命名為 turtle_tc.py，

使用者只要把本程式模組放在 python 環境下，模組的搜尋路徑內，
一般為當前程式碼的目錄 (current dir)或是 C:/Python3.x/Lib/，
那麼，你就可以用
import turtle_tc
來取代
import turtle

進而，運用中文來寫基於 龜 的作圖程式，就成為可能。



last updated: 2014/12/24, 2015/01/21

'''
#
# The following are imported in turtle.py originally
# they will not be imported automatically using 
#
# from turtle import *
#
# so we need include them here
#

import tkinter as TK
import types
import math
import time
import inspect
import sys

from os.path import isfile, split, join
from copy import deepcopy
from tkinter import simpledialog

# ############################################


import random

from turtle import *
from turtle import _CFG, _Screen, _Root, TK, _TurtleImage, Tbuffer, TurtleGraphicsError
from turtle import TurtleScreenBase, TurtleScreen, TNavigator, TPen, RawTurtle, Canvas #, Turtle, Screen



import inspect as ip
import random as rd

'''
隨機數= rd.random
隨機整數= rd.randint
時間= time.time
睡= time.sleep
'''

from turtle_tc_alias import *  ## 把所有別名列表都移出去了

classBeChanged= [
    'Vec2D', 
    'Shape', 
    'TurtleScreenBase', 
    'TurtleScreen', 
    'TNavigator', 
    'TPen', 
    'RawTurtle', 
    '_Screen',  
    'Screen',  # this is a little bit strange, Screen is a function
    'Turtle'
]

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


X=[]

for y in 總別名表:
    for x in y:
        X += [x]

中英對照表= sorted(X)

def 印中英對照表():

    print('-'*20)
    print('中英對照表')
    print('-'*20)

    for i,x in enumerate(中英對照表):
            print(i,x)

if __name__=='__main__':
    印中英對照表()



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

    try:
        module = __import__(modname)
    except:
        print('%s.py 不存在， 略過！ turtle_tc  還是可用，只是沒有中文求助功能！'%modname)
        return

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
            print('''%s 說明文件輸入有誤，請檢查： %s
            '''% (modname, key))

#'''
讀入繁體中文說明文件= read_docstrings
try:
    讀入繁體中文說明文件()
except:
    print('想要 讀入繁體中文說明文件()，但是 %s.py 不存在，先略過。'%modname)
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

from turtle import __all__
__tcAll__= __all__[:]

from turtle import getmethparlist #, _getpen, _getscreen, _turtle_docrevise, _screen_docrevise #, _Screen, Turtle

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

__tcAll__ += methodPutToMain

#from turtle import _CFG, _Screen, _Root, TK, _TurtleImage, Tbuffer, TurtleGraphicsError
#from turtle import TurtleScreenBase, TurtleScreen, TNavigator, TPen, RawTurtle, Canvas #, Turtle, Screen

__tcAll__ += ['向量類', '形狀類', '龜幕基類', '龜幕類','龜行類','龜筆類','原生龜類', 'TK'] # 2014/12/30, 處理 two_canvases_tc.py 時遇到！

for x in 別名表:
    for y in x[1:]:
        __tcAll__ +=  [y]


__tcAll__ += ['中英對照表']

__all__= __tcAll__[:]  

#
# 用上面這幾行 (__tcAll__[:] 的功勞) 
# 抵抗了 與 turtle.__all__ 的糾纏, 
# 原先 是 __all__ 來自 turtle, 然後 一路   += ， 
# 那樣是錯的，
# 因為 turtle_tc.__all__ 就與 turtle.__all__ 糾纏不清了。
# 2015/01/18
#

#'''
def 印可用的詞彙別名表():

    print('-'*10)
    print('可用的詞彙別名表 (中英對照表)')
    print('-'*10)
    print('__all__= ',sorted(__all__))

if __name__=='__main__':
    印可用的詞彙別名表()

#'''

#
# 模組到此結束。以下為測試。
#
#################################################################

def 陰陽太極圖():

    def 陰(半徑, 顏色1, 顏色2):
        筆寬(3); 顏色(黑, 顏色1)
        開始填(); 
        畫圓(半徑/2., 180); 畫圓(半徑, 180); 左轉(180); 畫圓(-半徑/2., 180); 
        結束填()
        左轉(90); 提筆(); 前進(半徑*0.35); 右轉(90); 下筆(); 顏色(顏色1, 顏色2)
        開始填(); 畫圓(半徑*0.15); 結束填()
        左轉(90); 提筆(); 後退(半徑*0.35); 下筆(); 左轉(90);
        
    陰(100, 黑, 白)
    陰(100, 白, 黑)




class 陰陽龜類(龜類):

    def __init__(我, 位置= (0,0)):
        龜類.__init__(我)
        我.提筆()
        我.前往(位置)
        我.下筆()
        我.陰(100, 黑, 白)
        我.陰(100, 白, 黑)
        

    
    def 陰(我, 半徑, 顏色1, 顏色2):
        
        我.筆寬(3); 我.顏色(黑, 顏色1)
        我.開始填(); 
        我.畫圓(半徑/2., 180); 我.畫圓(半徑, 180); 我.左轉(180); 我.畫圓(-半徑/2., 180); 
        我.結束填()
        我.左轉(90); 我.提筆(); 我.前進(半徑*0.35); 我.右轉(90); 我.下筆(); 我.顏色(顏色1, 顏色2)
        我.開始填(); 我.畫圓(半徑*0.15); 我.結束填()
        我.左轉(90); 我.提筆(); 我.後退(半徑*0.35); 我.下筆(); 我.左轉(90);
        

if __name__ == '__main__':
    
    # 程序型
    陰陽太極圖()
    
    # 物件導向
    龜1= 陰陽龜類((200,200))
    '''
    龜2= 陰陽龜類((-200,+200))
    龜3= 陰陽龜類((-200,-200))
    龜4= 陰陽龜類((+200,-200))
    '''