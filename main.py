# To see the original level 3, turn to the original program (The Maze Game Project Original)
#importing pygame module
import pygame
import time
from pygame.locals import *
# initiate pygame and give permission
# to use pygame's functionality
pygame.init()
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("MAZE GAME")
#make screen white with bg red,green,blue at (255)
bgred = 250
bggreen = 100
bgblue = 20
window.fill((bgred, bggreen, bgblue))
pygame.display.update()
#create a circle
x = 550
y = 150
#choose a color
red = 30
green = 100
blue = 50
radius = 5
thickness = 100

pygame.draw.circle(window, (red, green, blue), [x, y], radius, thickness)
pygame.display.update()
red_r = 50
green_r = 40
blue_r = 100
red = 100
#Level 1
# SIDE 1 (ALL LEVELS)(LEVEL ONE)
srx1 = 0
sry1 = 0
length = 600
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(srx1, sry1, length, width))
pygame.display.update()
# SIDE 2 (ALL LEVELS)(LEVEL ONE)
srx2 = 0
sry2 = 288
length = 600
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(srx2, sry2, length, width))
pygame.display.update()
# RECT 1 (LEVEL ONE)
rx1 = 50
ry1 = 30
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx1, ry1, length, width))
pygame.display.update()
# RECT 2 (LEVEL ONE)
rx2 = 50
ry2 = 228
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx2, ry2, length, width))
pygame.display.update()
# RECT 3 (LEVEL ONE)
rx3 = 20
ry3 = 70
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx3, ry3, length, width))
pygame.display.update()
# RECT 4 (LEVEL ONE)
rx4 = 20
ry4 = 188
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx4, ry4, length, width))
pygame.display.update()
# RECT 5 (LEVEL ONE)
rx5 = 80
ry5 = 70
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx5, ry5, length, width))
pygame.display.update()
# RECT 6 (LEVEL ONE)
rx6 = 80
ry6 = 188
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx6, ry6, length, width))
pygame.display.update()
# RECT 7 (LEVEL ONE)
rx7 = 120
ry7 = 70
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx7, ry7, length, width))
pygame.display.update()
# RECT 8 (LEVEL ONE)
rx8 = 150
ry8 = 80
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx8, ry8, length, width))
pygame.display.update()
# RECT 9 (LEVEL ONE)
rx9 = 180
ry9 = 100
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx9, ry9, length, width))
pygame.display.update()
# RECT 10 (LEVEL ONE)
rx10 = 240
ry10 = 100
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx10, ry10, length, width))
pygame.display.update()
# RECT 11 (LEVEL ONE)
rx11 = 310
ry11 = 100
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx11, ry11, length, width))
pygame.display.update()
# RECT 12 (LEVEL ONE)
rx12 = 115
ry12 = 188
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx12, ry12, length, width))
pygame.display.update()
# RECT 13 (LEVEL ONE)
rx13 = 170
ry13 = 188
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx13, ry13, length, width))
pygame.display.update()
# RECT 14 (LEVEL ONE)
rx14 = 200
ry14 = 218
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx14, ry14, length, width))
pygame.display.update()
# RECT 15 (LEVEL ONE)
rx15 = 260
ry15 = 218
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx15, ry15, length, width))
pygame.display.update()
# RECT 16 (LEVEL ONE)
rx16 = 300
ry16 = 218
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx16, ry16, length, width))
pygame.display.update()
# RECT 17 (LEVEL ONE)
rx17 = 350
ry17 = 100
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx17, ry17, length, width))
pygame.display.update()
# RECT 18 (LEVEL ONE)
rx18 = 370
ry18 = 190
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx18, ry18, length, width))
pygame.display.update()
#we are going to loop the update command
dx = 1
dy = 5
print("WELCOME TO THE MAZE GAME (BY PEDRO CRUZ-AVALOS)")
print("THIS IS A SIMPLE MAZE GAME, GO TO THE LEFT SIDE OF THE SCREEN TO WIN")
name = input("WHAT IS YOUR NAME CHALLENGER: ")
print("WELCOME TO YOUR CHALLENGE", (name))
start1 = input("TO BEGIN PRESS THE ENTER KEY: ")
print("\n")
print("YOU MIGHT HAVE TO CHANGE THE SCREEN SIZE.....")
print("CONTROLS (ARROW KEYS FOR MOVEMENT)")
print("\n")
print("TIP: THERE ARE TWO POSSIBLE WAYS TO GO.......")
print("BEGIN LEVEL ONE...CLICK ON GAME SCREEN TO START MOVING...")
while (1 == 1):
    #slow this loop down
    time.sleep(0.01)
    #here we will make our ball do stuff
    pygame.draw.circle(window, (bgred, bggreen, bgblue), [x, y], radius,
                       thickness)
    pygame.display.update()
    eve = pygame.event.get()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        x = x - 1
        print("acknowledged_1_LEFT")
    if key_input[pygame.K_RIGHT]:
        x = x + 1
        print("acknowledged_2_RIGHT")
    if key_input[pygame.K_UP]:
        y = y - 1
        print("acknowledged_3_UP")
    if key_input[pygame.K_DOWN]:
        y = y + 1
        print("acknowledged_4_DOWN")
    pygame.draw.circle(window, (red, green, blue), [x, y], radius, thickness)
    pygame.display.update()
    # SIDE 1 LOSE (ALL LEVELS)(LEVEL ONE)
    if (y < 36):
        print("ENCOUNTERED TOP WALL")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # SIDE 2 LOSE (ALL LEVELS)(LEVEL ONE)
    if (y > 283):
        print("ENCOUNTERED LOWER WALL")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
            break
    # RECT 1 LOSE (LEVEL ONE)
    if (45 < x < 85 and 25 < y < 95):
        print("ENCOUNTERED RECTANGLE 1")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
            break
    # RECT 2 LOSE (LEVEL ONE)
    if (45 < x < 85 and 223 < y < 293):
        print("ENCOUNTERED RECTANGLE 2")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 3 LOSE (LEVEL ONE)
    if (15 < x < 55 and 65 < y < 135):
        print("ENCOUNTERED RECTANGLE 3")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 4 LOSE (LEVEL ONE)
    if (15 < x < 55 and 183 < y < 253):
        print("ENCOUNTERED RECTANGLE 4")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 5 LOSE (LEVEL ONE)
    if (75 < x < 115 and 65 < y < 135):
        print("ENCOUNTERED RECTANGLE 5")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 6 LOSE (LEVEL ONE)
    if (75 < x < 115 and 183 < y < 253):
        print("ENCOUNTERED RECTANGLE 6")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 7 LOSE (LEVEL ONE)
    if (115 < x < 185 and 65 < y < 105):
        print("ENCOUNTERED RECTANGLE 7")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 8 LOSE (LEVEL ONE)
    if (145 < x < 185 and 75 < y < 145):
        print("ENCOUNTERED RECTANGLE 8")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 9 LOSE (LEVEL ONE)
    if (175 < x < 245 and 95 < y < 135):
        print("ENCOUNTERED RECTANGLE 9")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 10 LOSE (LEVEL ONE)
    if (235 < x < 275 and 95 < y < 165):
        print("ENCOUNTERED RECTANGLE 10")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 11 LOSE (LEVEL ONE)
    if (305 < x < 345 and 95 < y < 165):
        print("ENCOUNTERED RECTANGLE 11")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 12 LOSE (LEVEL ONE)
    if (110 < x < 180 and 183 < y < 253):
        print("ENCOUNTERED RECTANGLE 12")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 13 LOSE (LEVEL ONE)
    if (165 < x < 205 and 183 < y < 253):
        print("ENCOUNTERED RECTANGLE 13")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 14 LOSE (LEVEL ONE)
    if (195 < x < 265 and 213 < y < 253):
        print("ENCOUNTERED RECTANGLE 14")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 15 LOSE (LEVEL ONE)
    if (255 < x < 295 and 213 < y < 283):
        print("ENCOUNTERED RECTANGLE 15")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 16 LOSE (LEVEL ONE)
    if (295 < x < 365 and 213 < y < 253):
        print("ENCOUNTERED RECTANGLE 16")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 17 LOSE (LEVEL ONE)
    if (345 < x < 415 and 95 < y < 135):
        print("ENCOUNTERED RECTANGLE 17")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 18 LOSE (LEVEL ONE)
    if (365 < x < 405 and 185 < y < 255):
        print("ENCOUNTERED RECTANGLE 18")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    #PLAYER WINS (LEVEL ONE)
    if (x < 15):
        print("PLAYER WINS!!! LEVEL ONE")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("WINNER WINNER CHICKEN DINNER", red1, green1, blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(green1)
            window.blit(text, textRect)
            pygame.display.update()
            break
        break
print("CONRAGULATIONS CHALENGER:", (name))
print("FOR COMPLETING LEVEL ONE OF THE MAZE GAME")
#Level 2
window.fill((bgred, bggreen, bgblue))
pygame.display.update()
nx = 550
ny = 150
pygame.draw.circle(window, (red, green, blue), [nx, ny], radius, thickness)
pygame.display.update()
# SIDE 1 (ALL LEVELS)(LEVEL TWO)
srx1 = 0
sry1 = 0
length = 600
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(srx1, sry1, length, width))
pygame.display.update()
# SIDE 2 (ALL LEVELS)(LEVEL TWO)
srx2 = 0
sry2 = 288
length = 600
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(srx2, sry2, length, width))
pygame.display.update()
# RECT 1 (LEVEL TWO)
rx1 = 0
ry1 = 30
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx1, ry1, length, width))
pygame.display.update()
# RECT 2 (LEVEL TWO)
rx2 = 0
ry2 = 228
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx2, ry2, length, width))
pygame.display.update()
# RECT 3 (LEVEL TWO)
rx3 = 20
ry3 = 70
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx3, ry3, length, width))
pygame.display.update()
# RECT 4 (LEVEL TWO)
rx4 = 20
ry4 = 188
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx4, ry4, length, width))
pygame.display.update()
# RECT 5 (LEVEL TWO)
rx5 = 100
ry5 = 90
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx5, ry5, length, width))
pygame.display.update()
# RECT 6 (LEVEL TWO)
rx6 = 100
ry6 = 168
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx6, ry6, length, width))
pygame.display.update()
# RECT 7 (LEVEL TWO)
rx7 = 150
ry7 = 90
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx7, ry7, length, width))
pygame.display.update()
# RECT 8 (LEVEL TWO)
rx8 = 150
ry8 = 168
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx8, ry8, length, width))
pygame.display.update()
# RECT 9 (LEVEL TWO)
rx9 = 240
ry9 = 100
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx9, ry9, length, width))
pygame.display.update()
# RECT 10 (LEVEL TWO)
rx10 = 240
ry10 = 100
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx10, ry10, length, width))
pygame.display.update()
# RECT 11 (LEVEL TWO)
rx11 = 310
ry11 = 30
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx11, ry11, length, width))
pygame.display.update()
# RECT 12 (LEVEL TWO)
rx12 = 310
ry12 = 168
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx12, ry12, length, width))
pygame.display.update()
# RECT 13 (LEVEL TWO)
rx13 = 400
ry13 = 100
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx13, ry13, length, width))
pygame.display.update()
# RECT 14 (LEVEL TWO)
rx14 = 400
ry14 = 158
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx14, ry14, length, width))
pygame.display.update()
# RECT 15 (LEVEL TWO)
rx15 = 260
ry15 = 218
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx15, ry15, length, width))
pygame.display.update()
# RECT 16 (LEVEL TWO)
rx16 = 260
ry16 = 218
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx16, ry16, length, width))
pygame.display.update()
# RECT 17 (LEVEL TWO)
rx17 = 350
ry17 = 160
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx17, ry17, length, width))
pygame.display.update()
# RECT 18 (LEVEL TWO)
rx18 = 370
ry18 = 190
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx18, ry18, length, width))
pygame.display.update()
start2 = input("ARE YOU READY TO START LEVEL 2 (PRESS THE ENTER KEY): ")
print("CONTROLS (ARROW KEYS FOR MOVEMENT)")
print("NO TIPS THIS TIME")
print("BEGIN LEVEL 2")
while (1 == 1):
    #slow this loop down
    time.sleep(0.01)
    #here we will make our ball do stuff
    pygame.draw.circle(window, (bgred, bggreen, bgblue), [nx, ny], radius,
                       thickness)
    pygame.display.update()
    eve = pygame.event.get()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        nx = nx - 1
        print("acknowledged_1_LEFT")
    if key_input[pygame.K_RIGHT]:
        nx = nx + 1
        print("acknowledged_2_RIGHT")
    if key_input[pygame.K_UP]:
        ny = ny - 1
        print("acknowledged_3_UP")
    if key_input[pygame.K_DOWN]:
        ny = ny + 1
        print("acknowledged_4_DOWN")
    pygame.draw.circle(window, (red, green, blue), [nx, ny], radius, thickness)
    pygame.display.update()
    # SIDE 1 LOSE (ALL LEVELS)(LEVEL TWO)
    if (ny < 36):
        print("ENCOUNTERED TOP WALL")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # SIDE 2 LOSE (ALL LEVELS)(LEVEL TWO)
    if (ny > 283):
        print("ENCOUNTERED LOWER WALL")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
            break
    # RECT 1 LOSE (LEVEL TWO)
    if (-5 < nx < 35 and 25 < ny < 95):
        print("ENCOUNTERED RECTANGLE 1")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
            break
    # RECT 2 LOSE (LEVEL TWO)
    if (-5 < nx < 35 and 223 < ny < 293):
        print("ENCOUNTERED RECTANGLE 2")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 3 LOSE (LEVEL TWO)
    if (15 < nx < 55 and 65 < ny < 135):
        print("ENCOUNTERED RECTANGLE 3")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 4 LOSE (LEVEL TWO)
    if (15 < nx < 55 and 183 < ny < 253):
        print("ENCOUNTERED RECTANGLE 4")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 5 LOSE (LEVEL TWO)
    if (95 < nx < 135 and 85 < ny < 155):
        print("ENCOUNTERED RECTANGLE 5")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 6 LOSE (LEVEL TWO)
    if (95 < nx < 135 and 163 < ny < 233):
        print("ENCOUNTERED RECTANGLE 6")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 7 LOSE (LEVEL TWO)
    if (145 < nx < 185 and 85 < ny < 155):
        print("ENCOUNTERED RECTANGLE 7")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 8 LOSE (LEVEL TWO)
    if (145 < nx < 185 and 163 < ny < 233):
        print("ENCOUNTERED RECTANGLE 8")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 9 LOSE (LEVEL TWO)
    if (235 < nx < 305 and 95 < ny < 135):
        print("ENCOUNTERED RECTANGLE 9")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 10 LOSE (LEVEL TWO)
    if (235 < nx < 275 and 95 < ny < 165):
        print("ENCOUNTERED RECTANGLE 10")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 11 LOSE (LEVEL TWO)
    if (305 < nx < 345 and 25 < ny < 95):
        print("ENCOUNTERED RECTANGLE 11")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 12 LOSE (LEVEL TWO)
    if (305 < nx < 345 and 163 < ny < 233):
        print("ENCOUNTERED RECTANGLE 12")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 13 LOSE (LEVEL TWO)
    if (395 < nx < 435 and 95 < ny < 165):
        print("ENCOUNTERED RECTANGLE 13")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 14 LOSE (LEVEL TWO)
    if (395 < nx < 435 and 153 < ny < 223):
        print("ENCOUNTERED RECTANGLE 14")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 15 LOSE (LEVEL TWO)
    if (255 < nx < 295 and 213 < ny < 273):
        print("ENCOUNTERED RECTANGLE 15")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 16 LOSE (LEVEL TWO)
    if (255 < nx < 325 and 213 < ny < 253):
        print("ENCOUNTERED RECTANGLE 16")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 17 LOSE (LEVEL TWO)
    if (345 < nx < 415 and 155 < ny < 195):
        print("ENCOUNTERED RECTANGLE 17")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 18 LOSE (LEVEL TWO)
    if (365 < nx < 405 and 185 < ny < 255):
        print("ENCOUNTERED RECTANGLE 18")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    #PLAYER WINS (LEVEL TWO)
    if (nx < 15):
        print("PLAYER WINS!!! LEVEL TWO")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("WINNER WINNER CHICKEN DINNER", red1, green1, blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(green1)
            window.blit(text, textRect)
            pygame.display.update()
            break
        break
print("CONRAGULATIONS CHALENGER:", (name))
print("FOR COMPLETING LEVEL TWO OF THE MAZE GAME")
# LEVEL 3 (NEW LEVEL THREE)
window.fill((bgred, bggreen, bgblue))
pygame.display.update()
px = 550
py = 150
pygame.draw.circle(window, (red, green, blue), [px, py], radius, thickness)
pygame.display.update()
# SIDE 1 (ALL LEVELS)(NEW LEVEL THREE)
srx1 = 0
sry1 = 0
length = 600
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(srx1, sry1, length, width))
pygame.display.update()
# SIDE 2 (ALL LEVELS)(NEW LEVEL THREE)
srx2 = 0
sry2 = 288
length = 600
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(srx2, sry2, length, width))
pygame.display.update()
# RECT 1 (NEW LEVEL THREE)
rx1 = 30
ry1 = 30
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx1, ry1, length, width))
pygame.display.update()
# RECT 2 (NEW LEVEL THREE)
rx2 = 60
ry2 = 52
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx2, ry2, length, width))
pygame.display.update()
# RECT 3 (NEW LEVEL THREE)
rx3 = 90
ry3 = 74
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx3, ry3, length, width))
pygame.display.update()
# RECT 4 (NEW LEVEL THREE)
rx4 = 120
ry4 = 96
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx4, ry4, length, width))
pygame.display.update()
# RECT 5 (NEW LEVEL THREE)
rx5 = 150
ry5 = 118
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx5, ry5, length, width))
pygame.display.update()
# RECT 6 (NEW LEVEL THREE)
rx6 = 30
ry6 = 168
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx6, ry6, length, width))
pygame.display.update()
# RECT 7 (NEW LEVEL THREE)
rx7 = 60
ry7 = 190
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx7, ry7, length, width))
pygame.display.update()
# RECT 8 (NEW LEVEL THREE)
rx8 = 90
ry8 = 212
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx8, ry8, length, width))
pygame.display.update()
# RECT 9 (NEW LEVEL THREE)
rx9 = 120
ry9 = 234
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx9, ry9, length, width))
pygame.display.update()
# RECT 10 (NEW LEVEL THREE)
rx10 = 150
ry10 = 256
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx10, ry10, length, width))
pygame.display.update()
# RECT 11 (NEW LEVEL THREE)
rx11 = 230
ry11 = 30
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx11, ry11, length, width))
pygame.display.update()
# RECT 12 (NEW LEVEL THREE)
rx12 = 230
ry12 = 115
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx12, ry12, length, width))
pygame.display.update()
# RECT 13 (NEW LEVEL THREE)
rx13 = 230
ry13 = 175
length = 30
width = 60
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx13, ry13, length, width))
pygame.display.update()
# RECT 14 (NEW LEVEL THREE)
rx14 = 230
ry14 = 260
length = 30
width = 50
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx14, ry14, length, width))
pygame.display.update()
# RECT 15 (NEW LEVEL THREE)
rx15 = 295
ry15 = 50
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx15, ry15, length, width))
pygame.display.update()
# RECT 16 (NEW LEVEL THREE)
rx16 = 295
ry16 = 110
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx16, ry16, length, width))
pygame.display.update()
# RECT 17 (NEW LEVEL THREE)
rx17 = 295
ry17 = 170
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx17, ry17, length, width))
pygame.display.update()
# RECT 18 (NEW LEVEL THREE)
rx18 = 295
ry18 = 230
length = 60
width = 30
pygame.draw.rect(window, (red_r, green_r, blue_r),
                 pygame.Rect(rx18, ry18, length, width))
pygame.display.update()
start4 = input("ARE YOU READY TO START LEVEL 3 (PRESS THE ENTER KEY): ")
print("CONTROLS (ARROW KEYS FOR MOVEMENT)")
print("NO TIPS THIS TIME")
print("BEGIN LEVEL 3")
while (1 == 1):
    #slow this loop down
    time.sleep(0.01)
    #here we will make our ball do stuff
    pygame.draw.circle(window, (bgred, bggreen, bgblue), [px, py], radius,
                       thickness)
    pygame.display.update()
    eve = pygame.event.get()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        px = px - 1
        print("acknowledged_1_LEFT")
    if key_input[pygame.K_RIGHT]:
        px = px + 1
        print("acknowledged_2_RIGHT")
    if key_input[pygame.K_UP]:
        py = py - 1
        print("acknowledged_3_UP")
    if key_input[pygame.K_DOWN]:
        py = py + 1
        print("acknowledged_4_DOWN")
    pygame.draw.circle(window, (red, green, blue), [px, py], radius, thickness)
    pygame.display.update()
    # SIDE 1 LOSE (ALL LEVELS)(NEW LEVEL THREE)
    if (px < 36):
        print("ENCOUNTERED TOP WALL")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # SIDE 2 LOSE (ALL LEVELS)(NEW LEVEL THREE)
    if (py > 283):
        print("ENCOUNTERED LOWER WALL")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 1 LOSE (NEW LEVEL THREE)
    if (25 < px < 65 and 25 < py < 95):
        print("ENCOUNTERED RECTANGLE 1")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 2 LOSE (NEW LEVEL THREE)
    if (55 < px < 95 and 47 < py < 117):
        print("ENCOUNTERED RECTANGLE 2")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 3 LOSE (NEW LEVEL THREE)
    if (85 < px < 125 and 69 < py < 139):
        print("ENCOUNTERED RECTANGLE 3")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 4 LOSE (NEW LEVEL THREE)
    if (115 < px < 155 and 91 < py < 161):
        print("ENCOUNTERED RECTANGLE 4")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 5 LOSE (NEW LEVEL THREE)
    if (145 < px < 185 and 113 < py < 183):
        print("ENCOUNTERED RECTANGLE 5")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 6 LOSE (NEW LEVEL THREE)
    if (25 < px < 65 and 163 < py < 233):
        print("ENCOUNTERED RECTANGLE 6")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 7 LOSE (NEW LEVEL THREE)
    if (55 < px < 95 and 185 < py < 255):
        print("ENCOUNTERED RECTANGLE 7")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 8 LOSE (NEW LEVEL THREE)
    if (85 < px < 125 and 207 < py < 277):
        print("ENCOUNTERED RECTANGLE 8")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 9 LOSE (NEW LEVEL THREE)
    if (115 < px < 155 and 229 < py < 299):
        print("ENCOUNTERED RECTANGLE 9")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 10 LOSE (NEW LEVEL THREE)
    if (145 < px < 185 and 251 < py < 321):
        print("ENCOUNTERED RECTANGLE 10")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 11 LOSE (NEW LEVEL THREE)
    if (225 < px < 265 and 25 < py < 95):
        print("ENCOUNTERED RECTANGLE 11")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 12 LOSE (NEW LEVEL THREE)
    if (225 < px < 265 and 110 < py < 180):
        print("ENCOUNTERED RECTANGLE 12")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 13 LOSE (NEW LEVEL THREE)
    if (225 < px < 265 and 170 < py < 240):
        print("ENCOUNTERED RECTANGLE 13")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 14 LOSE (NEW LEVEL THREE)
    if (225 < px < 265 and 255 < py < 315):
        print("ENCOUNTERED RECTANGLE 14")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 15 LOSE (NEW LEVEL THREE)
    if (290 < px < 360 and 45 < py < 85):
        print("ENCOUNTERED RECTANGLE 15")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 16 LOSE (NEW LEVEL THREE)
    if (290 < px < 360 and 105 < py < 145):
        print("ENCOUNTERED RECTANGLE 16")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 17 LOSE (NEW LEVEL THREE)
    if (290 < px < 360 and 165 < py < 205):
        print("ENCOUNTERED RECTANGLE 17")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    # RECT 18 LOSE (NEW LEVEL THREE)
    if (290 < px < 360 and 225 < py < 265):
        print("ENCOUNTERED RECTANGLE 18")
        print("GAME OVER!!!")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("LOSER LOSER NO CHICKEN DINNER", red1, green1,
                           blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(red1)
            window.blit(text, textRect)
            pygame.display.update()
        break
    #PLAYER WINS (NEW LEVEL THREE)
    if (px < 15):
        print("PLAYER WINS!!! LEVEL THREE")
        white = (255, 255, 255)
        red1 = (255, 0, 0)
        green1 = (0, 255, 0)
        blue1 = (0, 0, 218)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("WINNER WINNER CHICKEN DINNER", red1, green1, blue1)
        textRect = text.get_rect()
        textRect.center = (300, 100)
        while (2 == 2):
            window.fill(green1)
            window.blit(text, textRect)
            pygame.display.update()
            break
        break
print("CONRAGULATIONS CHALENGER:", (name))
print("FOR COMPLETING LEVEL THREE OF THE MAZE GAME")