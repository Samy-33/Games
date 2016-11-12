#!/usr/bin/env python

import os, sys
import pygame, random

pygame.init()

size = (600, 600)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Pick Apple")
pygame.display.update()
high_scoref = open("high_score", "r")
clock = pygame.time.Clock()
try:
	high_score = int(high_scoref.readline())
except:
	high_score = 0
high_scoref.close()
left_hand_pos = [160, 400, 40, 10]
right_hand_pos = [240, 400, 40, 10]
head_x = 210
stomach_x = 200
speed = 5
legs_x = [205, 225]
pos_apple_x = 0
pos_apple_y = 0
apple_presence = False
picked = False
gameOver = False
run = 0

font = pygame.font.SysFont(None, 25)

def showScore(a, color, coords):
	text = font.render(a, True, color)
	canvas.blit(text, coords)
	
def show_msg(msg, coord):
	fontM = pygame.font.SysFont(None, 40)
	text = fontM.render(msg, True, red)
	canvas.blit(text, coord)

score = 0

mainMenu = False
while not mainMenu:
	#print event
	if not gameOver:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				mainMenu = True
				break
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if left_hand_pos[0]-10 >= 15:
						run = -10
						#left_hand_pos[0] -= 15
						#right_hand_pos[0] -= 15
						#head_x -= 15
						#stomach_x -= 15
						#legs_x[0] -= 15
						#legs_x[1] -= 15
				if event.key == pygame.K_RIGHT:
					if right_hand_pos[0]+50 <= 590:
						run = 10
						#right_hand_pos[0] += 15
						#left_hand_pos[0] += 15
						#head_x += 15
						#stomach_x += 15
						#legs_x[0] += 15
						#legs_x[1] += 15
			if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
				run = 0
	else:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				mainMenu = True
	canvas.fill((0, 50, 100))
	#left_hand_pos[0] -= 15
	#right_hand_pos[0] -= 15
	#head_x -= 15
	#stomach_x -= 15
	#legs_x[0] -= 15
	#legs_x[1] -= 15
	if not gameOver:
		#left_hand_pos[0] += run
		#right_hand_pos[0] += run
		#head_x += run
		#stomach_x += run
		#legs_x[0] += run
		#legs_x[1] += run
		if not apple_presence:
			pos_apple_x = random.randrange(0, 590)
			apple_presence = True
			picked = False
		if not picked:
			pygame.draw.rect(canvas, (200, 100, 0), [pos_apple_x, pos_apple_y, 10, 10])
		if left_hand_pos[0]+run >= 1 and right_hand_pos[0]+50+run <= 600:
			left_hand_pos[0] += run
			right_hand_pos[0] += run
			head_x += run
			stomach_x += run
			legs_x[0] += run
			legs_x[1] += run
		else: run = 0
		pos_apple_y += speed;
		canvas.fill(black, rect=[head_x, 370, 20, 20])
		pygame.draw.rect(canvas, red, [stomach_x, 390, 40, 40])
		canvas.fill(red, rect=left_hand_pos)
		canvas.fill(red, rect=right_hand_pos)
		pygame.draw.rect(canvas, black, [left_hand_pos[0]-10, 400, 10, 10])		#hands
		pygame.draw.rect(canvas, black, [right_hand_pos[0]+40, 400, 10, 10])
		canvas.fill(green, rect=[legs_x[0], 430, 10, 50])	#legs
		canvas.fill(green, rect=[legs_x[1], 430, 10, 50])
		canvas.fill(black, rect=[legs_x[0], 480, 10, 10])	#shoes
		canvas.fill(black, rect=[legs_x[1], 480, 10, 10])
		canvas.fill(red, rect=[0, 490, 600, 20])
		
		showScore("Score: "+str(score), (200, 100, 0), [500, 530])
		showScore("High Score: "+str(high_score), (200, 100, 0), [5, 530])
		
		if(((pos_apple_x+10) in range(head_x+1, head_x+20) and (pos_apple_y+10) in range(370+1, 390)) or (pos_apple_x+10 in range(stomach_x+1, stomach_x+50) and pos_apple_y+10 in range(390, 440)) or (pos_apple_x +10 in range(left_hand_pos[0]-1, right_hand_pos[0]+60) and pos_apple_y+10 in range(400, 420))):
			picked = True
			apple_presence = False
			score += 10
			pos_apple_y = 0
			if high_score < score:
				high_score = score
			if not (score % 100):
				speed = 1.5*speed
		elif(pos_apple_y+10 > 490):
			gameOver = True
			high_scoref = open("high_score", "w")
			high_scoref.write(str(high_score))
			high_scoref.close()
	else:
		show_msg("GAME OVER... Press any key to exit", [60, 300])
		show_msg("Score: %d" % score, [250, 230])
	pygame.display.update()
	
	clock.tick(20)
		
pygame.quit()
sys.exit()

