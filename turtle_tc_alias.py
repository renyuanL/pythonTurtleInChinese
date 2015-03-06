'''

turtle_tc_alias.py

2015/01/21

'''
#
# 物類內別名，(Inside-class alias)
#


cListTurtleScreenBase=[
('TurtleScreenBase', '龜幕基類', '烏龜螢幕地基類'),
('mainloop'  ,   '主迴圈', '進入主迴圈', '做完了', '點擊X結束', '等待閉幕', '閉幕'),
('numinput'  ,   '輸入數字'),
('textinput' ,   '輸入文字'),
]



cListTurtleScreen=[
('TurtleScreen',                '龜幕類', '烏龜螢幕類'),

('addshape',                    '加形狀'),
('bgcolor',                     '背景色'),
('bgpic',                       '背景圖'),
#('clear',                       '清除'),  # 這個會和 turtle 中 的 clear 衝突！！ 2015/01/13
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
('TNavigator', '龜行類', '烏龜航行類'),

('reset',                       '重設'),
('forward',                     '前進'),
('back',                        '後退'),
('right',                       '右轉'),
('left',                        '左轉'),
('pos',                         '位置'),
('goto',                        '前往', '設位置', '去到'),
('setheading',                  '設頭向'),
('home',                        '回家'),

('circle',                      '畫圓', '圓'),
('speed',                       '速度'),

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
('setposition',                 '設位置'),

('fd',       '前進'),      #= forward  # 以下是漏網之魚，2015/01/10
('bk',       '後退'),      #= back
('backward', '後退'),      # = back
('rt',       '右轉'),      #= right
('lt',       '左轉'),      #= left
('position', '位置'),      #= pos
('seth',     '設頭向')     # = setheading

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



('resizemode',                  '重設大小模式', '設成可伸縮模式'),

('up',      '提筆'),              #= penup # 漏網之魚， 2015/01/10
('pu',      '提筆'),              #= penup
('pd',      '下筆'),              #= pendown
('down',    '下筆'),              #= pendown
('st',      '顯龜','顯示','顯'),   #= showturtle
('ht',      '藏龜','隱藏','藏')    #= hideturtle


]



cListRawTurtle=[
('RawTurtle',                       '原龜類', '粗龜類', '原生龜類'),

('shapesize',                       '形狀大小', '大小', '龜大小'),
('shape',                           '形狀', '形'),
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

cListShape=[
('Shape','形狀類'),
('addcomponent',    '加成員')
]

cListVec2D=[
('Vec2D', '向量類', '二維向量類'),
('rotate', '旋轉')

]



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


 ('Pen',                '筆類'),  #2015/01/03
 ('RawPen',             '原生筆類'),
 ('RawTurtle',          '原生龜類'),
 ('ScrolledCanvas',     '可捲畫布類'),
 ('Shape',              '形狀類'),
 ('TurtleScreen',       '龜幕類'),
 ('Vec2D',              '向量類', '二維向量類', '向量2D類'),

 ('Turtle', '龜類', '生龜','生一隻龜', 'Pen', '筆類'), # 2015/01/03 # Pen 與 Turtle 需產生連結。
 ('Screen', '幕類', '開幕')

]



總別名表=[
    cListShape,
    cListVec2D,
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
