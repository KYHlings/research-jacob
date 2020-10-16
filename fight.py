import pygame
import os
from ROB.main_menu import main_menu
from ROB.lobby import lobby

class Window():
    def __init__(self):
        self.fps = pygame.time.Clock()
        self.screen_w = 800
        self.screen_h = 600
        self.black = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        self.bg_image = pygame.image.load('pics//arena_bakgrund_0.png')
        self.center_window = os.environ["SDL_VIDEO_CENTERED"] = "1"

# ljudeffekter
    def sounds(self):
        self.punch = pygame.mixer.Sound('music//PUNCH.wav')
        self.dead = pygame.mixer.Sound('music//Wilhelm_Scream.ogg')
        self.kick = pygame.mixer.Sound('music//KICK.wav')

    def blit(self):
        self.canvas = self.screen.blit()


# pygame.init()
# pygame.image.load('pics//arena_bakgrund_1.png')]
# fps = 120

# TODO loopa bakrundsbilderna
# screen.blit(bg_image[0], (0, 0))
# screen.blit(bg_image[1], (0, 0))


class Player(pygame.sprite.Sprite, Window):
    """
    Spawn a player
    """

    def __init__(self):
        Window.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        # how many pixels the character is moving per action
        self.vel = 5
        self.frame = 0
        # stating left and right
        self.left = False
        self.right = False
        self.rect = (0, 0, 0, 0)
        self.images = []
        self.image = [pygame.image.load("pics//walking_right_2.png")]
        self.hp = 100


    def player1_pics(self):
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(self.black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.player1.image = pygame.transform.flip(self.player1.images[self.player1.frame], True, False)

    def spawn_player(self):

        # spawnar spelare
        self.player1 = Player()
        self.player1_pics()
        self.player1.rect.x = 720
        self.player1.rect.y = 200
        self.player2 = Player()
        self.player1_pics()
        self.player2.rect.x = 60
        self.player2.rect.y = 200


        # lägger alla spelare i en sprite grupp
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.player1, self.player2)

    def collision(self):
        # kollar om kollision har skett
        col = pygame.sprite.collide_rect(self.player1, self.player2)
        if col == True:
            return True


    def player_movement(self, player1, player2):
        # Grund inställningar för position
        self.player1.rect.y += self.player1.vel
        self.player2.rect.y += self.player2.vel
        if self.player1.rect.y == 500:
            self.player1.vel = 0
        if self.player2.rect.y == 500:
            self.player2.vel = 0
        self.keys = pygame.key.get_pressed()
        for self.keys in pygame.event.get():
            if self.keys.type == pygame.QUIT:
                running = False


    # TODO det finns en bug där man flyger utanför skärmen om spelarna kolliderar och går åt ett håll tillsammans
    # FIGHTER 1
        # vänster
        if self.keys[pygame.K_LEFT] and self.player1.rect.x > self.player1.vel:
            self.player1.left = True
            self.player1.right = False
            if self.collision() == True:
                if self.player1.left == True:
                    self.player1.rect.x += 5
            self.player1.rect.x -= 1
            self.player1.image = pygame.transform.flip(self.player1.images[self.player1.frame], True, False)
            self.player1.frame += 1
            if self.player1.frame == 2:
                self.player1.frame = 0

        # höger
        if self.keys[pygame.K_RIGHT] and self.player1.rect.x < self.screen.w - 40:
            self.player1.left = False
            self.player1.right = True
            if self.collision() == True:
                if self.player1.right == True:
                    self.player1.rect.x -= 5
            self.player1.rect.x += 1
            self.player1.frame += 1
            if self.player1.frame == 2:
                self.player1.frame = 0
            self.player1.image = self.player1.images[self.player1.frame]

    # HOPP
        if self.keys[pygame.K_RCTRL]:
            # hoppets höjd
            self.player1.rect.y -= 15
            # dragningskraft
            self.player1.vel = 3
            # invisible border max hopphöjd
            if self.player1.rect.y < 200:
                self.player1.vel = 20
            # lägsta punkt
        if self.player1.rect.y > 500:
            self.player1.rect.y = 500

    # FIGTER 2
        # vänster
        if self.keys[pygame.K_a] and self.player2.rect.x > self.player2.vel:
            self.player2.left = True
            self.player2.right = False
            if self.collision() == True:
                if self.player2.left == True:
                    self.player2.rect.x += 5
            self.player2.rect.x -= 1
            self.player2.image = pygame.transform.flip(self.player2.images[self.player2.frame], True, False)
            self.player2.frame += 1
            if self.player2.frame == 2:
                self.player2.frame = 0

        # höger
        if self.keys[pygame.K_d] and self.player2.rect.x < self.screen_w - 40:
            self.player2.left = False
            self.player2.right = True
            if self.collision() == True:
                if self.player2.right == True:
                    self.player2.rect.x -= 5
            self.player2.rect.x += 1
            self.player2.frame += 1
            if self.player2.frame == 2:
                self.player2.frame = 0
            self.player2.image = self.player2.images[self.player2.frame]

    # HOPP
        if self.keys[pygame.K_SPACE]:
            # hoppets höjd
            self.player2.rect.y -= 15
            # dragningskraft
            self.player2.vel = 3
            # invisible border max hopphöjd
            if self.player2.rect.y < 200:
                self.player2.vel = 20
        # lägsta punkt
        if self.player2.rect.y > 500:
            self.player2.rect.y = 500
#
# def healthbar():
#     w = Window()
#     p = Player()
#     if p.player1.hp > -10:
#         bg_bar1 = pygame.Rect(550, 50, 200, 50)
#         hp_bar1 = pygame.Rect(550, 50, 200*(p.player1.hp*0.01), 50)
#         pygame.draw.rect(w.screen, (255, 0, 0), bg_bar1)
#         pygame.draw.rect(w.screen, (0, 255, 0), hp_bar1)
#
#     if p.player2.hp > -10:
#         bg_bar2 = pygame.Rect(50, 50, 200, 50)
#         hp_bar2 = pygame.Rect(50, 50, 200*(p.player2.hp*0.01), 50)
#         pygame.draw.rect(w.screen, (255, 0, 0), bg_bar2)
#         pygame.draw.rect(w.screen, (0, 255, 0), hp_bar2)
#     pygame.display.update()




# run order
main_menu()
lobby()
pygame.mixer.music.stop()
pygame.mixer.music.load('music//fight_music.ogg')
pygame.mixer.music.play(-1)


def punch_and_kick(Player):
    p = Player()
    # kollar om en knapp är nedtryckt
    if p.keys.type == pygame.KEYDOWN:

        # fighter1 slag och spark
        if p.keys.key == pygame.K_w:
            if p.collision(p.player1, p.player2) == True:
                p.effect_punch.play(0)
                print("slag")
                p.player2.hp -= 10
                print(f"HP PLAYER 2: {p.player2.hp}")

        if p.keys.key == pygame.K_s:
            if p.collision(p.player2, p.player2) == True:
                print("spark")
                p.effect_KICK.play(0)
                p.player2.hp -= 10
                print(f"HP PLAYER 2: {p.player2.hp}")

        # fighter2 slag och spark
        if p.keys.key == pygame.K_UP:
            if p.collision(p.player1, p.player2) == True:
                p.effect_punch.play(0)
                print("slag")
                p.player1.hp -= 10
                print(f"HP PLAYER 1: {p.player1.hp}")
        if p.keys.key == pygame.K_DOWN:
            if p.collision(p.player1, p.player2) == True:
                print("spark")
                p.effect_kick.play(0)
                p.player1.hp -= 10
                print(f"HP PLAYER 1: {p.player1.hp}")

    player_dead()
def player_dead():
    p = Player()
    w = Window()
    dead = pygame.image.load("pics//player_dead.png")
    if p.player2.hp == 0:
        w.screen.blit(dead)
        p.dead.play(0)

p = Player()
w = Window()
running = True
while running:
    Window()
    Player()
  #  punch_and_kick(Player)


