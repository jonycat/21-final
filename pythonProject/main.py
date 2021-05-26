import random
import time
import pygame

# инициализация
pygame.init()
pygame.font.init()
pygame.mixer.init()

# music

pygame.mixer.music.load('music/kazino.mp3')
pygame.mixer.music.play(loops=99)
pygame.mixer.music.set_volume(0.4)

# main menu


# Настройки экрана
screen = pygame.display.set_mode((950, 500))

clock = pygame.time.Clock()

background_image = pygame.image.load('pics/table.jpg')

FPS = 60


# cards
tuz = 5
king = 4
dama = 3
valet = 2
ten = 10
nine = 9
eight = 8
seven = 7
six = 6
cards = [six, six, six, six, seven, seven, seven, seven, eight, eight, eight, eight, nine, nine, nine, nine, ten, ten,
         ten, ten, valet, valet, valet, valet, dama, dama, dama, dama, king, king, king, king, tuz, tuz, tuz, tuz]

ran = random.choice(cards)


#coordinates
win_lose_x = 400
win_lose_y = 200

o4ki_player_x = 350
o4ki_player_y = 400

text_player_x = 250
text_player_y = 400

text_bot_x = 250
text_bot_y = 100

o4ki_bot_x = 350
o4ki_bot_y = 100


text_uprav_x = 0
text_uprav_y = 0

text_restart_x = 400
text_restart_y = 250

text_draw_x = 450
text_draw_y = 200

text_e_x = 0
text_e_y = 20

text_r_x = 0
text_r_y = 40

text_q_x = 0
text_q_y = 60

text_mm_x = 0
text_mm_y = 80

text_exit_x = 0
text_exit_y = 100

text_count_x = 800
text_count_y = 20

text_win_player_x = 802
text_win_player_y = 60

text_win_bot_x = 830
text_win_bot_y = 90

text_c_p_x = 880
text_c_p_y = 60

text_c_b_x = 880
text_c_b_y = 90






max = 22
# colors
white = ((255, 255, 255))
blue = ((0, 0, 255))
green = ((0, 255, 0))
red = ((255, 0, 0))
black = ((0, 0, 0))

# очки
o4ko_player = '0'
o4ko_bot = '0'
o4ko_bot_final = 0

card_b1 = random.choice(cards)
card_b2 = random.choice(cards)
o4ko_bot_final = card_b1 + card_b2

c_p = '0'
c_b = '0'

p_ch = '' #выпавшие числа
max = 22

stop_word = 1
# Text + font
font = pygame.font.Font('font/bruh.ttf', 20)
text_player = font.render("Сумма: ", True, white)
text_bot = font.render("Сумма: ", True, white)
text_win = font.render("", True, white)
text_lose = font.render("", True, white)
text_restart = font.render("",True,white)
text_o4ki_player = font.render(o4ko_player, True, white)
text_o4ki_bot = font.render(o4ko_bot, True, white)
text_uprav = font.render("Управление:", True, white)
e = font.render("У = Добавить карту", True, white)  #text_add
r = font.render("К = Раскрыть карты", True, white)  #text_end
q = font.render("Й = Рестарт", True, white)         #text_restart
text_draw = font.render("", True, white)
text_main = font.render("", True, white)
text_exit = font.render("ESC - Выход из игры", True, white)

text_chisla = font.render("Выпавшие числа:", True, white)

TEXT_COUNT = font.render("С Ч Ё Т", True, white)

win_player = font.render("Игрок: ", True, white)
win_bot  = font.render("Бот: ", True, white)

count_p = font.render(c_p, True, white)
count_b = font.render(c_b, True, white)

text_null = font.render("Обнулить - С ", True, white)

p_chisla = font.render('', True, white)



true = True


# _____________________game stuff
o4ko_player = int(o4ko_player)
if o4ko_player > 21:
    print("lose")
    screen.blit(text_lose, (400, 250))
    screen.blit(background_image, (0, 0))
    o4ko_player = str(o4ko_player)
    print("lose text")

while True:






    # вывод фона
    screen.blit(background_image, (0, 0))

    # вывод текста
    screen.blit(text_player, (text_player_x, text_player_y))
    screen.blit(text_o4ki_player, (o4ki_player_x, o4ki_player_y))


    screen.blit(text_lose, (win_lose_x,win_lose_y))
    screen.blit(text_win, (win_lose_x, win_lose_y))


    screen.blit(text_restart,(text_restart_x,text_restart_y))
    screen.blit(text_uprav,(text_uprav_x,text_uprav_y))


    screen.blit(e,(text_e_x,text_e_y))
    screen.blit(r,(text_r_x,text_r_y))
    screen.blit(q,(text_q_x,text_q_y))



    screen.blit(text_draw, (text_draw_x,text_draw_y))
    screen.blit(text_main,(text_mm_x,text_mm_y))
    screen.blit(text_exit,(text_exit_x,text_exit_y))


    screen.blit(TEXT_COUNT,(text_count_x,text_count_y))
    screen.blit(win_player,(text_win_player_x,text_win_player_y))
    screen.blit(win_bot,(text_win_bot_x,text_win_bot_y))


    screen.blit(text_bot, (text_bot_x, text_bot_y))
    screen.blit(text_o4ki_bot, (o4ki_bot_x, o4ki_bot_y))

    screen.blit(win_player,(text_win_player_x,text_win_player_y))
    screen.blit(win_bot,(text_win_bot_x,text_win_bot_y))

    screen.blit(count_p,(text_c_p_x,text_c_p_y))
    screen.blit(count_b,(text_c_b_x,text_c_b_y))

    screen.blit(text_null, (802, 115))

    screen.blit(text_chisla, (200, 300))
    screen.blit(p_chisla,(400, 300))


    pygame.display.update()
    clock.tick(FPS)
    pygame.display.flip()

    # font

    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()

        o4ko_player = int(o4ko_player)
        o4ko_bot = int(o4ko_bot)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:

            c_p = '0'
            c_b = '0'
            count_p = font.render(c_p, True, white)
            count_b = font.render(c_b, True, white)

            screen.blit(count_p, (text_c_p_x, text_c_p_y))
            screen.blit(count_b, (text_c_b_x, text_c_b_y))

        if o4ko_player < 22:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and stop_word == 1:

                o4ko_player = int(o4ko_player)
                ran = random.choice(cards)
                ran = int(ran)
                text_o4ki_player = '0'


                o4ko_player = int(o4ko_player)
                o4ko_player += ran
                o4ko_player = str(o4ko_player)
                o4ko_bot = str(o4ko_bot)
                text_o4ki_player = 0
                text_o4ki_player = font.render(o4ko_player, True, white)
                text_o4ki_bot = font.render(o4ko_bot, True, white)

                ran = str(ran)

                p_ch += " " + ran
                print(p_ch)
                p_chisla = font.render(p_ch, True, white)
                ran = int(ran)
                cards.pop(ran)
                print(cards)


                o4ko_player = int(o4ko_player)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:

                    o4ko_player = '0'
                    o4ko_bot = '0'
                    p_ch = ' '
                    p_chisla = font.render(p_ch, True, white)
                    text_win = font.render("", True, white)
                    text_lose = font.render("", True, white)
                    text_restart = font.render("", True, white)
                    true = False
                    cards = [six, six, six, six, seven, seven, seven, seven, eight, eight, eight, eight, nine, nine,
                             nine,
                             nine, ten, ten,
                             ten, ten, valet, valet, valet, valet, dama, dama, dama, dama, king, king, king, king, tuz,
                             tuz,
                             tuz, tuz]






                o4ko_player = int(o4ko_player)
                o4ko_bot = int(o4ko_bot)
                if o4ko_player > 21:
                    c_b = str(int(c_b) + 1)
                    count_b = font.render(c_b, True, white)
                    text_lose = font.render("Вы Проиграли", True, white)
                    text_restart = font.render("Нажмите Й для рестарта", True, white)

                    screen.blit(text_lose, (400, 250))
                    screen.blit(text_restart, (500, 250))
                    screen.blit(count_b, (text_c_b_x, text_c_b_y))



        if max > o4ko_player :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                o4ko_bot = o4ko_bot_final
                o4ko_player = int(o4ko_player)
                o4ko_bot = str(o4ko_bot_final)



                text_o4ki_bot = font.render(o4ko_bot, True, white)

                o4ko_bot = int(o4ko_bot)
                if o4ko_player > o4ko_bot or o4ko_bot > 21:
                    text_win = font.render("Вы Выиграли", True, white)
                    text_restart = font.render("Нажмите Й для рестарта", True, white)

                    c_p = str(int(c_p) + 1)
                    count_p = font.render(c_p, True, white)
                    screen.blit(count_p, (text_c_p_x, text_c_p_y))


                elif o4ko_bot == o4ko_player:
                    text_draw = font.render("Ничья", True, white)
                    text_restart = font.render("Нажмите Й для рестарта", True, white)
                    stop_word = 0
                else:
                    text_lose = font.render("Вы Проиграли", True, white)
                    text_restart = font.render("Нажмите Й для рестарта", True, white)
                    o4ko_bot = str(o4ko_bot_final)
                    text_o4ki_bot = font.render(o4ko_bot, True, white)
                    o4ko_bot = int(o4ko_bot_final)

                    c_b = str(int(c_b) + 1)
                    count_b = font.render(c_b, True, white)
                    screen.blit(count_b, (text_c_b_x, text_c_b_y))

                stop_word = 0






        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            p_ch = ' '
            p_chisla = font.render(p_ch, True, white)

            o4ko_player = '0'
            o4ko_bot = '0'

            card_b1 = random.choice(cards)
            card_b2 = random.choice(cards)
            o4ko_bot_final = card_b1 + card_b2



            text_win = font.render("", True, white)
            text_lose = font.render("", True, white)
            text_restart = font.render("", True, white)
            text_draw = font.render("", True, white)
            text_o4ki_player = font.render(o4ko_player, True, white)
            text_o4ki_bot = font.render(o4ko_bot, True, white)
            true = False


            stop_word = 1

            cards = [six, six, six, six, seven, seven, seven, seven, eight, eight, eight, eight, nine, nine, nine, nine,
                     ten, ten,
                     ten, ten, valet, valet, valet, valet, dama, dama, dama, dama, king, king, king, king, tuz, tuz,
                     tuz, tuz]

        o4ko_bot = str(o4ko_bot)
        o4ko_player = str(o4ko_player)





