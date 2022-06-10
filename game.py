from pygame import * 
from random import randint
win_width=500
win_height=500
window = display.set_mode((win_width,win_height))#создаем объект окна игры - и задаем ему размер
display.set_caption("MY GAME")
BLUE=(0,0,255)
WHITE=(255,255,255)#Создаем белый цветс помощью RGB
RED=(255,0,0)
#Создаем персонажа
hero = image.load('platform.png')#поверхность 50 на 50 пикселей
hero=transform.scale(hero,(70,30))#закрашиваем красным
rect1 = hero.get_rect()#создаем 
rect1.x=230
rect1.y=470
enemy = image.load('bird.png')
enemy = transform.scale(enemy,(20,20))
rect2 = enemy.get_rect()
rect2.x = 50
rect2.y=50
point = 0
dead = 0
FPS = 150
font.init()
font24=font.SysFont('Arial',24)
text1 =font24.render("Пойманые:"+str(point),True,(255,0,0))
text2 =font24.render("Пропущеные:"+str(dead),True,(255,0,0))
text3 =font24.render("FPS:"+str(FPS),True,(255,0,0))
textwin =font24.render("ПОБЕДА!",True,(255,0,0))
textlose =font24.render("ПРОИГРЫШ!",True,(255,0,0))
backraund = image.load('fon.png')
backraund = transform.scale(backraund,(win_width,win_height))
#Запускаем основной игровой цикл
clock = time.Clock()
game = 'in_process'
while True:
    if game=='in_process':
        window.blit(backraund,(0,0))
        window.blit(text3,(400,0))
        window.blit(text1,(0,20))
        window.blit(text2,(0,40))
        window.blit(hero,(rect1.x,rect1.y))
        window.blit(enemy,(rect2.x,rect2.y))
        display.update()#фиксируем изменения - пишется всегда в конце
        rect2.y+=1
        if rect2.y > win_height:
            dead+=1
            text2 =font24.render("Пропущеные:"+str(dead),True,(255,0,0))
            rect2.x = randint(0, win_height - 20)
            rect2.y = 0
        if rect1.colliderect(rect2) == True:
            FPS+=10
            text3 =font24.render("FPS:"+str(FPS),True,(255,0,0))
            point+=1
            text1 =font24.render("Пойманые:"+str(point),True,(255,0,0))
            rect2.x = randint(0, win_height - 20)
            rect2.y = 0
        
        #Управление для персонажа
        keys = key.get_pressed()
        if keys[K_LEFT] and rect1.x>0:
            rect1.x-=1
        elif keys[K_RIGHT] and rect1.x + 70<win_width:
            rect1.x+=1
        if dead >= 10:
            game = 'lose'
        if point >= 10:
            game = 'win'
    elif game == 'win':
        window.blit(textwin,(250,250))   
        display.update() 
    elif game == 'lose':
        window.blit(textlose,(250,250))
        display.update()
    for i in event.get():
        if i.type==QUIT:
            quit()
        if i.type == KEYDOWN and game!= "in_process":
            if i.key == K_SPACE:
                point = 0
                dead = 0
                FPS = 150
                text2 =font24.render("Пропущеные:"+str(dead),True,(255,0,0))
                text1 =font24.render("Пойманые:"+str(point),True,(255,0,0))
                text3 =font24.render("FPS:"+str(FPS),True,(255,0,0))
                rect2.x = randint(0, win_height - 20)
                rect2.y = 0
                rect1.x=230
                rect1.y=470
                game = 'in_process'
    clock.tick(FPS)
   