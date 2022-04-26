import pygame as pg
from mainmenu import MainMenu, Credits

class TheGame():
    def __init__(self):
        """
        Initializing the window, flags, the clock, and keystrokes for The Game Class
        """
        pg.init()
        pg.display.set_caption('OBLIQUE by YOUSOF KAYAL')
        icon = pg.image.load("assets/icon.png")
        pg.display.set_icon(icon)
        self.running, self.start = True, False
        self.up_KEY, self.down_KEY, self.start_KEY, self.back_KEY = False, False, False, False

        self.display_WIDTH, self.display_HEIGHT = 1280, 720
        self.mid_WIDTH, self.mid_HEIGHT = self.display_WIDTH/2, self.display_HEIGHT/2

        self.display = pg.Surface((self.display_WIDTH,self.display_HEIGHT))
        self.window = pg.display.set_mode(((self.display_WIDTH,self.display_HEIGHT)))
        self.black, self.white, self.magenta, self.crimson = (0,0,0), (255,255,255), (90,35,175), (87,15,20)

        self.user_text = ''
        
        self.menu_font = 'assets/PoppkornRegular-MzKY.ttf'
        self.game_font = 'assets/PressStart2P-vaV7.ttf'
        
        self.main_menu = MainMenu(self)
        self.credits = Credits(self)
        self.current_menu = MainMenu(self)


    def main_loop(self): 
        """
        The game loop, this is where the actual game lives.
        """
        while self.start:
            self.listen_event()

            if self.back_KEY:
                self.start = False
                self.user_text = ''

            self.display.fill(self.black)
            
            self.render_text(self.user_text, 15 ,self.game_font, self.white, self.mid_WIDTH, self.mid_HEIGHT+200)

            #No input output
            if self.user_text == "":
                self.render_text("You wake up in a hospital bed...", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Looking around to the left and right, you are all alone.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("Press 1 to Continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            #intro sequence
            if self.user_text == "1":
                self.render_text("There are tubes connected into your skin.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("You pull them out, and get out of the bed.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("The hospital is empty... Do you find a way out, or explore?", 20, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("Press 1 to explore, press 2 to leave", 15, self.game_font, self.white, self.mid_WIDTH, 400)
            
            #explore start branch: 11     
            if self.user_text == "11":
                self.render_text("You follow the exit signs scattered all over.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("As you continue to search for a way out, you notice something.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("You've been going in circles", 20, self.game_font, self.magenta, self.mid_WIDTH, 170)
                self.render_text("You pause, take a deep breath, and think of two solutions:", 15, self.game_font, self.white, self.mid_WIDTH, 210)
                self.render_text("Ignore the signs and explore, or find a window.", 15, self.game_font, self.white, self.mid_WIDTH, 240)
                self.render_text("Press 1 explore, 2 to search for a window. ", 15, self.game_font, self.white, self.mid_WIDTH, 400)
            
            if self.user_text == "111":
                self.render_text("You wander aimlessly for hours, nothing seems to catch your attention.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Everything looks the same.", 20, self.game_font, self.magenta, self.mid_WIDTH, 140)
                self.render_text("The floors, ceilings, doors, walls. They all look the same.", 15, self.game_font, self.white, self.mid_WIDTH, 180)
                self.render_text("The thought keeps popping up in your mind.", 15, self.game_font, self.white, self.mid_WIDTH, 210)
                self.render_text("'How long have I been here? Is this the rest of my life?'", 15, self.game_font, self.white, self.mid_WIDTH, 240)
                self.render_text("You realize that if you stay any longer, you will be driven to insanity.", 15, self.game_font, self.white, self.mid_WIDTH, 270)
                self.render_text("Press 1 to keep wandering, 2 to go back and rest.", 15, self.game_font, self.white, self.mid_WIDTH, 400)
            
            if self.user_text == "1111":
                self.render_text("Your eyes are starting to fool you.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Things that previously weren't there are appearing.", 15, self.game_font, self.magenta, self.mid_WIDTH, 130)
                self.render_text("Shadowy figures zip around your surroundings.", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("You assume that they are just hallucinations", 15, self.game_font, self.white, self.mid_WIDTH, 190)
                self.render_text("But they are real...", 20, self.game_font, self.crimson, self.mid_WIDTH, 230)
                self.render_text("You have to fight, there is no way out.", 15, self.game_font, self.white, self.mid_WIDTH, 270)
                self.render_text("Press 1 fight. ", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                
            if self.user_text == "11111":
                self.render_text("You are weak, and frail", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("But nonetheless, you try to fight back.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("The shadowy figures zip left and right", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("With no effort, they strike a vital organ and watch you fall to the ground.", 15, self.game_font, self.white, self.mid_WIDTH, 190)
                self.render_text("You died. Game Over", 25, self.game_font, self.crimson, self.mid_WIDTH, 230)
                
            
            #search for a window: 112
            if self.user_text == "112":
                self.render_text("You remember there was a window in the room you woke up in and backtrack.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("You find the room and casually walk towards it.", 15, self.game_font, self.white, self.mid_WIDTH, 120)
                self.render_text("You look out the window and find yourself on a relatively low floor.", 15, self.game_font, self.white, self.mid_WIDTH, 150)
                self.render_text("A fall from here would still kill you.", 20, self.game_font, self.crimson, self.mid_WIDTH, 190)
                self.render_text("After close inspection of the window, you find the lock has been opened already.", 15, self.game_font, self.white, self.mid_WIDTH, 230)
                self.render_text("You open the window and start climbing down.", 15, self.game_font, self.white, self.mid_WIDTH, 260)
                self.render_text("You smell something disgusting behind you...", 15, self.game_font, self.white, self.mid_WIDTH, 290)
                self.render_text("Press 1 to continue.", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                
            if self.user_text == "1121":
                self.render_text("Curious, you look behind you. ", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("You are met with a creature with three arms and two legs with a decaying body.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("It tries to grab you, but you jump onto a trash container.", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("You live for another day", 20, self.game_font, self.magenta, self.mid_WIDTH, 200)
                self.render_text("Press 1 to continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                
            
            #Go back and rest: 1112
            if self.user_text == "1112":
                self.render_text("You wander aimlessly for hours, nothing seems to catch your attention.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Everything looks the same.", 20, self.game_font, self.magenta, self.mid_WIDTH, 140)
                self.render_text("The floors, ceilings, doors, walls. They all look the same.", 15, self.game_font, self.white, self.mid_WIDTH, 180)
                self.render_text("The thought keeps popping up in your mind.", 15, self.game_font, self.white, self.mid_WIDTH, 210)
                self.render_text("'How long have I been here? Is this the rest of my life?'", 15, self.game_font, self.white, self.mid_WIDTH, 240)
                self.render_text("You realize that if you stay any longer, you will be driven to insanity.", 15, self.game_font, self.white, self.mid_WIDTH, 270)
                self.render_text("Press 1 to keep wandering, 2 to go back and rest.", 15, self.game_font, self.white, self.mid_WIDTH, 400)
            
            #leave start branch: 12
            if self.user_text == "12":
                self.render_text("You find a window in the same room you woke up in.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("The sky has a slight crimson tint.", 15, self.game_font, self.crimson, self.mid_WIDTH, 140)
                self.render_text("Your head is fuzzy and you don't know how you got here.", 15, self.game_font, self.white, self.mid_WIDTH, 170)
                self.render_text("After close inspection of the window, you find that it is locked by a padlock. ", 15, self.game_font, self.white, self.mid_WIDTH, 200)
                self.render_text("You feel confident in your ability in breaking the glass though.", 15, self.game_font, self.white, self.mid_WIDTH, 230)
                self.render_text("Break it? Press 1 for yes, press 2 for no.", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                 
            if self.user_text == "122":
                self.render_text("Level 1 Please enter you name", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("welcome to level 1", 15, self.game_font, self.white, self.mid_WIDTH, 120)
                self.render_text("Press N to continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                 
            
            if self.user_text == "121":
                self.render_text("Level 1 Please enter you name", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("welcome to level 1", 15, self.game_font, self.white, self.mid_WIDTH, 120)
                self.render_text("Press N to continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                
                
            if self.user_text == "1221":
                self.render_text("Level 1 Please enter you name", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("welcome to level 1", 15, self.game_font, self.white, self.mid_WIDTH, 120)
                self.render_text("Press N to continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                
                
            if self.user_text == "1222":
                self.render_text("Level 1 Please enter you name", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("welcome to level 1", 15, self.game_font, self.white, self.mid_WIDTH, 120)
                self.render_text("Press N to continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                
           
            self.window.blit(self.display,(0,0))
            pg.display.update()

            self.reset_key()

    def listen_event(self):
        """
        Function that is checking for user inputs
        """
        for event in pg.event.get():
            #exit game through "x" button
            if event.type == pg.QUIT:
                self.running, self.start = False, False
                self.current_menu.run_display= False
                
            #tracking user input for menu traversal 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.start_KEY = True
                elif event.key == pg.K_ESCAPE:
                    self.back_KEY = True
                elif event.key == pg.K_DOWN:
                    self.down_KEY = True
                elif event.key == pg.K_UP:
                    self.up_KEY = True
                elif event.key == pg.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode
                    
                    
    def reset_key(self):
        """
        Reset user key presses
        """        
        self.start_KEY, self.back_KEY, self.down_KEY, self.up_KEY = False, False, False, False



    def render_text(self, text, size, font, color, x, y):
        """
        Rendering text in chosen font

        Args:
            text (String): The text that is being rendered
            size (Int): How large the text is
            font (String): What font to render
            color(Int): The color value for the rendered text
            x, y (Int): Where the text is located on the screen  
        """
        chosenfont = pg.font.Font(font,size)
        text_surface = chosenfont.render(text, True, color)
        render_rect = text_surface.get_rect()
        render_rect.center = (x, y)
        self.display.blit(text_surface,render_rect)


"""
Attributing "TheGame" class to a variable (ob) and the program loop
"""
ob = TheGame() 
while ob.running:
    ob.current_menu.display()
    ob.main_loop()
    