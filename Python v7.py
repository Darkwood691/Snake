import pygame
import random
import scoreSort
pygame.font.init()
pygame.init()

#colour definitions -----------------------------------------------
white = (240,240,240)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (80,80,80)

#display window setup----------------------------------------------

resolution = [640,640]

gameDisplay = pygame.display.set_mode(resolution) #set window size
pygame.display.set_caption("Snake") #set window title

"""pygame.display.update() #update display window"""

#variable setup---------------------------------------------------------

sortType = "merge"

entryFont=pygame.font.SysFont("TimesNewRoman",15,bold=True,italic=False,)
myFont=pygame.font.SysFont("TimesNewRoman", 20, bold=False, italic=False)
scoreFont=pygame.font.SysFont("TimesNewRoman",20,bold=True,italic=False)
bigFont=pygame.font.SysFont("TimesNewRoman", 50, bold=True, italic=False)
highScoreFont=pygame.font.SysFont("Arial", 20,False)

score=0

lead_x = 280
lead_y = 280
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

global size   #speed & size of block
size = 20

#snake body variables
snake = []
count=0
snakeLen=2
growthFactor=2
#---------------------

fruit=False
gameExit=False
gameOver=False

#Defining Exit------------------------------

def end():
    pygame.quit()
    quit()


#Pause-----------------------------------------------------

def pause():
    pauseText = bigFont.render(("Pause"),True,(green))
    gameDisplay.blit(pauseText,((resolution[0]*(1/3)+40),((resolution[1]-100)/2)))
    pygame.display.update()
    #pygame.time.wait(150)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(9)==1:
                    return

        
                
        clock.tick(60)
#start menu---------------------------------------------------------

colour_inactive = (150,150,150)
colour_active = (0,0,0)
colour = colour_inactive
textActive=False
name=""
gameStart=False

gameDisplay.fill(white)
logo = bigFont.render(("SNAKE"),True,(black))
gameDisplay.blit(logo,((resolution[0]*(1/3)+10),((resolution[1]-100)/2)))
pygame.display.update()

input_box = pygame.draw.rect(gameDisplay,colour,[(resolution[0]*(1/3)),((resolution[1]-100)/2),140,20])

emptyScoreboard=True
fail=False


try:
    scoreboard = open("scoreboard.txt", "r")
    oldScores=scoreboard.read()
    #print(scoreSort.scoreSort(oldScores))
    highScores=(scoreSort.sortPrep(oldScores,sortType))
    HS=len(highScores)
    if HS>=5:
        scoreFive=" ".join(highScores[4])
    if HS>=4:
        scoreFour=" ".join(highScores[3])
    if HS>=3:
        scoreThree=" ".join(highScores[2])
    if HS>=2:
        scoreTwo=" ".join(highScores[1])
    if HS>=1:
           scoreOne=" ".join(highScores[0])
           emptyScoreboard=False
except:
    print("scoreboard.txt not found")
    scoreboard=open("scoreboard.txt","w")
    print("scoreboard.txt has been created")
    fail=True





    

while gameStart!=True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                textActive = not textActive
            else:
                textActive = False

            colour = colour_active if textActive else colour_inactive
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                    gameStart=True
            if textActive:
                if event.key == pygame.K_RETURN:
                    gameStart=True
                elif event.key == pygame.K_BACKSPACE:
                    name=name[:-1]
                else:
                    name += event.unicode
            
        if event.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(9)==1:
                gameStart=True
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
        
    
                
    gameDisplay.fill(white)
    
    labOne = scoreFont.render(("Enter Name:"),False,(0,0,0))
    gameDisplay.blit(labOne,((resolution[0]*(1/3)),((resolution[1]-145)/2)))
    
    txt_surface = entryFont.render(name, True, black)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    gameDisplay.blit(txt_surface, (input_box.x+2,input_box.y+2))
    pygame.draw.rect(gameDisplay,colour,input_box,2)           
    #lables
    labTwo = myFont.render(("Press Enter to start"),True,(0,0,0))
    gameDisplay.blit(labTwo,((resolution[0]*(1/3)),((resolution[1])/2)-20))
    labThree = myFont.render(("WASD or Arrow Keys to move"),True,(0,0,0))
    gameDisplay.blit(labThree,((resolution[0]*(1/3)),((resolution[1])/2)))
    labFour = myFont.render(("Escape to pause/unpause"),True,(0,0,0))
    gameDisplay.blit(labFour,((resolution[0]*(1/3)),((resolution[1])/2)+20))
    
    #scores
    if emptyScoreboard==False:
        labFive = scoreFont.render(("HighScores:"),True,(0,0,0))
        gameDisplay.blit(labFive,(15,3))
        if HS>=1:
            scoreA = highScoreFont.render(("1 %s" % scoreOne),True,(0,0,0))
            gameDisplay.blit(scoreA,(15,25))
        if HS>=2:
            scoreB = highScoreFont.render(("2 %s" % scoreTwo),True,(0,0,0))
            gameDisplay.blit(scoreB,(15,45))
        if HS>=3:
            scoreC = highScoreFont.render(("3 %s" % scoreThree),True,(0,0,0))
            gameDisplay.blit(scoreC,(15,65))
        if HS>=4:
            scoreD = highScoreFont.render(("4 %s" % scoreFour),True,(0,0,0))
            gameDisplay.blit(scoreD,(15,85))
        if HS>=5:
            scoreE = highScoreFont.render(("5 %s" % scoreFive),True,(0,0,0))
            gameDisplay.blit(scoreE,(15,105))
         
    pygame.display.update()
                    
    clock.tick(60)
                    
    

#game loop---------------------------------------------------------------------

while gameExit != True:   #event handling (keypresses)
    #event detection------------------------------------------------------------------
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            end()
        if event.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(9)==1:
                pause()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if lead_x_change == 0:
                    lead_x_change = -size         
                    lead_y_change = 0
                    break
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:        
                if lead_x_change == 0:
                    lead_x_change = size                                                            
                    lead_y_change = 0
                    break
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if lead_y_change == 0:
                    lead_y_change = -size
                    lead_x_change = 0
                    break
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if lead_y_change == 0:
                    lead_y_change = size
                    lead_x_change = 0
                    break
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
        hats = joystick.get_numhats()
        for i in range(hats):
            hat=joystick.get_hat(i)
            if hat==(1,0):
                #right
                if lead_x_change == 0:
                    lead_x_change = size                                                            
                    lead_y_change = 0
            elif hat==(-1,0):
                #left
                if lead_x_change == 0:
                    lead_x_change = -size         
                    lead_y_change = 0
            elif hat==(0,1):
                #up
                if lead_y_change == 0:
                    lead_y_change = -size
                    lead_x_change = 0
            elif hat==(0,-1):
                #down
                if lead_y_change == 0:
                    lead_y_change = size
                    lead_x_change = 0
            """elif hat==(1,1):
                #right&up
                if lead_x_change == size:
                    lead_x_change = 0
                    lead_y_change = -size
                    print("1")
                elif lead_y_change == -size:
                    lead_y_change = 0
                    lead_x_change = size
                    print("2")
            elif hat==(1,-1):
                #right&down
                if lead_x_change == size:
                    lead_x_change = 0
                    lead_y_change = size
                    print("1")
                elif lead_y_change == size:
                    lead_y_change = 0
                    lead_x_change = size
                    print("2")
            elif hat==(-1,1):
                #left&up
                if lead_x_change == -size:
                    lead_x_change = 0
                    lead_y_change = -size
                    print("1")
                elif lead_y_change == -size:
                    lead_y_change = 0
                    lead_x_change = -size
                    print("2")
            elif hat==(-1,-1):
                #left&down
                if lead_x_change == -size:
                    lead_x_change = 0
                    lead_y_change = size
                    print("1")
                elif lead_y_change == size:
                    lead_y_change = 0
                    lead_x_change = -size
                    print("2")"""
            
    #dispaly wipe-----------------------------------------------------------                

    gameDisplay.fill(white)

    #font---------------------------------------------------------------------
    textSurface = scoreFont.render((" %s" % score),True,(0,0,0))
    gameDisplay.blit(textSurface,(0,0))  
    
    #movement---------------------------------------------------------------
           
    lead_x += lead_x_change
    lead_y += lead_y_change

    #print("x:",lead_x_change," y:",lead_y_change," ",lead_x," ",lead_y)

    
    #death check-------------------------------------------
    for cords in snake:
        if score>=1:
            if lead_x==cords[0] and lead_y==cords[1]:
                gameOver=True
                
    if lead_x < 0:
        print("Game Over")
        gameOver = True
    elif lead_y < 0:
        print("Game Over")
        gameOver = True
    elif lead_x == resolution[0]:
        print("Game Over")
        gameOver = True
    elif lead_y == resolution[1]:
        print("Game Over")
        gameOver = True
    if gameOver == True:
        gameExit = True
    
    #fruit placement--------------------------------------------------------
    goodPlacement=False
    while goodPlacement != True:
        check=0
        goodPlacement=False
        if fruit == False:
            fruit_x=(random.randint(0,(resolution[0]-20)/size))*size
            fruit_y=(random.randint(0,(resolution[1]-20)/size))*size
            
            if fruit_x==lead_x and fruit_y==lead_y:
                print("Bad placement Head") # for testing
                check+=1
            for cords in snake:
                if fruit_x==cords[0] and fruit_y==cords[1]:
                    print("Bad placement Body")
                    check+=1
            #print(check)
            if check == 0:
                goodPlacement=True
                fruit=True
                        
            #print(fruit_x,fruit_y) # for testing
        elif fruit == True:
            #print("break ",check," fruit:",fruit)
            break
        
    #eat fruit---------------------------------------------
    if fruit_x==lead_x and fruit_y==lead_y:
        fruit=False
        score=score+1
        snakeLen+=growthFactor
        #print(score)

    #snake body---------------------------------------------------------------
        
    if snakeLen < len(snake):
        del snake[0]
    
    snake.append([lead_x,lead_y])    
    
    for item in snake:
        pygame.draw.rect(gameDisplay, grey, [(item[0]),(item[1]),size,size])
        
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,size,size]) # x,y (from top left), width, height    #snake head
    pygame.draw.rect(gameDisplay, red, [fruit_x,fruit_y,size,size]) #fruit
    
    pygame.display.update()

    
    if score <=5:
        clock.tick(8)
    elif score <= 10:
        clock.tick(9)
    elif score <= 15:
        clock.tick(10)
    elif score >15:
        clock.tick(11)
    #clock.tick(12)

#Game Over Screen---------------------------------------------------------------------
    
if gameOver == True:
    gameDisplay.fill(white)
    gameOverText = bigFont.render(("Game Over   Score: %s" %score),False,(0,0,0))
    gameDisplay.blit(gameOverText,((resolution[0]*(1/7)),((resolution[1]-100)/2)))
    pygame.display.update()
    pygame.time.wait(2000)    
    
    score=str(score)
    if name=="" or int(score)==0:
        end()
    else:       
        entry=(name+" "+score+"\n")
        if fail==False:
            scoreboard = open("scoreboard.txt","a")
        scoreboard.write(entry)
        scoreboard.close()
    

    
#end--------------------------------
end()
































