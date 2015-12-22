# *- coding: utf-8 -*-

import commands
import random
import RPi.GPIO as GPIO
from time import sleep

list = ["おはよう", "こんにちは", "こんばんは", "ハロー", "今日もいちにち頑張るぞい！", "心がぴょんぴょんするんじゃぁーー", "ダレカタスケテー", "調子はどうですか？", "おやすみなさい", "今日もいちにち、お疲れさまでした", "お休みなさい", "また明日も頑張りましょう", "罰金バッキンガムよー", "心配はノンノンノートルダムよ", "しゃべる余裕はありま温泉", "にゃんぱすー", "今何してますか？", "ゆっくりしていってね", "どうしよう東照宮", "宿題はやりましたか？", "僕に勝てるわけないでしょ？", "あぁー気持ちいいんじゃぁー", "２４歳、学生です。", "あくしろよ", "じゃけん夜行きましょうねー", "あぁいいっすね", "トランザム！", "バーロー", "おはようごじゃいまーす", "あばばばばばば", "イキすぎィ！", "あそこが罰金バッキンガムよ"]

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(24,GPIO.IN)
#GPIO.setup(22,GPIO.OUT)

while(1):
#	if(GPIO.input(24)):
		i = random.randint(0,len(list))
#		GPIO.output(22,True)
		commands.getoutput('../aquestalkpi/AquesTalkPi "%s"| aplay' %list[i])
		print (list[i])
#		print(GPIO.input(24))
#		time.sleep(10)
#		GPIO.cleanup()
