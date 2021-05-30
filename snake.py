import pygame
import random
import emoji



pygame.mixer.init()
# pygame.mixer.music.load('resources/crash.mp3')
# pygame.mixer.music.play()

from pygame.constants import K_DOWN, K_SPACE
pygame.init()

# screen  size variables
screen_width=1000 
screen_height=600


# putting logo  in welcome page 
img=pygame.image.load('resources/logo.png')
img=pygame.transform.scale(img,(int(screen_width*(0.40)),int(screen_height*(0.40))))# scaling image to some other size

# colors
# white=(255,255,255)
# red=(255,0,0)
# black=(0,0,0)
white=(12, 39, 12)
red=(51, 204, 0)
black=(255, 71, 26)
welcome_page_bg=(201, 235, 140)
welcome_page_txt=(45, 85, 30)
welcome_page_key=(219, 74, 48)
# ora=(255, 71, 26)
# green=(51, 204, 0)
# bg=(12, 39, 12)



gameWindow=pygame.display.set_mode((screen_width,screen_height)) # setting the display 
pygame.display.set_caption("Snake Game by Ro__")                 # setting title 
pygame.display.update()

font=pygame.font.SysFont('arial',50,bold=True)
# this is a function to display text on display
def score_on_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
    
# this is the function to plot snake 
def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
    

clock=pygame.time.Clock()
def welcome_page():
    exit_game=False 
    while not exit_game:
        gameWindow.fill(welcome_page_bg)
        #====================================
        
        gameWindow.blit(img,(300,50))
        #=====================================
        score_on_screen("Welcome  To  Snake  Game  By Ro__",welcome_page_txt,screen_width*(0.150),screen_height*(0.550))
        score_on_screen("Press SpaceBar  to Play...!",welcome_page_key,screen_width*(0.230),screen_height*(0.700))
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==K_SPACE:
                        pygame.mixer.music.load('resources/bg.mp3')
                        pygame.mixer.music.play(loops=-1)
                        gameloop()
                        
        pygame.display.update()
        clock.tick(60)
        
        
#Game Loop
def gameloop():
    # game variables
    exit_game=False 
    game_over=False
    snake_x=45
    snake_y=50 
    snake_size=20
    velocity_x=0
    velocity_y=0
    fps=30
    food_x=random.randint(25,(0.75)*screen_width)
    food_y=random.randint(25,(0.75)*screen_height)
    score=0
    snake_list=[]
    snake_length=1
    
    
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            score_on_screen("Game Over!...Press Enter to Continue",red,screen_width*(0.150),screen_height*(0.40))
            # txtstr=emoji.emojize(' 😂')
            score_on_screen("Your Current Score :"+" "+str(score*10),black,screen_width*(0.300),screen_height*(0.50))#   after added
            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome_page()                                                           #gameloop()
        else:
            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        # snake_x+=10
                        velocity_x=6
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        # snake_x-=10
                        velocity_x=-6
                        velocity_y=0
                    if event.key==pygame.K_DOWN:
                        # snake_y+=10
                        velocity_y=6
                        velocity_x=0
                    if event.key==pygame.K_UP:
                        # snake_y-=10
                        velocity_y=-6
                        velocity_x=0
            snake_x+=velocity_x
            snake_y+=velocity_y
            
            
            if abs(snake_x-food_x)<=7 and abs(snake_y-food_y)<=7:
                score+=1
                # pygame.mixer.music.load('resources/food_snake.wav')
                # pygame.mixer.music.play()
                # #------------------------------------------------------------------
                # pygame.mixer.music.load('resources/bg.mp3')
                # pygame.mixer.music.play()
                # #----------------------------------------------------------
                # print("Score :",score) 
                food_x=random.randint(25,(0.75)*screen_width)
                food_y=random.randint(25,(0.75)*screen_height)
                snake_length+=5
                
                
            
            gameWindow.fill(white)
            score_on_screen("Score :"+str(score*10),red,5,5)
            
            pygame.draw.rect(gameWindow, red,[food_x,food_y,snake_size,snake_size])
            
            
            
            
            head=[snake_x,snake_y]
            snake_list.append(head)
            
            
            if len(snake_list)>snake_length:
                del snake_list[0]
            
            
            
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('resources/crash.mp3')
                pygame.mixer.music.play()
            
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('resources/crash.mp3')
                pygame.mixer.music.play()
                
            
            # pygame.draw.rect(gameWindow, black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
        
            

    pygame.quit()
    quit()
welcome_page()