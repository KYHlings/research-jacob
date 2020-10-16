import pygame

#Skapar en klass som heter Menu
class Menu():
    def __init__(self, game):
        # Sätter game objektet till self.game
        self.game = game
        # Variabler för att göra så att menyn hamnar mitt på skärmen
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        # Skapar en bool-variabel.
        self.run_display = True
        # Skapar en rektangel för markören av de olika menyvalen
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        # skapar en variabel som är -100 för att skjuta markören till vänster
        self.offset = - 100

    def draw_cursor(self):
        # Använder draw_text funktionen från Game() och ritar ut markören
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        #  Skapar en funktion som först visar canvas, sen uppdaterar displayen och sen resettar keys från reset_keys funktionen i Game
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

#Skapar en klass för huvudmenyn där alla menyer ska samlas
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        # Sätter en startposition för game state
        self.state = "Start"
        # Sätter position för alla rektanglar
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        # Gör så att markören startar bredvid startrektangeln
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        # Skapar en bool-variabel just in case
        self.run_display = True
        # Om self.run_display är True:
        while self.run_display:
            # Kallar på check_events från Game klassen
            self.game.check_events()
            # Kallar på check_input funktionen
            self.check_input()
            # Kallar på diplay.fill och färgen BLACK från Game klassen
            self.game.display.fill(self.game.BLACK)
            # Skriver ut alla strängar som ska synas på skrämen.
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            # Ritar ut markören
            self.draw_cursor()
            # Gör så att det visas på skärmen
            self.blit_screen()


    def move_cursor(self):
        # Bestämmer var markören ska vara när man trycker på DOWN
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        # Bestämmer var markören ska vara när man trycker på UP
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

#Skapar klassen för Options menyn och hämtar inställningar för skärmen från Menu klassen (kanske)
class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        # Gör så att markören startar på volume (Se klassen MainMenu)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by Ajvar', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
