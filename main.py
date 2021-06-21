import pygame, sys, random


def ball_movement():
    global ball_speed_x, ball_speed_y, pl_score, opp_score, game_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        pl_score +=1
        game_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        opp_score +=1
        game_time = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_movement():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def restart():
    global ball_speed_x, ball_speed_y, game_time

    curr_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    #Таймер
    tic = 3
    border = 0
    while border < 1800:
        if border < curr_time - game_time < (border + 600):
            timer = font.render(str(tic), False, grey)
            screen.blit(timer, (screen_width / 2 - 8, screen_height / 2 + 25))
        tic -= 1
        border += 600

    if curr_time - game_time < 1800:
        ball_speed_x = 0
        ball_speed_y = 0
    else:
        ball_speed_x = 5 * random.choice((1, -1))
        ball_speed_y = 5 * random.choice((1, -1))
        game_time = None



pygame.init()
clock = pygame.time.Clock()

#Окно
screen_width = 1000
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping-Pong')

#rect
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

background = pygame.Color('black')
grey = (190, 200, 200)

ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
player_speed = 0
opponent_speed = 8

pl_score = 0
opp_score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

game_time = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5


    ball_movement()
    player_movement()
    opponent_movement()


    # Объекты
    screen.fill(background)
    pygame.draw.rect(screen, grey, player)
    pygame.draw.rect(screen, grey, opponent)
    pygame.draw.ellipse(screen, grey, ball)
    pygame.draw.aaline(screen, grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if game_time:
        restart()


    #Счет
    pl_text = font.render(f"{pl_score}", False, grey)
    screen.blit(pl_text, (540, 375))

    opp_text = font.render(f"{opp_score}", False, grey)
    screen.blit(opp_text, (450, 375))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)
