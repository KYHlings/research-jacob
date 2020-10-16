from test_menu import *


class Game():
    def __init__(self):
        # Startar upp pygame
        pygame.init()
        # Sätter variabler som kommer bestämma om man spelar eller inte
        self.running, self.playing = True, False
        # Sätter variabler för tangenterna UP, DOWN, START och BACK
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        # Sätter storleken på fönstret
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        # Målar ut en bild som är lika stor som fönstret
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        # Skapar spelfönstret med storleken som defineras på rad 13
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        # Sätter en Font på texten
        self.font_name = '8-BIT WONDER.TTF'
        #self.font_name = pygame.font.get_default_font()
        # Lägger variabler för färgerna svart och vit
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        # Sätter variabel för klassen MainMenu, OptionsMenu och CreditsMenu så att man ska kunna ändra mellan game states
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        # Sätter current menu till main_menu (denna ändras senare)
        self.curr_menu = self.main_menu

    def game_loop(self):
        # Medan playing är True:
        while self.playing:
            # Kollar knapptryckningar med hjälp av funktionen check_events på rad 51
            self.check_events()
            # Om man trycker på enter så sätts variabeln playing till False och man kommer tillbaka till huvudmenyn
            if self.START_KEY:
                self.playing= False
            # Fyller skärmen med svart färg.
            self.display.fill(self.BLACK)
            # Skriver ut "Thanks for playing" mitt i rutan med storlek 20.
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            # Gör så att texten syns ovanpå Surface
            self.window.blit(self.display, (0,0))
            # Uppdaterar skärmbilden
            pygame.display.update()
            # Gör UP, DOWN, START och BACK False igen med hjälp av reset_keys funktionen på rad 66
            self.reset_keys()


    # Hela funktionen kollar knapptryckningar
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    # Funktion för att rita saker, grundinställningar för alla textrektanglar
    # Som indata tar vi text(sträng), font storlek, koordinaterna för rektangelns x och y värde.
    def draw_text(self, text, size, x, y ):
        # Bestämmer fontstorleken
        font = pygame.font.Font(self.font_name,size)
        # Gör så att texten laddas in men den dyker inte upp förrän vi 'blit'ar displayen på rad 79
        text_surface = font.render(text, True, self.WHITE)
        # Denna tar texten och storleken och gör det spacet till en rektangel
        text_rect = text_surface.get_rect()
        # Sätter x och y koordinaterna av rektangeln i mitten av rektangeln istället för i övre vänstra hörnet
        text_rect.center = (x,y)
        # Visar texten som vi har skrivit på skärmen
        self.display.blit(text_surface,text_rect)






