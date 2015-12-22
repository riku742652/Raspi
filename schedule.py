#coding: UTF-8

import time
import commands
import datetime
import random

Mon=[" ", "情報ネットワーク", " ", "基礎化学"]
Tue=["プロジェクトデザイン実践", "プロジェクトデザイン実践", " ", "日本学"]
Wed=["コンピュータアーキテクチャ基礎", "ビジネスコミュニケーション"]
Thu=["情報理論", "オペレーティングシステム１", " ", " "]
Fri=["情報工学実験２", "ソフトウェア工学", " ", "形式言語とオートマトン"]
#Sat=[]
#Sun=[]
rand = ["今日もいちにち頑張るぞい", "忘れ物はないか確認してください", "今日も元気に行ってらっしゃい"]



d = datetime.datetime.now()
day = d.weekday()
e = random.randint(0,2)

commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "今日の授業は"|aplay')


if(day == 0):
	for i in range(0,4):
		print Mon[i]
		if(Mon[i] != " "):
			commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s限目"|aplay'%str(i+1))
			commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%Mon[i])

if(day == 1):
        for i in range(0,4):
                print Tue[i]
                if(Tue[i] != " "):
                        commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s限目"|aplay'%str(i+1))
                        commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%Tue[i])

if(day == 2):
        for i in range(0,4):
                print Wed[i]
                if(Wed[i] != " "):
                        commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s限目"|aplay'%str(i+1))
                        commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%Wed[i])

if(day == 3):
        for i in range(0,4):
                print Thu[i]
                if(Mon[i] != " "):
                        commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s限目"|aplay'%str(i+1))
                        commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%Thu[i])

if(day == 4):
        for i in range(0,4):
                print Fri[i]
                if(Fri[i] != " "):
                        commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s限目"|aplay'%str(i+1))
                        commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%Fri[i])



commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "です。"|aplay')
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%rand[e])
