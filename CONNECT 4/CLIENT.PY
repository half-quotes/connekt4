import sys
import time
import pygame
from pygame.locals import*
pygame.init()
FPS=32
SCREENWIDTH = 900
SCREENHEIGHT = 600
grid = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2]]
GAME_SPRITES = {}
GAME_SOUND = {}


SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
SCREEN.fill((245,222,179))
GAME_SPRITES['kack_g']=pygame.image.load('sprite\kack_g.png').convert_alpha()
GAME_SPRITES['kack_g'] = pygame.transform.scale(GAME_SPRITES['kack_g'], (900, 600))
SCREEN.blit(GAME_SPRITES['kack_g'], (0, 0))
pygame.display.update()
font = pygame.font.Font(None, 32)
nomatch=0
no_match = ''
input_rect = pygame.Rect(422,300+50,50,30)
color_active = pygame.Color('grey21')
color_de = pygame.Color('grey69')
color = [color_de, color_active]

rectA = pygame.Rect(70,80,530,440)

rect0 = pygame.Rect(70, 80, 75.714, 440)
rect1 = pygame.Rect(70+(1*75.714), 80, 75.714, 440)
rect2 = pygame.Rect(70+(2*75.714), 80, 75.714, 440)
rect3 = pygame.Rect(70+(3*75.714), 80, 75.714, 440)
rect4 = pygame.Rect(70+(4*75.714), 80, 75.714, 440)
rect5 = pygame.Rect(70+(5*75.714), 80, 75.714, 440)
rect6 = pygame.Rect(70+(6*75.714), 80, 75.714, 440)

def clear():
    global grid
    for i in range (6):
        for j in range (7):
            grid[i][j]=2
    return

def winner():
    pass
    



def welcome():
    SCREEN.fill((245,222,179))
    GAME_SPRITES['kack_g']=pygame.image.load('sprite\kack_g.png').convert_alpha()
    GAME_SPRITES['kack_g'] = pygame.transform.scale(GAME_SPRITES['kack_g'], (900, 600))
    SCREEN.blit(GAME_SPRITES['kack_g'], (0, 0))
    pygame.display.update()
    global no_match
    x=0
    z=0
    F=0
    active = False
    while True:
        for event in pygame.event.get():
                F=1
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(1)
                if event.type == MOUSEBUTTONDOWN and input_rect.collidepoint(event.pos):
                    active = True
                    z=1

                if event.type == KEYDOWN and active == True:
                    if event.key == K_BACKSPACE:
                        no_match = ''
                        welcome()
                     
                    if event.key == K_RETURN or event.key == K_KP_ENTER:
                        global nomatch 
                        try:
                            if int(no_match) > 0 and int(no_match) < 100:
                                nomatch = int(no_match)
                        except:
                            nomatch = 1
                        no_match=''
                        maingame()
                        return

                    else:
                        if(x<2):
                            if no_match == 'null':
                                no_match = event.unicode
                            else:
                                no_match += event.unicode
                            x+=1
                    
        
        pygame.draw.rect(SCREEN, (color[z]), input_rect, 5) 
        surface = font.render(no_match, True, (0,0,0))
        SCREEN.blit(surface,(425+11, 300+5+50))
        SCREEN.blit(GAME_SPRITES['logo'], (70, 20))
        SCREEN.blit(GAME_SPRITES['wel_1'], (90-30, 180+30))
        SCREEN.blit(GAME_SPRITES['wel_2'], (280-50, 220+30))
        SCREEN.blit(GAME_SPRITES['me'], (775-40, 555))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def maingame():
        global nomatch
    
            
        SCREEN.fill(pygame.Color('grey21'))
        f=1
        while True:
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit(1)
                    if event.type == MOUSEBUTTONDOWN and rectA.collidepoint(event.pos):
                        print ('down')
                        if event.type == MOUSEBUTTONDOWN and rect0.collidepoint(event.pos):
                            for i in range(5):
                                if grid[i][0]==2 and grid[i+1][0] != 2:
                                    GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                    SCREEN.blit(GAME_SPRITES['yellow'][f%2], (70,80+(i*73.33)))
                                    grid[i][0]=0
                                    f+=1
                                    break
                            if grid[5][0]==2:
                                GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                SCREEN.blit(GAME_SPRITES['yellow'][f%2], (70,80+(5*73.33)))
                                grid[5][0]=0
                                f+=1
                            print ('hi')

                        if event.type == MOUSEBUTTONDOWN and rect1.collidepoint(event.pos):
                            for i in range(5):
                                if grid[i][1]==2 and grid[i+1][1] != 2:
                                    GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                    SCREEN.blit(GAME_SPRITES['yellow'][f%2], (145.714,80+(i*73.33)))
                                    grid[i][1]=0
                                    f+=1
                                    pygame.display.update()
                                    break
                            if grid[5][1]==2:
                                GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                SCREEN.blit(GAME_SPRITES['yellow'][f%2], (145.714,80+(5*73.33)))
                                grid[5][1]=0
                                f+=1
                                pygame.display.update()
                        if event.type == MOUSEBUTTONDOWN and rect2.collidepoint(event.pos):
                            for i in range(5):
                                if grid[i][2]==2 and grid[i+1][2] != 2:
                                    GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                    SCREEN.blit(GAME_SPRITES['yellow'][f%2], (221.428,80+(i*73.33)))
                                    grid[i][2]=0
                                    f+=1
                                    break
                            if grid[5][2]==2:
                                GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                SCREEN.blit(GAME_SPRITES['yellow'][f%2], (221.428,80+(5*73.33)))
                                grid[5][2]=0
                                f+=1
                        if event.type == MOUSEBUTTONDOWN and rect3.collidepoint(event.pos):
                            for i in range(5):
                                if grid[i][3]==2 and grid[i+1][3] != 2:
                                    GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                    SCREEN.blit(GAME_SPRITES['yellow'][f%2], (297.142,80+(i*73.33)))
                                    grid[i][3]=0
                                    f+=1
                                    break
                            if grid[5][3]==2:
                                GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                SCREEN.blit(GAME_SPRITES['yellow'][f%2], (297.142,80+(5*73.33)))
                                grid[5][3]=0
                                f+=1
                        if event.type == MOUSEBUTTONDOWN and rect4.collidepoint(event.pos):
                            for i in range(5):
                                if grid[i][4]==2 and grid[i+1][4] != 2:
                                    GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                    SCREEN.blit(GAME_SPRITES['yellow'][f%2], (372.856,80+(i*73.33)))
                                    grid[i][4]=0
                                    f+=1
                                    break
                            if grid[5][4]==2:
                                GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                SCREEN.blit(GAME_SPRITES['yellow'][f%2], (372.856,80+(5*73.33)))
                                grid[5][4]=0
                                f+=1
                        if event.type == MOUSEBUTTONDOWN and rect5.collidepoint(event.pos):
                            for i in range(5):
                                if grid[i][5]==2 and grid[i+1][5] != 2:
                                    GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                    SCREEN.blit(GAME_SPRITES['yellow'][f%2], (448.57,80+(i*73.33)))
                                    grid[i][5]=0
                                    f+=1
                                    break
                            if grid[5][5]==2:
                                GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                SCREEN.blit(GAME_SPRITES['yellow'][f%2], (448.57,80+(5*73.33)))
                                grid[5][5]=0
                                f+=1
                        if event.type == MOUSEBUTTONDOWN and rect6.collidepoint(event.pos):
                            for i in range(5):
                                if grid[i][6]==2 and grid[i+1][6] != 2:
                                    GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                    SCREEN.blit(GAME_SPRITES['yellow'][f%2], (524.284,80+(i*73.33)))
                                    grid[i][6]=0
                                    f+=1
                                    break
                            if grid[5][6]==2:
                                GAME_SPRITES['yellow'][f%2] = pygame.transform.scale(GAME_SPRITES['yellow'][f%2], (70, 70))
                                SCREEN.blit(GAME_SPRITES['yellow'][f%2], (524.284,80+(5*73.33)))
                                grid[5][6]=0
                                f+=1

            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (100-30, 100-20), (100-30, 540-20),7)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (100-30, 540-20), (630-30, 540-20),7)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (630-30, 540-20), (630-30, 100-20),7)

            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (145.714, 80), (145.714, 520),7)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (221.428, 80), (221.428, 520),7)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (297.142, 80), (297.142, 520),7)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (372.856, 80), (372.856, 520),7)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (448.57, 80), (448.57, 520),7)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (524.284, 80), (524.284, 520),7)

            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (70, 80), (600, 80),2)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (70, 155-1.67), (600, 155-1.67),4)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (70, 230-1.67), (600, 230-1.67),4)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (70, 305-1.67), (600, 305-1.67),4)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (70, 380-1.67), (600, 380-1.67),4)
            pygame.draw.line(SCREEN, (pygame.Color('darkorchid3')),  (70, 455-1.67), (600, 455-1.67),4)
            pygame.display.update()
            
            if f==43:
                time.sleep(2)
                print ('match compeleted')
                clear()
                nomatch -=1
                if nomatch > 0:
                    maingame()
                else:
                    welcome()

                
if __name__ == '__main__':
    
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption('@half.quotes_')
    GAME_SPRITES['logo']=pygame.image.load('sprite\logo.png').convert_alpha()
    GAME_SPRITES['wel_1']=pygame.image.load('sprite\wel_1.png').convert_alpha()
    GAME_SPRITES['wel_2']=pygame.image.load('sprite\wel_2.png').convert_alpha()
    GAME_SPRITES['me']=pygame.image.load('sprite\me.png').convert_alpha()
    GAME_SPRITES['yellow']= [ pygame.image.load('sprite\yellow.png').convert_alpha(),
                            pygame.image.load('sprite\green.png').convert_alpha(),]
    welcome()
    