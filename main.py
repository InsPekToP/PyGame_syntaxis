#импортируем и инициализируем библиотеку
import pygame

pygame.init()

#Устанавливаем ширину и высоту в пикселях
WIDTH = 800
HEIGHT = 600

#Настраиваем окно отрисовки
screen = pygame.display.set_mode([WIDTH,HEIGHT])

#Игровой цикл выполняется,пока пользователь не захочет выйти
running = True
while running:
    #Нажал ли пользователь кнопку закрытия окна?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    
    #Заполняем фон белым цветом
    screen.fill((255,255,255))

    #Рисуем синий круг в центре экрана радиусом 50
    pygame.draw.circle(screen,(0,0,255),(WIDTH//2,HEIGHT//2),50)

    #Рисуем красный контуреый квадрат в верхнем левом углу экрана
    red_square = pygame.Rect((50,50),(100,100))
    pygame.draw.rect(screen,(200,0,0),red_square,1)

    #Рисуем оранжевый текст с кеглем 60
    text_font = pygame.font.SysFont("any_font",60)
    text_block = text_font.render(
        "Hello, World! From Pygame",False,(200,100,0)
    )
    screen.blit(text_block,(50,HEIGHT-50))

    #Обновляем экран
    pygame.display.flip()

#Цикл завершился!Уходим
pygame.quit()