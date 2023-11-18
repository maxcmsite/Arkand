import pygame
from random import randint
from threading import Thread
from time import sleep
import os
pygame.init()
sc = pygame.display.set_mode()
w, h = pygame.display.get_surface().get_size()
def auto_size_display():
	global w,h
	while True:
		w, h = pygame.display.get_surface().get_size()
		sleep(0.1)
Thread(target=auto_size_display,daemon=True).start()
FPS = 60
clock = pygame.time.Clock()
x1=w*.5
y1=h*.5
vx1=randint(-1,1)
vy1=randint(-1,1)
x2=w*.5
y2=h*.5
vx2=randint(-1,1)
vy2=randint(-1,1)
size1=15
count1=0
count2=0
pl_size=200
pl2=w*.5-pl_size*.5
pl1=w*.5-pl_size*.5
speed=1
th1r=False
start_game=False
path=os.path.dirname(os.path.abspath(__file__))
strt1='1 player'
strt2='2 player'
game1=False
color1=[0,0,0]
clmin1=0
clr1=0
clg1=0
clb1=0
clrad1=randint(0,2)
print(clrad1)
sound1=pygame.mixer.Sound(path+'/metal_ball_l01.mp3')
sound2=pygame.mixer.Sound(path+'/asu.mp3')
soundr=True
soundt=0
if clrad1==0:
	clr1=1
elif clrad1==1:
	clr1=1
elif clrad1==2:
	clb1=1
sleep(1)
while start_game==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.FINGERDOWN:
			if event.finger_id==0:
				if event.x*w>w*.5-140 and event.x*w<w*.5-140+270 and event.y*h>h*.5-55 and event.y*h<h*.5-55+75:
					start_game=True
					game1=True
				if event.x*w>w*.5-140 and event.x*w<w*.5-140+270 and event.y*h>h*.5+30 and event.y*h<h*.5+30+75:
					start_game=True
					game1=False
				if event.x>.8 and event.x*w<w*.8+100 and event.y*h>h*.065 and event.y*h<h*.065+75:
					soundt=0
				if event.x>.8 and event.x*w<w*.8+100 and event.y*h>h*.14 and event.y*h<h*.14+75:
					soundt=1
				if event.x>.8 and event.x*w<w*.8+100 and event.y*h>h*.215 and event.y*h<h*.215+75:
					if soundr==True:
						soundr=False
					else:
						soundr=True
	if x2>w-size1:
		vx2=-1
	elif x2<0+size1:
		vx2=1
	if vx2==-1:
		x2+=-10
	else:
		x2+=10
	if y2>h-size1:
		vy2=-1
	elif y2<0+size1:
		vy2=1
	if vy2==-1:
		y2+=-10
	else:
		y2+=10
	if clrad1==0:
		if clr1==1 and color1[0]<255:
			color1[0]+=1
		elif clr1==-1 and color1[0]>0:
			color1[0]+=-1
		if color1[0]==255:
			clr1=-1
		elif color1[0]==0:
			clr1=1
	elif clrad1==1:
		if clg1==1 and color1[1]<255:
			color1[1]+=1
		elif clg1==-1 and color1[1]>0:
			color1[1]+=-1
		if color1[1]==255:
			clg1=-1
		elif color1[1]==0:
			clg1=1
	elif clrad1==2:
		if clb1==1 and color1[2]<255:
			color1[2]+=1
		elif clb1==-1 and color1[2]>0:
			color1[2]+=-1
		if color1[2]==255:
			clb1=-1
		elif color1[2]==0:
			clb1=1
	pygame.draw.circle(sc, color1, (x2, y2), size1)
	font2=pygame.font.SysFont('Comic Sans MS',100)
	font3=pygame.font.SysFont('Comic Sans MS',50)
	text3=font2.render(strt1,True,(255,255,255))
	text4=font2.render(strt2,True,(255,255,255))
	text5=font3.render('ball',True,(255,255,255))
	text6=font3.render('asu',True,(255,255,255))
	if soundr==True:
		text7=font3.render('on',True,(255,255,255))
	else:
		text7=font3.render('off',True,(255,255,255))
	sc.blit(text3, (w*.5-140,h*.5-50))
	sc.blit(text4, (w*.5-140,h*.5+30))
	sc.blit(text5, (w*.825,h*.065))
	sc.blit(text6, (w*.825,h*.14))
	sc.blit(text7, (w*.84,h*.215))
	pygame.draw.rect(sc, (255,255,255), pygame.Rect(w*.5-140, h*.5-55, 275, 75),  2)
	pygame.draw.rect(sc, (255,255,255), pygame.Rect(w*.5-140, h*.5+30, 275, 75),  2)
	if soundt==0:
		pygame.draw.rect(sc, (0,255,0), pygame.Rect(w*.8, h*.05, 100, 75),  2)
		pygame.draw.rect(sc, (255,255,255), pygame.Rect(w*.8, h*.125, 100, 75),  2)
	elif soundt==1:
		pygame.draw.rect(sc, (255,255,255), pygame.Rect(w*.8, h*.05, 100, 75),  2)
		pygame.draw.rect(sc, (0,255,0), pygame.Rect(w*.8, h*.125, 100, 75),  2)
	if soundr==True:
		pygame.draw.rect(sc, (0,255,0), pygame.Rect(w*.8, h*.2, 100, 75),  2)
	else:
		pygame.draw.rect(sc, (255,255,255), pygame.Rect(w*.8, h*.2, 100, 75),  2)
	pygame.display.update()
	sc.fill((0,0,0))
	clock.tick(FPS)
sleep(.5)
while start_game==True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.FINGERMOTION:
			if game1==True:
				if event.finger_id==0:
					pl2=event.x*w-pl_size*.5
			elif game1==False:
				if event.finger_id==0:
					if event.y<.5:
						pl1=event.x*w-pl_size*.5
					elif event.y>.5:
						pl2=event.x*w-pl_size*.5
				if event.finger_id==1:
					if event.y<.5:
						pl1=event.x*w-pl_size*.5
					elif event.y>.5:
						pl2=event.x*w-pl_size*.5
	if game1==True:
		pl1=x1-pl_size*.5
	sc.fill((0,0,0))
	pygame.draw.line(sc,(255,255,255),[0,round(h*.5)],[w,round(h*.5)])
	pygame.draw.circle(sc, (0,255,0), (x1, y1), size1)
	font1=pygame.font.SysFont('Comic Sans MS',100)
	text1=font1.render(str(count1),True,(255,255,255))
	text1=pygame.transform.rotate(text1, 180)
	sc.blit(text1, (w-100,h*.5-100))
	text2=font1.render(str(count2),True,(255,255,255))
	pygame.draw.line(sc,(255,255,255),[pl1,round(h*.1)],[pl1+pl_size,round(h*.1)],15)
	pygame.draw.line(sc,(255,255,255),[pl2,round(h*.9)],[pl2+pl_size,round(h*.9)],15)
	sc.blit(text2, (100,h*.5+25))
	def sys_game():
		global x1,y1,vx1,vy1,speed,size1,pl_size,pl1,pl2,th1r,count1,count2,sc
		while True:
			if x1>w-size1:
				vx1=-1
				if soundr==True:
					if soundt==0:
						sound1.play()
					elif soundt==1:
						sound2.play()
			elif x1<0+size1:
				vx1=1
				if soundr==True:
					if soundt==0:
						sound1.play()
					elif soundt==1:
						sound2.play()
			if vx1==-1:
				x1+=-speed
			else:
				x1+=speed
			if y1>h-size1:
				vy1=-1
				count1+=1
				speed=1
				pl_size=200
				if soundr==True:
					if soundt==0:
						sound1.play()
					elif soundt==1:
						sound2.play()
			elif y1<0+size1:
				vy1=1
				count2+=1
				speed=1
				pl_size=200
				if soundr==True:
					if soundt==0:
						sound1.play()
					elif soundt==1:
						sound2.play()
			elif x1<pl2+pl_size and x1>pl2 and y1>h*.9-15*.5-size1 and y1<h*.9+15*.5+size1:
				if vy1==1:
					vy1=-1
					if soundr==True:
						if soundt==0:
							sound1.play()
						elif soundt==1:
							sound2.play()
				elif vy1==-1:
					vy1=1
					if soundr==True:
						if soundt==0:
							sound1.play()
						elif soundt==1:
							sound2.play()
				if speed<49:
					speed+=1
				elif speed>=49:
					if pl_size>99:
						pl_size+=-1
			elif x1<pl1+pl_size and x1>pl1 and y1>h*.1-15*.5-size1 and y1<h*.1+15*.5+size1:
				if vy1==1:
					vy1=-1
					if soundr==True:
						if soundt==0:
							sound1.play()
						elif soundt==1:
							sound2.play()
				elif vy1==-1:
					vy1=1
					if soundr==True:
						if soundt==0:
							sound1.play()
						elif soundt==1:
							sound2.play()
				if speed<49:
					speed+=1
				elif speed>=49:
					if pl_size>99:
						pl_size+=-1
			if vy1==-1:
				y1+=-speed
			else:
				y1+=speed
			th1r=True
			sleep(0.01)
	if th1r==False:
		Thread(target=sys_game).start()
	pygame.display.update()
	clock.tick(FPS)