pythonTurtleInChinese
=====================

pythonTurtleInChinese .....

turtle_tc.py

Renyuan Lyu
2014/05/25

renyuan.lyu@gmail.com

http://google.com/+RenyuanLyu




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

