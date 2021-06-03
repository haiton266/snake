import pygame,sys,random,time
from pygame.locals import *


pygame.init()

pygame.display.set_caption('The Hunting Snake ')
font = pygame.font.SysFont("monospace", 36)
font2 = pygame.font.SysFont("monospace",16)
screen = pygame.display.set_mode((1000,700))
running = True
VIEN = (105,55,50)
NEN = (28,47,77)
RED = (194,134,134)
GREEN = (137,176,144)
WHITE = (255,255,255)
YL_GR = (138,179,45)
BLACK = (0,0,0)
count = 0
x_bait=470;y_bait=290;
FPS = 10
fpsClock = pygame.time.Clock()

# SNAKE
SNAKE = pygame.Surface((500, 500),SRCALPHA)
pygame.draw.rect(SNAKE,YL_GR,(0,0,20,20));
pygame.draw.circle(SNAKE,BLACK,(14,10),2.5)
x_snake = 300;y_snake=300;

trai = False;phai=True; lenn=False; xuong=False
len_snake = 2;


x = [x_snake,0]
y = [y_snake,0]

def reset():
	global x,running,count,x_bait,y_bait,FPS,fpsClock,SNAKE,x_snake,y_snake,len_snake,x,y
	running = True
	count = 0
	x_bait=470;y_bait=290;
	FPS = 10
	fpsClock = pygame.time.Clock()

	# SNAKE
	SNAKE = pygame.Surface((500, 500),SRCALPHA)
	pygame.draw.rect(SNAKE,YL_GR,(0,0,20,20));
	pygame.draw.circle(SNAKE,BLACK,(14,10),2.5)
	x_snake = 300;y_snake=300;

	trai = False;phai=True; lenn=False; xuong=False
	len_snake = 2;


	x = [x_snake,0]
	y = [y_snake,0]

def ditheo():
	i=len_snake-1
	while i>=2:
		x[i] = x[i-1]
		y[i] = y[i-1]
		i-=1 
bait_sizee = 1
ct = True
while running == True:
	while ct == True:
		screen.fill(NEN)
		pygame.draw.rect(screen,VIEN,(20,100,960,580))
		pygame.draw.rect(screen,NEN,(40,120,920,540))

		TEXT0 = font.render('THE HUNTING SNAKE',True,RED);screen.blit(TEXT0,(200,25))
		TEXT1 = font.render('SCORE: ',True,RED);screen.blit(TEXT1,(700,25))
		DIEM  = font.render(str(count),True,RED);screen.blit(DIEM,(830,25))

		# pygame.draw.rect(SNAKE,GREEN,(0,0,20,20));

		#bait
		if bait_sizee == 2:
			pygame.draw.circle(screen,VIEN,(x_bait,y_bait),20)
		else: pygame.draw.circle(screen,VIEN,(x_bait,y_bait),10)
		#Move
		ditheo()
		x[1]=x_snake
		y[1]=y_snake
		if trai==True: x_snake-=20
		if phai==True: x_snake+=20
		if lenn==True: y_snake-=20
		if xuong==True: y_snake+=20


		screen.blit(SNAKE, (x_snake, y_snake))
		for i in range(1,len_snake):
			pygame.draw.rect(screen,GREEN,(x[i],y[i],20,20));
		

		
		#score
		def eat():
			global len_snake,x_bait,y_bait,trai,phai,lenn,xuong,x,y,bait_sizee
			len_snake+=1;
			x_bait = random.randrange(50,880,20)
			y_bait = random.randrange(130,420,20)
			if trai==True: x.append(int(x[len_snake-2]+20));y.append(int(y[len_snake-2]));
			if phai==True: x.append(int(x[len_snake-2]-20));y.append(int(y[len_snake-2]));
			if lenn==True: x.append(int(x[len_snake-2]));y.append(int(y[len_snake-2]+20));
			if xuong==True: x.append(int(x[len_snake-2]));y.append(int(y[len_snake-2]-20));		
			bait_sizee = random.randrange(1,6)

		if bait_sizee == 2:
			if (x_snake+10 == x_bait and y_snake+10 == y_bait) or (x_snake+10+20 == x_bait and y_snake+10 == y_bait) or (x_snake+10-20 == x_bait and y_snake+10 == y_bait) or (x_snake+10 == x_bait and y_snake+10 == y_bait+20) or (x_snake+10 == x_bait and y_snake+10 == y_bait-20):
				eat();count+=10
		elif x_snake+10 == x_bait and y_snake+10 == y_bait: eat();count+=5
			
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == K_LEFT: trai=True;phai=False;lenn=False;xuong=False;
				if event.key == K_RIGHT: phai=True;trai=False;lenn=False;xuong=False;
				if event.key == K_UP: lenn=True;xuong=False;trai=False;phai=False;
				if event.key == K_DOWN: xuong=True;lenn=False;trai=False;phai=False;
		if x_snake<40 or x_snake>960 or y_snake<120 or y_snake>660 : 
			pygame.draw.rect(screen,WHITE,(340,300,300,90),2)
			TEXTT = font.render('GAME OVER',True,WHITE)
			screen.blit(TEXTT,(380,325))
			text_space = font2.render('Press Space to start again',True,WHITE)
			screen.blit(text_space,(365,365))
			#time.sleep(5)
			ct = False
		if event.type == pygame.QUIT:
			ct = False
			running = False
		# pygame.display.update()	
		fpsClock.tick(FPS+count//10)
		pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			# print('ok')
			if event.key == K_SPACE: ct = True;reset()
		if event.type == pygame.QUIT:
				running = False


pygame.quit()
