# from pygame import *
# import math  # Импортируем модуль для расчета расстояний

# # Инициализация Pygame
# init()

# # Загрузка фона и настройка окна
# background = transform.scale(image.load('sea.png'), (700, 500))
# window = display.set_mode((700, 500))
# display.set_caption('Лабиринт (Переработанная версия)')

# class GameSprite(sprite.Sprite):
#     def __init__(self, picture, w, h, x, y):
#         super().__init__()
#         self.image = transform.scale(image.load(picture), (w, h))
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# wall_1 = GameSprite('buoys_h.png', 400, 65, 5, 430)
# wall_2 = GameSprite('buoys_v.png', 65, 390, 0, 50)
# wall_3 = GameSprite('buoys_v.png', 65, 360, 125, -10)
# wall_4 = GameSprite('buoys_v.png', 65, 385, 250, 50)
# wall_5 = GameSprite('buoys_v.png', 65, 360, 375, -10)
# wall_6 = GameSprite('buoys_v.png', 65, 390, 500, 50)
# wall_7 = GameSprite('buoys_v.png', 65, 415, 635, -10)
# wall_8 = GameSprite('mini_buoys_h.png', 150, 65, 405, 430)

# treasure = GameSprite('treasure.png', 150, 100, 555, 400)
# island = GameSprite('island.png', 150, 100, 555, 400)
# loss = GameSprite('loss.png', 500, 500, 100, -25)
# key = GameSprite('key.png', 70, 25, 570, 100)
# start_arch = GameSprite('start.png', 75, 75, 55, -10)
# finish_arch = GameSprite('finish.png', 100, 100, 550, 315)

# arrow_1 = GameSprite('arrow_right.png', 50, 25, 65, 430)
# arrow_2 = GameSprite('arrow_up.png', 25, 50, 260, 365)
# arrow_3 = GameSprite('arrow_right.png', 50, 25, 195, 0)
# arrow_4 = GameSprite('arrow_down.png', 25, 50, 380, 0)
# arrow_5 = GameSprite('arrow_right.png', 50, 25, 315, 430)
# arrow_6 = GameSprite('arrow_up.png', 25, 50, 510, 365)
# arrow_7 = GameSprite('arrow_right.png', 50, 25, 445, 0)
# arrow_8 = GameSprite('arrow_down.png', 25, 50, 640, 0)

# arrows = sprite.Group()
# arrows.add(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8)

# barriers = sprite.Group()
# barriers.add(wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8)

# class Weapon(GameSprite):
#     def __init__(self, picture, w, h, x, y, x_speed, y_speed=0):
#         super().__init__(picture, w, h, x, y)
#         self.speed = x_speed
#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.x > 710 or sprite.spritecollide(self, barriers, False):
#             self.kill()

# class EnemyWeapon(GameSprite):
#     def __init__(self, picture, w, h, x, y, x_speed, y_speed=0):
#         super().__init__(picture, w, h, x, y)
#         self.speed = x_speed
#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.x < 0 or sprite.spritecollide(self, barriers, False):
#             self.kill()

# class Player(GameSprite):
#     def __init__(self, picture, w, h, x, y, x_speed, y_speed):
#         super().__init__(picture, w, h, x, y)
#         self.x_speed = x_speed
#         self.y_speed = y_speed
#     def update(self):
#         old_x = self.rect.x
#         old_y = self.rect.y
#         self.rect.x += self.x_speed
#         self.rect.y += self.y_speed
#         if sprite.spritecollide(self, barriers, False):
#             self.rect.x = old_x
#             self.rect.y = old_y
#     def fire(self):
#         core = Weapon('cannon_core.png', 20, 20, self.rect.right, self.rect.centery, 15)
#         weapons.add(core)
# weapons = sprite.Group()

# class Enemy(GameSprite):
#     def __init__(self, picture, w, h, x, y, left_x, right_x, x_speed=2, y_speed=0, shooting_range=100, firing_delay=2000):
#         super().__init__(picture, w, h, x, y)
#         self.speed = x_speed
#         self.direction = 'left'
#         self.left_x = left_x
#         self.right_x = right_x
#         self.shooting_range = shooting_range
#         self.firing_delay = firing_delay
#         self.last_shot_time = 0
#     def can_see_player(self, player):
#         """Проверяет, находится ли игрок в зоне поражения и примерно на одной высоте с врагом."""
#         horizontal_distance = abs(self.rect.centerx - player.rect.centerx)  # Горизонтальное расстояние
#         vertical_distance = abs(self.rect.centery - player.rect.centery)   # Вертикальное расстояние
#         # Возвращаем True только если оба условия выполняются:
#         # 1. Игрок находится в пределах горизонтального радиуса поражения
#         # 2. Игрок находится примерно на одной высоте с врагом (разница по вертикали не превышает 10 пикселей)
#         return (horizontal_distance <= self.shooting_range and vertical_distance <= 10)
#     def shoot(self):
#         current_time = time.get_ticks()
#         if current_time - self.last_shot_time > self.firing_delay and self.can_see_player(player):
#             bullet = EnemyWeapon('cannon_core.png', 20, 20, self.rect.left, self.rect.centery, -15)
#             enemy_weapons.add(bullet)
#             self.last_shot_time = current_time
    
#     def update(self):
#         if self.rect.x <= self.left_x:
#             self.direction = 'right'
#         elif self.rect.x >= self.right_x:
#             self.direction = 'left'
#         if self.direction == 'left':
#             self.rect.x -= self.speed
#         else:
#             self.rect.x += self.speed  
#         self.shoot()

# enemy_1 = Enemy('enemy_ship_1.png', 50, 50, 200, 375, 65, 200)
# enemy_2 = Enemy('enemy_ship_2.png', 50, 50, 200, 0, 200, 325)
# enemy_3 = Enemy('enemy_ship_3.png', 50, 50, 315, 375, 315, 440)
# enemy_4 = Enemy('enemy_ship_4.png', 50, 50, 550, 0, 435, 590)
# # player = Player('player_ship.png', 60, 50, 0, 0, 0, 0)
# player = Player('player_ship.png', 60, 50, 445, 100, 0, 0)

# enemies = sprite.Group()
# enemies.add(enemy_1, enemy_2, enemy_3, enemy_4)
# enemy_weapons = sprite.Group()

# run = True
# finish = False
# enemy_4_killed = False

# font.init()
# font = font.SysFont('Arial', 100)
# win_title = font.render('Ты выиграл!', True, (0, 255, 0))
# loss_title = font.render('Ты проиграл!', True, (255, 0, 0))
# win_background = transform.scale(image.load('win.png'), (700, 500))
# while run:
#     for e in event.get():
#         if e.type == QUIT:
#             run = False
#         elif e.type == KEYDOWN:
#             if e.key == K_UP or e.key == K_w:
#                 player.y_speed = -5
#             elif e.key == K_DOWN or e.key == K_s:
#                 player.y_speed = 5
#             elif e.key == K_LEFT or e.key == K_a:
#                 player.x_speed = -5
#             elif e.key == K_RIGHT or e.key == K_d:
#                 player.x_speed = 5
#             elif e.key == K_SPACE:
#                 player.fire()
#         elif e.type == KEYUP:
#             if e.key == K_UP or e.key == K_DOWN or e.key == K_w or e.key == K_s:
#                 player.y_speed = 0
#             elif e.key == K_LEFT or e.key == K_RIGHT or e.key == K_a or e.key == K_d:
#                 player.x_speed = 0
#     if finish != True:
#         window.blit(background, (0, 0))  # Фон обновляется каждый кадр
#         if enemy_4_killed == True:
#             key.reset()
#         player.reset()
#         island.reset()
#         treasure.reset()   
#         start_arch.reset()
#         finish_arch.reset()
#         barriers.draw(window)
#         arrows.draw(window)
#         enemies.draw(window)
#         weapons.draw(window)
#         enemy_weapons.draw(window)
#         # key.reset()
#         if sprite.collide_rect(player, treasure):
#             finish = True
#             window.blit(win_background, (0, 0))
#             window.blit(win_title, (105, -20))
#         if sprite.groupcollide(sprite.Group(player), enemies, True, False):
#             finish = True
#             window.blit(background, (0, 0))
#             loss.reset()
#             window.blit(loss_title, (100, 350))
#         if sprite.groupcollide(sprite.Group(player), enemy_weapons, True, False):
#             finish = True
#             window.blit(background, (0, 0))
#             loss.reset()
#             window.blit(loss_title, (100, 350))
#         if sprite.groupcollide(weapons, enemies, True, True):
#             continue
#         if sprite.groupcollide(weapons, sprite.Group(enemy_4), True, True):
#             enemy_4_killed = True
#             print('пуля попала в 4-ого врага')
#         if sprite.collide_rect(player, key):
#             key.kill()
#             print('игрок и ключ коснулись')
#     player.update()
#     enemies.update()
#     weapons.update()
#     enemy_weapons.update()
#     display.update()
#     time.delay(50)
# quit()

from pygame import *
<<<<<<< HEAD
import math  # Для расчёта расстояний

# --- Инициализация Pygame ---
init()
=======
import math  # Импортируем модуль для расчета расстояний
init() # Инициализация Pygame

# Загрузка фона и настройка окна
>>>>>>> 3c0131d1077b2cb831ff388a03bca1286dc22b33
background = transform.scale(image.load('sea.png'), (700, 500))
window = display.set_mode((700, 500))
display.set_caption('Лабиринт (Переработанная версия)')
clock = time.Clock()

# --- Класс базового спрайта с правильным вызовом super().__init__() ---
class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()   # правильно вызываем конструктор родителя
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# --- Определяем стены (барьеры) ---
wall_1 = GameSprite('buoys_h.png', 400, 65, 5, 430)
wall_2 = GameSprite('buoys_v.png', 65, 390, 0, 50)
wall_3 = GameSprite('buoys_v.png', 65, 360, 125, -10)
wall_4 = GameSprite('buoys_v.png', 65, 385, 250, 50)
wall_5 = GameSprite('buoys_v.png', 65, 360, 375, -10)
wall_6 = GameSprite('buoys_v.png', 65, 390, 500, 50)
wall_7 = GameSprite('buoys_v.png', 65, 415, 635, -10)
wall_8 = GameSprite('mini_buoys_h.png', 150, 65, 405, 430)

barriers = sprite.Group()
barriers.add(wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8)


# --- Дополнительные спрайты: сокровище, остров, потеря, ключ, арки старта/финиша ---
treasure    = GameSprite('treasure.png', 150, 100, 555, 400)
island      = GameSprite('island.png',   150, 100, 555, 400)
loss        = GameSprite('loss.png',     500, 500, 100, -25)
key         = GameSprite('key.png',       70, 25,  570, 100)
start_arch  = GameSprite('start.png',     75, 75,   55, -10)
finish_arch = GameSprite('finish.png',   100, 100, 550, 315)


# --- Стрелки (индикаторы направления) ---
arrow_1 = GameSprite('arrow_right.png', 50, 25, 65, 430)
arrow_2 = GameSprite('arrow_up.png',    25, 50, 260, 365)
arrow_3 = GameSprite('arrow_right.png', 50, 25, 195, 0)
arrow_4 = GameSprite('arrow_down.png',  25, 50, 380, 0)
arrow_5 = GameSprite('arrow_right.png', 50, 25, 315, 430)
arrow_6 = GameSprite('arrow_up.png',    25, 50, 510, 365)
arrow_7 = GameSprite('arrow_right.png', 50, 25, 445, 0)
arrow_8 = GameSprite('arrow_down.png',  25, 50, 640, 0)

arrows = sprite.Group()
arrows.add(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8)


# --- Класс оружия игрока ---
class Weapon(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed=0):
        super().__init__(picture, w, h, x, y)
        self.speed = x_speed

    def update(self):
        self.rect.x += self.speed
        # Если пуля улетает за границы экрана или врезается в стену — удаляем её
        if self.rect.x > 710 or sprite.spritecollide(self, barriers, False):
            self.kill()
<<<<<<< HEAD


# --- Класс оружия врага (стреляет влево) ---
=======
        
>>>>>>> 3c0131d1077b2cb831ff388a03bca1286dc22b33
class EnemyWeapon(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed=0):
        super().__init__(picture, w, h, x, y)
        self.speed = x_speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or sprite.spritecollide(self, barriers, False):
            self.kill()


weapons       = sprite.Group()
enemy_weapons = sprite.Group()


# --- Класс игрока ---
class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        old_x = self.rect.x
        old_y = self.rect.y
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        # Проверяем столкновение с любым барьером
        if sprite.spritecollide(self, barriers, False):
            self.rect.x = old_x
            self.rect.y = old_y

    def fire(self):
        # Создаём пулю из правого борта корабля
        core = Weapon('cannon_core.png', 20, 20, self.rect.right, self.rect.centery, 15)
        weapons.add(core)


player = Player('player_ship.png', 60, 50, 445, 100, 0, 0)


# --- Класс врага ---
class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, left_x, right_x,
                 x_speed=2, y_speed=0, shooting_range=100, firing_delay=2000):
        super().__init__(picture, w, h, x, y)
        self.speed = x_speed
        self.direction = 'left'
        self.left_x = left_x
        self.right_x = right_x
        self.shooting_range = shooting_range
        self.firing_delay = firing_delay
        self.last_shot_time = 0

    def can_see_player(self, player):
        horizontal_distance = abs(self.rect.centerx - player.rect.centerx)
        vertical_distance   = abs(self.rect.centery - player.rect.centery)
        # Вернём True, если игрок в пределах радиуса и примерно на одной высоте (±10 px)
        return (horizontal_distance <= self.shooting_range and vertical_distance <= 10)

    def shoot(self):
        current_time = time.get_ticks()
        if current_time - self.last_shot_time > self.firing_delay and self.can_see_player(player):
            bullet = EnemyWeapon('cannon_core.png', 20, 20, self.rect.left, self.rect.centery, -15)
            enemy_weapons.add(bullet)
            self.last_shot_time = current_time
<<<<<<< HEAD

=======
>>>>>>> 3c0131d1077b2cb831ff388a03bca1286dc22b33
    def update(self):
        # Двигаемся между left_x и right_x
        if self.rect.x <= self.left_x:
            self.direction = 'right'
        elif self.rect.x >= self.right_x:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        # Пытаемся выстрелить
        self.shoot()


# Создаём 4-х врагов и добавляем в одну группу
enemy_1 = Enemy('enemy_ship_1.png', 50, 50, 200, 375, 65, 200)
enemy_2 = Enemy('enemy_ship_2.png', 50, 50, 200,   0, 200, 325)
enemy_3 = Enemy('enemy_ship_3.png', 50, 50, 315, 375, 315, 440)
enemy_4 = Enemy('enemy_ship_4.png', 50, 50, 550,   0, 435, 590)

enemies = sprite.Group()
enemies.add(enemy_1, enemy_2, enemy_3, enemy_4)


# --- Переменные состояния игры ---
enemy_4_killed = False
finish         = False


# --- Шрифты и титулы победы/поражения ---
font.init()
big_font    = font.SysFont('Arial', 100)
win_title   = big_font.render('Ты выиграл!', True, (0, 255, 0))
loss_title  = big_font.render('Ты проиграл!', True, (255, 0, 0))
win_bg      = transform.scale(image.load('win.png'), (700, 500))


# --- Основной игровой цикл ---
run = True
while run:
    # --- Обработка событий ---
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key in (K_UP, K_w):
                player.y_speed = -5
            elif e.key in (K_DOWN, K_s):
                player.y_speed = 5
            elif e.key in (K_LEFT, K_a):
                player.x_speed = -5
            elif e.key in (K_RIGHT, K_d):
                player.x_speed = 5
            elif e.key == K_SPACE:
                player.fire()

        elif e.type == KEYUP:
            if e.key in (K_UP, K_w, K_DOWN, K_s):
                player.y_speed = 0
            elif e.key in (K_LEFT, K_a, K_RIGHT, K_d):
                player.x_speed = 0

    if not finish:
        # 1) Заливаем фон
        window.blit(background, (0, 0))

        # 2) Если четвёртый враг убит → рисуем ключ (только если он ещё существует)
        if enemy_4_killed and key.alive():
            key.reset()

        # 3) Рисуем остальные объекты
        player.reset()
        island.reset()
        treasure.reset()
        start_arch.reset()
        finish_arch.reset()
        barriers.draw(window)
        arrows.draw(window)
        enemies.draw(window)
        weapons.draw(window)
        enemy_weapons.draw(window)

        # 4) Проверяем, столкнулся ли игрок с сокровищем
        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win_bg, (0, 0))
            window.blit(win_title, (105, -20))

        # 5) Проверяем, столкнулся ли игрок с любым врагом
        if sprite.spritecollide(player, enemies, False):
            finish = True
            window.blit(background, (0, 0))
            loss.reset()
            window.blit(loss_title, (100, 350))

        # 6) Проверяем, не попал ли в игрока вражеский снаряд
        if sprite.spritecollide(player, enemy_weapons, False):
            finish = True
            window.blit(background, (0, 0))
            loss.reset()
            window.blit(loss_title, (100, 350))

        # 7) Обработка попаданий по врагам:
        #    Сначала проверяем попадание по 4-му врагу (чтобы гарантированно отработать этот кейс)
        if not enemy_4_killed:
            hit_enemy_4 = sprite.groupcollide(weapons, sprite.Group(enemy_4), True, True)
            if hit_enemy_4:
                enemy_4_killed = True
                print('Попадание в 4-го врага → ключ активирован')

        #    Затем обрабатываем попадания по остальным врагам
        #    (если enemy_4 уже убит, он автоматически убран из группы enemies)
        hit_other = sprite.groupcollide(weapons, enemies, True, True)
        if hit_other:
            # Можете добавить звук или эффект уничтожения врага здесь
            pass

        # 8) Проверяем, подобрал ли игрок ключ (после отрисовки, но при условии, что ключ ещё жив)
        if enemy_4_killed and key.alive() and sprite.collide_rect(player, key):
            key.kill()
            print('Игрок подобрал ключ')

    # --- Обновляем позиции всех подвижных спрайтов ---
    player.update()
    enemies.update()
    weapons.update()
    enemy_weapons.update()

    # --- Обновляем экран и задержка ---
    display.update()
    clock.tick(20)  # примерно 20 кадров в секунду (каждые ~50 мс)

# --- Завершение работы Pygame ---
quit()
