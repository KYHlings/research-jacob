# Importerar klassen Game från test.py
from test import Game

# Sätter variabeln "g" för klassen Game()
g = Game()

# När g körs:
while g.running:
	# Från Game hämtar vi current display. Visar nuvarande skärm, vilken ändras under programmets gång.
	g.curr_menu.display_menu()
	# Från Game hämtar vi metoden game_loop
	g.game_loop()