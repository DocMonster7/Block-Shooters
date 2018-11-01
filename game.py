import random
import pygame

pygame.init()

res = (300,300)
win = pygame.display.set_mode(res)
pygame.display.set_caption("Block Shooter")
fr = pygame.time.Clock()
cBlack = (0,0,0)
cRed = (255,0,0)
cGreen = (0,255,0)
cBlue = (0,0,255)
cWhite = (255,255,255)

x=25
y=275
x1=x
y1=y
x2=0
y2=0
width=25
height=25
vel = 10
run = True
mfont = pygame.font.Font('comicz.ttf', 20)

def renderonwin():
	win.fill(cBlack)
	text = mfont.render("Score :" + str(Score),True,cWhite)
	win.blit(text,(145,0))
	shoot()
	enemy()
	pygame.draw.rect(win,cBlue,(x,y,width,height))

	pygame.display.update()

def enemy():
	pygame.draw.rect(win,cRed,(x2,y2,20,20))

def shoot():
	pygame.draw.rect(win,cWhite,(x1,y1,10,10))

bullet = True
enemydead = True
Score = 0


while run:
	fr.tick(30)
	if enemydead == True:
		x2 = random.randint(0,270)
		y2 = random.randint(75,100)

	enemydead = False
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keyp = pygame.key.get_pressed()

	if bullet == True:
		if y1 > 0:
			y1 -= vel
		else:
			bullet = False

	if y1 >= y2 and y1 <= y2+20:
		if x1 >= x2 and x1 <= x2+20:
			Score  += 1
			enemydead = True


	if keyp[pygame.K_SPACE]:
		x1=x
		y1=y
		bullet = True

	if keyp[pygame.K_RIGHT]:
		if x < res[1]-width:
			x += vel
	if keyp[pygame.K_LEFT]:
		if x > 0:
			x -= vel

	renderonwin()
pygame.quit()