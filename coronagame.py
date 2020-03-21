from pygame.locals import *
import pygame, sys, random, time, os, math, _random, collections
from datetime import datetime

# global variables
left = False
right = False
up = False
down = False
walkcount = 0
enemieskilled = 0
level = 1
inprogress = False
viruses = []
spawns = 0
appearing = [False, False, False, False]
appeared = [False, False, False, False]
appearingcount = 0
dna=[False, False, False, False, False, False, False, False]
syringes=[]
entities = []
activedna=0
health=100
avaliabletargets=[]

def main():  # sets up the basics of the game window and such, gets the game moving
    global entities
    # create game window
    main_clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Coronavirus Cacophany")
    screen = pygame.display.set_mode((1280, 720))
    display = pygame.Surface((1280, 720))
    entities = create_entities(entities)
    start_game(main_clock, entities, screen, display)


def create_entities(entities):
    player = entity(0, 130, 34, 58, 5, 'player', True, True, True)
    entities.append(player)
    #dummy entity (used to be a virus, but I moved the virus function to later and don't want to change the indexes of everything else
    dummy = entity(0, 0, 0, 0, 0, 'dummy', False, False, False)
    entities.append(dummy)
    # dummy entity (used to be a syringe, but I moved the virus function to later and don't want to change the indexes of everything else
    dummy = entity(0, 0, 0, 0, 0, 'dummy', False, False, False)
    entities.append(dummy)
    car = entity(58, 0, 148, 127, 0, 'car', False, True, False)
    entities.append(car)
    fence = entity(0, 195, 1087, 11, 0, 'fence', False, True, False)
    entities.append(fence)
    house = entity(223, 0, 864, 123, 0, 'house', False, True, False)
    entities.append(house)
    right_bar = entity(1087, 0, 193, 720, 0, 'right_bar', False, True, False)
    entities.append(right_bar)
    china = entity(6, 606, 243, 126, 0, 'china', True, False, False)
    entities.append(china)
    iran = entity(315, 588, 212, 126, 0, 'iran', True, False, False)
    entities.append(iran)
    italy = entity(609, 588, 138, 129, 0, 'italy', True, False, False)
    entities.append(italy)
    USA = entity(798, 588, 261, 135, 0, 'usa', True, False, False)
    entities.append(USA)
    DNA_yellow = entity(1106, 280, 70, 70, 0, 'DNA_yellow', True, False, False)
    entities.append(DNA_yellow)
    DNA_white = entity(1194, 280, 70, 70, 0, 'DNA_white', True, False, False)
    entities.append(DNA_white)
    DNA_red = entity(1106, 370, 70, 70, 0, 'DNA_red', True, False, False)
    entities.append(DNA_red)
    DNA_purple = entity(1194, 370, 70, 70, 0, 'DNA_purple', True, False, False)
    entities.append(DNA_purple)
    DNA_pink = entity(1106, 460, 70, 70, 0, 'DNA_pink', True, False, False)
    entities.append(DNA_pink)
    DNA_orange = entity(1194, 460, 70, 70, 0, 'DNA_orange', True, False, False)
    entities.append(DNA_orange)
    DNA_green = entity(1106, 550, 70, 70, 0, 'DNA_green', True, False, False)
    entities.append(DNA_green)
    DNA_brown = entity(1194, 550, 70, 70, 0, 'DNA_brown', True, False, False)
    entities.append(DNA_brown)
    DNA_blue = entity(1106, 640, 70, 70, 0, 'DNA_blue', True, False, False)
    entities.append(DNA_blue)
    DNA_black = entity(1194, 640, 70, 70, 0, 'DNA_black', True, False, False)
    entities.append(DNA_black)
    health_bar_full=entity(1090,34,188,220,0,'health_bar_full',False,False,False)
    entities.append(health_bar_full)
    health_bar_empty = entity(1090, 34, 188, 220, 0, 'health_bar_empty', False, False, False)
    entities.append(health_bar_empty)
    return entities


def start_game(main_clock, entities, screen, display):
    global left, right, up, down, level, enemieskilled, inprogress, viruses, appearing, dna, syringes, activedna,avaliabletargets
    while True:
        # progesses the levels and unlocks new spawners+dna when all the enemies in a stage are cleared. also clears the virus array, which should already be empty
        if enemieskilled == 8 or enemieskilled == 21 or enemieskilled == 34 or enemieskilled == 47:
            level += 1
            #bumps up the kill progress by one so the method doesn't get tripped constantly:
            enemieskilled+=1
            viruses.clear()
            inprogress = False
        # adds the viruses for each level
        if level == 1 and inprogress == False:
            #reset the avaliable targets at the start of each level so viruses don't end up overlapping
            avaliabletargets=[0,66,132,198,264,330,396,462,528,594,660,726,792,858,924]
            appearing[0] = True
            dna[0]=True
            dna[1] = True
            virusadd(8, 'china')
            inprogress = True
        if level == 2 and inprogress == False:
            avaliabletargets = [0, 66, 132, 198, 264, 330, 396, 462, 528, 594, 660, 726, 792, 858, 924]
            appearing[1] = True
            dna[2]=True
            dna[3] = True
            virusadd(6, 'china')
            virusadd(6, 'iran')
            inprogress = True
        if level == 3 and inprogress == False:
            avaliabletargets = [0, 66, 132, 198, 264, 330, 396, 462, 528, 594, 660, 726, 792, 858, 924]
            appearing[2] = True
            dna[4]=True
            dna[5] = True
            virusadd(4, 'china')
            virusadd(4, 'iran')
            virusadd(4, 'italy')
            inprogress = True
        if level == 4 and inprogress == False:
            avaliabletargets = [0, 66, 132, 198, 264, 330, 396, 462, 528, 594, 660, 726, 792, 858, 924]
            appearing[3] = True
            dna[6]=True
            dna[7] = True
            virusadd(3, 'china')
            virusadd(3, 'iran')
            virusadd(3, 'italy')
            virusadd(3, 'usa')
            inprogress = True
        # shows end screen if level is 5
        if level == 5 and inprogress == False:
            end_screen=pygame.image.load('data/end_screen.png').convert()
            screen.blit(end_screen, (0, 0))
            inprogress = True
        #shows losing end screen:
        if health>(-1) and health<1:
            end_screen=pygame.image.load('data/losing_end_screen.png').convert()
            screen.blit(end_screen,(0,0))
            inprogress=True
        # check if the x button was clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP or event.type==pygame.MOUSEBUTTONUP:
                print(activedna)
                # check if virus activation keys were pressed and the DNA is unlocked
                if keys[pygame.K_1] and dna[0]==True or entities[11].get_hitbox().collidepoint(pygame.mouse.get_pos()) and dna[0]==True:
                    if entities[11].active==False and activedna+1<=4 or entities[11].active==True:
                        entities[11].active ^= True
                        if entities[11].active == True:
                            activedna += 1
                        else:
                            activedna -= 1
                if keys[pygame.K_2] and dna[1]==True or entities[12].get_hitbox().collidepoint(pygame.mouse.get_pos()) and dna[1]==True:
                    if entities[12].active == False and activedna + 1 <= 4 or entities[12].active == True:
                        entities[12].active ^= True
                        if entities[12].active == True:
                            activedna += 1
                        else:
                            activedna -= 1
                if keys[pygame.K_3] and dna[2]==True or entities[13].get_hitbox().collidepoint(pygame.mouse.get_pos()) and dna[2]==True:
                    if entities[13].active == False and activedna + 1 <= 4 or entities[13].active == True:
                        entities[13].active ^= True
                        if entities[13].active == True:
                            activedna += 1
                        else:
                            activedna -= 1
                if keys[pygame.K_4] and dna[3]==True or entities[14].get_hitbox().collidepoint(pygame.mouse.get_pos()) and dna[3]==True:
                    if entities[14].active == False and activedna + 1 <= 4 or entities[14].active == True:
                        entities[14].active ^= True
                        if entities[14].active == True:
                            activedna += 1
                        else:
                            activedna -= 1
                if keys[pygame.K_5] and dna[4]==True or entities[15].get_hitbox().collidepoint(pygame.mouse.get_pos()) and dna[4]==True:
                    if entities[15].active == False and activedna + 1 <= 4 or entities[15].active == True:
                        entities[15].active ^= True
                        if entities[15].active == True:
                            activedna += 1
                        else:
                            activedna -= 1
                if keys[pygame.K_6] and dna[5]==True or entities[16].get_hitbox().collidepoint(pygame.mouse.get_pos()) and dna[5]==True:
                    if entities[16].active == False and activedna + 1 <= 4 or entities[16].active == True:
                        entities[16].active ^= True
                        if entities[16].active == True:
                            activedna += 1
                        else:
                            activedna -= 1
                if keys[pygame.K_7] and dna[6]==True or entities[17].get_hitbox().collidepoint(pygame.mouse.get_pos()) and dna[6]==True:
                    if entities[17].active == False and activedna + 1 <= 4 or entities[17].active == True:
                        entities[17].active ^= True
                        if entities[17].active == True:
                            activedna += 1
                        else:
                            activedna -= 1
                if keys[pygame.K_8] and dna[7]==True or entities[18].get_hitbox().collidepoint(pygame.mouse.get_pos()) and dna[7]==True:
                    if entities[18].active == False and activedna + 1 <= 4 or entities[18].active == True:
                        entities[18].active ^= True
                        if entities[18].active == True:
                            activedna += 1
                        else:
                            activedna -= 1
                if keys[pygame.K_SPACE]:
                    for x in range(8):
                        entities[x+11].active=False
                        activedna=0
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0]<1087:
                syringes.append(entity(entities[0].x_pos,entities[0].y_pos,19,40,8,'syringe',False,True,True))
        keys = pygame.key.get_pressed()
        # makes every virus move
        for x in viruses:
            x.move(keys, entities)
        #make syringes move
        for x in syringes:
            x.move(keys, entities)
        # check if player movement keys were pressed
        if keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_d]:
            entities[0].move(keys, entities)
        # sets all movement directions to false if keys aren't pressed
        else:
            left = False
            right = False
            up = False
            down = False
        if level != 5 and health>0:  # make sure the game isn't over before redrawing all sprites
            redraw(entities, screen)
        main_clock.tick(60)
        pygame.display.update()


# creates virus entities in different amounts and on different spawners
def virusadd(num, spawn):
    global viruses
    if num == 8:
        if spawn == 'china':
            viruses.append(entity(0, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(0, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(67, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(67, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(134, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(134, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(201, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(201, 656, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'iran':
            viruses.append(entity(277, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(277, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(344, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(344, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(411, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(411, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(478, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(478, 656, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'italy':
            viruses.append(entity(548, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(548, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(615, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(615, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(682, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(682, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(749, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(749, 656, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'usa':
            viruses.append(entity(817, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(817, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(884, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(884, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(951, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(951, 656, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(1018, 591, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(1018, 656, 66, 64, 0, 'virus', True, False, True))
    if num == 3:
        if spawn == 'china':
            viruses.append(entity(49, 577, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(49, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(144, 577, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'iran':
            viruses.append(entity(346, 577, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(346, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(441, 577, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'italy':
            viruses.append(entity(599, 577, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(599, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(694, 577, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'usa':
            viruses.append(entity(867, 577, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(867, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(962, 577, 66, 64, 0, 'virus', True, False, True))
    if num == 6:
        if spawn == 'china':
            viruses.append(entity(29, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(29, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(97, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(97, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(165, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(165, 647, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'iran':
            viruses.append(entity(323, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(323, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(391, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(391, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(459, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(459, 647, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'italy':
            viruses.append(entity(574, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(574, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(642, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(642, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(710, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(710, 647, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'usa':
            viruses.append(entity(839, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(839, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(907, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(907, 647, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(975, 581, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(975, 647, 66, 64, 0, 'virus', True, False, True))
    if num == 4:
        if spawn == 'china':
            viruses.append(entity(68, 576, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(68, 648, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(142, 576, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(142, 648, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'iran':
            viruses.append(entity(350, 576, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(350, 648, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(424, 576, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(424, 648, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'italy':
            viruses.append(entity(618, 576, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(618, 648, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(692, 576, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(692, 648, 66, 64, 0, 'virus', True, False, True))
        if spawn == 'usa':
            viruses.append(entity(883, 576, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(883, 648, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(957, 576, 66, 64, 0, 'virus', True, False, True))
            viruses.append(entity(957, 648, 66, 64, 0, 'virus', True, False, True))


def redraw(entities, screen):
    global walkcount, viruses, spawns, appearing, appearingcount, appeared, syringes,health
    # draws all static entities
    screen.blit(pygame.image.load('data/background.png').convert(), (0, 0))
    screen.blit(entities[3].idle, (entities[3].x_pos, entities[3].y_pos))
    screen.blit(entities[4].idle, (entities[4].x_pos, entities[4].y_pos))
    screen.blit(entities[5].idle, (entities[5].x_pos, entities[5].y_pos))
    screen.blit(entities[6].idle, (entities[6].x_pos, entities[6].y_pos))
    # resets the player walking animation loop
    if walkcount + 1 >= 24:
        walkcount = 0
    # cycles through the various walking animations
    if left:
        screen.blit(entities[0].animations['left'][walkcount // 6], (entities[0].x_pos, entities[0].y_pos))
        walkcount += 1
    elif right:
        screen.blit(entities[0].animations['right'][walkcount // 6], (entities[0].x_pos, entities[0].y_pos))
        walkcount += 1
    elif up:
        screen.blit(entities[0].animations['forward'][walkcount // 6], (entities[0].x_pos, entities[0].y_pos))
        walkcount += 1
    elif down:
        screen.blit(entities[0].animations['back'][walkcount // 6], (entities[0].x_pos, entities[0].y_pos))
        walkcount += 1
    else:
        screen.blit(entities[0].idle, (entities[0].x_pos, entities[0].y_pos))

    # cycle the spawn point appearance animations ONCE
    for x in range(4):
        if appearing[x] == True:
            if appearingcount + 1 >= 24:
                appearingcount = 0
                appeared[x] = True
                appearing[x] = False
            else:
                screen.blit(entities[x + 7].animations['appearing'][appearingcount // 6],(entities[7 + x].x_pos, entities[7 + x].y_pos))
                appearingcount += 1
    for x in range(4):
        if appeared[x] == True:
            screen.blit(entities[7 + x].animations['appearing'][3], (entities[7 + x].x_pos, entities[7 + x].y_pos))
    #virus animations
    for x in viruses:
        if x.walkcount + 1 >= 24:
            x.walkcount = 0
        if x.attacking == False:
            # cycle the moving animation for viruses
            screen.blit(x.animations['moving'][x.walkcount // 12], (x.x_pos, x.y_pos))
            if x.colors[0]!='none':
                for y in range(len(x.colors)):
                    if y==0 and x.walkcount//12==0:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) +25, int(x.y_pos) +23),6)
                    if y==0 and x.walkcount//12==1:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) +27, int(x.y_pos) +24),6)
                    if y==1 and x.walkcount//12==0:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) +41, int(x.y_pos) +23),6)
                    if y==1 and x.walkcount//12==1:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) +39, int(x.y_pos) +24),6)
                    if y==2 and x.walkcount//12==0:
                       pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) +26, int(x.y_pos) +39),6)
                    if y==2 and x.walkcount//12==1:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) +27, int(x.y_pos) +38),6)
                    if y==3 and x.walkcount//12==0:
                        pygame.draw.circle(screen, x.colors[y],(int(x.x_pos)+41,int(x.y_pos)+39),6)
                    if y==3 and x.walkcount//12==1:
                        pygame.draw.circle(screen, x.colors[y],(int(x.x_pos)+39,int(x.y_pos)+38),6)
            x.walkcount += 1
        else:
            # cycles the attacking animation for viruses
            screen.blit(x.animations['attacking'][x.walkcount // 12], (x.x_pos, x.y_pos))
            if x.colors[0]!='none':
                for y in range(len(x.colors)):
                    if y == 0:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) + 25, int(x.y_pos) + 23), 6)
                    if y == 1:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) + 41, int(x.y_pos) + 23), 6)
                    if y == 2:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) + 26, int(x.y_pos) + 39), 6)
                    if y == 3:
                        pygame.draw.circle(screen, x.colors[y], (int(x.x_pos) + 41, int(x.y_pos) + 39), 6)
            x.walkcount += 1

    #display DNA marker
    for x in range(8):#change as more DNA is added
        if dna[x]==True:
            if entities[x+11].active==True:
                screen.blit(entities[x+11].animations['unlocking'][1],(entities[11+x].x_pos,entities[11+x].y_pos))
            else:
                screen.blit(entities[x + 11].animations['unlocking'][0], (entities[11 + x].x_pos, entities[11 + x].y_pos))

    #display syringes
    for x in syringes:
        screen.blit(x.idle, (x.x_pos, x.y_pos))
    #display health bars
    entities[21].idle.set_clip(pygame.Rect(0,entities[21].size_y-(entities[21].size_y*(health/100)), entities[21].size_x,entities[21].size_y*(health/100)))
    screen.blit(entities[22].idle, (entities[22].x_pos, entities[22].y_pos))
    screen.blit(entities[21].idle.subsurface(entities[21].idle.get_clip()),(entities[21].x_pos,entities[21].y_pos+(entities[21].size_y-(entities[21].size_y*(health/100)))))

class entity(object):
    global level, dna, entities, activedna, enemieskilled, syringes,avaliabletargets
    def __init__(self, x, y, size_x, size_y, velocity, type, animation, physics, movement):
        # sets all the entity attributes
        self.x_pos = x
        self.y_pos = y
        self.size_x = size_x
        self.size_y = size_y
        self.velocity = velocity
        self.hashitbox = physics
        idle = pygame.image.load('data/' + type + '/idle.png').convert()
        idle.set_colorkey((127, 0, 55))
        self.idle = idle
        # collects all the animations
        if animation == True:
            animation_timings = {}
            animation_database = {}
            for anim in os.listdir('data/' + type):
                if anim != 'idle.png':
                    f = open('data/' + type + '/' + anim + '/timing.txt', 'r')
                    t = f.read()
                    f.close()
                    timings = t.split(';')
                    n = 0
                    for val in timings:
                        timings[n] = int(val)
                        n += 1
                    animation_timings[anim] = timings.copy()
                    images = []
                    for i in range(len(timings)):
                        img = pygame.image.load(
                            'data/' + type + '/' + anim + '/' + anim + '_' + str(i + 1) + '.png').convert()
                        img.set_colorkey((127, 0, 55))
                        images.append(img.copy())
                    animation_database[anim] = images.copy()
            self.animations = animation_database
            self.animation_timings = animation_timings
        self.hitbox = [0, 0, self.size_x, self.size_y]
        # sets the movement type so the move function moves the entity in the correct way
        if movement == True:
            self.movement = type  # allows different movement for the three moving objects
        # sets virus specific attributes
        if type == 'virus':
            choice=random.choice(avaliabletargets)
            avaliabletargets.remove(choice)
            self.target = [choice, 205]
            self.walkcount = 0
            self.attacking = False
            self.velocity = 1
            self.colors=[]
            randomcolor=random.randrange(1,level*2+1)
            unlockedcolors = []
            if dna[0] == True:
                unlockedcolors.append((255, 255, 17))
            if dna[1] == True:
                unlockedcolors.append((255, 255, 255))
            if dna[2] == True:
                unlockedcolors.append((244, 0, 0))
            if dna[3] == True:
                unlockedcolors.append((99, 42, 159))
            if dna[4] == True:
                unlockedcolors.append((255, 0, 254))
            if dna[5] == True:
                unlockedcolors.append((255, 100, 0))
            if dna[6] == True:
                unlockedcolors.append((0, 255, 1))
            if dna[7] == True:
                unlockedcolors.append((101, 39, 0))
            #makes sure the number of colors on a virus isn't 0 but also isn't more than 4 and also doesn't exceed the number of unlocked colors
            if randomcolor>4:
                for x in range(4):
                    choice = random.choice(unlockedcolors)
                    self.colors.append(choice)
                    unlockedcolors.remove(choice)
            else:
                for x in range(randomcolor):
                    choice = random.choice(unlockedcolors)
                    self.colors.append(choice)
                    unlockedcolors.remove(choice)
        if type[:3]=='DNA':
            self.active=False
        if type=='syringe':
            #set target
            self.target=[]
            self.target=pygame.mouse.get_pos()
            # set colors
            self.colors = []
            if entities[11].active and activedna <= 4:
                self.colors.append((255, 255, 17))
            if entities[12].active and activedna <= 4:
                self.colors.append((255, 255, 255))
            if entities[13].active and activedna <= 4:
                self.colors.append((244, 0, 0))
            if entities[14].active and activedna <= 4:
                self.colors.append((99, 42, 159))
            if entities[15].active and activedna <= 4:
                self.colors.append((255, 0, 254))
            if entities[16].active and activedna <= 4:
                self.colors.append((255, 100, 0))
            if entities[17].active and activedna <= 4:
                self.colors.append((0, 255, 1))
            if entities[18].active and activedna <= 4:
                self.colors.append((101, 39, 0))
            #add colors to syringe
            for y in range(len(self.colors)):
                rectangle = pygame.image.load('data/syringeslot.png').convert()
                rectangle.fill(self.colors[y])
                if y == 0:
                    self.idle.blit(rectangle, (5, 12))
                if y == 1:
                    self.idle.blit(rectangle, (5, 17))
                if y == 2:
                    self.idle.blit(rectangle, (5, 22))
                if y == 3:
                    self.idle.blit(rectangle, (5, 27))
            #set angle
            b=self.target[0]-self.x_pos
            c=self.target[1]-self.y_pos
            if b>0:
                self.angle=180+(90-math.degrees(math.atan(c/b)))
            if b<0:
                self.angle=90+abs(math.degrees(math.atan(c/b)))
            if b==0:
                self.angle=180
            self.idle=pygame.transform.rotate(self.idle,self.angle)


    def get_hitbox(self):
        # returns the hitbox rectangle
        return pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos + self.hitbox[1], self.hitbox[2], self.hitbox[3])

    def move(self, keys, entities):
        global left, right, up, down, viruses, syringes, enemieskilled, health
        if self.movement == ('player'):
            # check for collision and then, if no collision is found, move the player. ADD THE SIDE BAR AS A COLLISION OBJECT
            if keys[pygame.K_w] and (self.y_pos - self.velocity) >= 0 and (
                    self.y_pos + self.size_y - self.velocity) <= 720:
                carcolliding = pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos - self.velocity + self.hitbox[1],
                                           self.hitbox[2], self.hitbox[3]).colliderect(entities[3].get_hitbox())
                housecolliding = pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos - self.velocity + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[5].get_hitbox())
                fencecolliding = pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos - self.velocity + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[4].get_hitbox())
                rightcolliding= pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos - self.velocity + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[6].get_hitbox())
                if carcolliding == False and housecolliding == False and fencecolliding == False and rightcolliding==False:
                    self.y_pos -= self.velocity
                    down = True
                    up = False
                    right = False
                    left = False
            if keys[pygame.K_s] and (self.y_pos + self.velocity) >= 0 and (
                    self.y_pos + self.size_y + self.velocity) <= 720:
                carcolliding = pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos + self.velocity + self.hitbox[1],
                                           self.hitbox[2], self.hitbox[3]).colliderect(entities[3].get_hitbox())
                housecolliding = pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos + self.velocity + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[5].get_hitbox())
                fencecolliding = pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos + self.velocity + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[4].get_hitbox())
                rightcolliding = pygame.Rect(self.x_pos + self.hitbox[0], self.y_pos + self.velocity + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[6].get_hitbox())
                if carcolliding == False and housecolliding == False and fencecolliding == False and rightcolliding==False:
                    self.y_pos += self.velocity
                    up = True
                    down = False
                    right = False
                    left = False
            if keys[pygame.K_a] and (self.x_pos - self.velocity) >= 0 and (
                    self.x_pos + self.size_x - self.velocity) <= 1280:
                carcolliding = pygame.Rect(self.x_pos - self.velocity + self.hitbox[0], self.y_pos + self.hitbox[1],
                                           self.hitbox[2], self.hitbox[3]).colliderect(entities[3].get_hitbox())
                housecolliding = pygame.Rect(self.x_pos - self.velocity + self.hitbox[0], self.y_pos + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[5].get_hitbox())
                fencecolliding = pygame.Rect(self.x_pos - self.velocity + self.hitbox[0], self.y_pos + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[4].get_hitbox())
                rightcolliding = pygame.Rect(self.x_pos - self.velocity + self.hitbox[0], self.y_pos + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[6].get_hitbox())
                if carcolliding == False and housecolliding == False and fencecolliding == False and rightcolliding==False:
                    self.x_pos -= self.velocity
                    left = True
                    right = False
                    up = False
                    down = False
            if keys[pygame.K_d] and (self.x_pos + self.velocity) >= 0 and (
                    self.x_pos + self.size_x + self.velocity) <= 1280:
                carcolliding = pygame.Rect(self.x_pos + self.velocity + self.hitbox[0], self.y_pos + self.hitbox[1],
                                           self.hitbox[2], self.hitbox[3]).colliderect(entities[3].get_hitbox())
                housecolliding = pygame.Rect(self.x_pos + self.velocity + self.hitbox[0], self.y_pos + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[5].get_hitbox())
                fencecolliding = pygame.Rect(self.x_pos + self.velocity + self.hitbox[0], self.y_pos + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[4].get_hitbox())
                rightcolliding = pygame.Rect(self.x_pos + self.velocity + self.hitbox[0], self.y_pos + self.hitbox[1],
                                             self.hitbox[2], self.hitbox[3]).colliderect(entities[6].get_hitbox())
                if carcolliding == False and housecolliding == False and fencecolliding == False and rightcolliding==False:
                    self.x_pos += self.velocity
                    left = False
                    right = True
                    up = False
                    down = False
            # operates on mouse and keyboard
        if self.movement == ('virus'):
            # if colliding with fence, set attack to true
            if self.get_hitbox().colliderect(entities[4].get_hitbox()) or self.get_hitbox().colliderect(entities[6].get_hitbox()):
                self.attacking = True
                health-=0.01
            else:
                # gets the x and y distance to the target. a is in absolute value i case the virus spawns to the right of its target
                a = self.target[0] - self.x_pos
                b = self.y_pos - self.target[1]
                # gets the angle to the target
                angle = math.atan(a/b)
                # moves the entity according to a proportional triangle with a hypotenuse the same length as the velocity
                collision=False
                self.x_pos += self.velocity * math.sin(angle)
                self.y_pos -= self.velocity * math.cos(angle)
            # moves towards mouse and disappears upon colliding with the right virus
        if self.movement == ('syringe'):
            a = self.target[0] - self.x_pos
            b = self.target[1]-self.y_pos
            angle = math.atan(a / b)
            # moves the entity according to a proportional triangle with a hypotenuse the same length as the velocity
            if not pygame.Rect(self.x_pos+(self.velocity * math.sin(angle)) + self.hitbox[0], self.y_pos+(self.velocity * math.cos(angle)) + self.hitbox[1], self.hitbox[2], self.hitbox[3]).colliderect(entities[6].get_hitbox()):
                self.x_pos += self.velocity * math.sin(angle)
                self.y_pos += self.velocity * math.cos(angle)
            else:
                syringes.remove(self)
            for x in viruses:
                if self.get_hitbox().colliderect(x.get_hitbox()) and collections.Counter(x.colors)==collections.Counter(self.colors):
                    viruses.remove(x)
                    enemieskilled+=1



main()
