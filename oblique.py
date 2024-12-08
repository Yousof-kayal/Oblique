import pygame as pg
from titlescreen import TitleScreen, Credits

class TheGame():
    def __init__(self):
        """
        Initializing the window, flags, and keystrokes for The Game Class
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
        
        self.title_screen = TitleScreen(self)
        self.credits = Credits(self)
        self.current_menu = self.title_screen


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

           # Initial state
            if self.user_text == "":
                self.render_text("You wake up in a hospital bed...", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Looking around to the left and right, you are all alone.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("Press 1 to Continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            # First choice
            if self.user_text == "1":
                self.render_text("There are tubes connected into your skin.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("You pull them out, and get out of the bed.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("The hospital is empty... Do you find a way out, or explore?", 20, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("Press 1 to explore, press 2 to leave", 15, self.game_font, self.white, self.mid_WIDTH, 400)
            
            ### EXPLORE BRANCH (1) ###

            # Initial explore choice
            if self.user_text == "11":
                self.render_text("You follow the exit signs scattered all over.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("As you continue to search for a way out, you notice something.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("You've been going in circles", 20, self.game_font, self.magenta, self.mid_WIDTH, 170)
                self.render_text("You pause, take a deep breath, and think of two solutions:", 15, self.game_font, self.white, self.mid_WIDTH, 210)
                self.render_text("Ignore the signs and explore, or find a window.", 15, self.game_font, self.white, self.mid_WIDTH, 240)
                self.render_text("Press 1 explore, 2 to search for a window. ", 15, self.game_font, self.white, self.mid_WIDTH, 400)
            
            # Follow signs path
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
            
            #Go back and rest: 1112
            if self.user_text == "1112":
                self.render_text("You wander aimlessly for hours, nothing seems to catch your attention.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Everything looks the same.", 20, self.game_font, self.magenta, self.mid_WIDTH, 140)
                self.render_text("The floors, ceilings, doors, walls. They all look the same.", 15, self.game_font, self.white, self.mid_WIDTH, 180)
                self.render_text("The thought keeps popping up in your mind.", 15, self.game_font, self.white, self.mid_WIDTH, 210)
                self.render_text("'How long have I been here? Is this the rest of my life?'", 15, self.game_font, self.white, self.mid_WIDTH, 240)
                self.render_text("You realize that if you stay any longer, you will be driven to insanity.", 15, self.game_font, self.white, self.mid_WIDTH, 270)
                self.render_text("Press 1 to keep wandering, 2 to go back and rest.", 15, self.game_font, self.white, self.mid_WIDTH, 400)
            
            if self.user_text == "11121":
                self.render_text("Your eyes are starting to fool you.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Things that previously weren't there are appearing.", 15, self.game_font, self.magenta, self.mid_WIDTH, 130)
                self.render_text("Shadowy figures zip around your surroundings.", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("You assume that they are just hallucinations", 15, self.game_font, self.white, self.mid_WIDTH, 190)
                self.render_text("But they are real...", 20, self.game_font, self.crimson, self.mid_WIDTH, 230)
                self.render_text("You have to fight, there is no way out.", 15, self.game_font, self.white, self.mid_WIDTH, 270)
                self.render_text("Press 1 fight. ", 15, self.game_font, self.white, self.mid_WIDTH, 400)
                
            if self.user_text == "111211":
                self.render_text("You are weak, and frail", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("But nonetheless, you try to fight back.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("The shadowy figures zip left and right", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("With no effort, they strike a vital organ and watch you fall to the ground.", 15, self.game_font, self.white, self.mid_WIDTH, 190)
                self.render_text("You died. Game Over", 25, self.game_font, self.crimson, self.mid_WIDTH, 230)
            
            #Find window path
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
                self.render_text("But something feels wrong about your escape...", 15, self.game_font, self.crimson, self.mid_WIDTH, 230)
                self.render_text("Press 1 to continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            if self.user_text == "11211":
                self.render_text("As you run through the empty streets, you notice there are no cars.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("No people. No sounds. Just emptiness.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("You find a police station and decide to investigate.", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("Press 1 to enter, 2 to keep searching the city", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            if self.user_text == "112111":
                self.render_text("Inside, you find a detailed report about a containment breach.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Project OBLIQUE: A failed attempt to cure death itself.", 15, self.game_font, self.magenta, self.mid_WIDTH, 130)
                self.render_text("The creatures are failed test subjects, you realize.", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("You hear footsteps approaching from behind...", 15, self.game_font, self.white, self.mid_WIDTH, 190)
                self.render_text("Press 1 to turn around", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            if self.user_text == "1121111":
                self.render_text("It's a police officer! Finally, someone normal!", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("He explains that the city has been evacuated.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("You're being taken to a safe zone.", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("Press 1 to go with the officer", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            # True climax and cliffhanger
            if self.user_text == "11211111":
                self.render_text("As you follow the officer, something catches your eye.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("His reflection in a window shows no face.", 15, self.game_font, self.crimson, self.mid_WIDTH, 130)
                self.render_text("You try to run, but more officers appear.", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("Their badges all read: PROJECT OBLIQUE", 20, self.game_font, self.magenta, self.mid_WIDTH, 190)
                self.render_text("'You weren't supposed to wake up yet.'", 15, self.game_font, self.white, self.mid_WIDTH, 220)
                self.render_text("Then you remember - you've seen this before.", 15, self.game_font, self.crimson, self.mid_WIDTH, 250)
                self.render_text("You've escaped this hospital exactly 47 times.", 15, self.game_font, self.magenta, self.mid_WIDTH, 280)
                self.render_text("And they're still testing...", 20, self.game_font, self.crimson, self.mid_WIDTH, 310)

            # Alternative branch from city exploration
            if self.user_text == "112112":
                self.render_text("The city seems frozen in time.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Store windows are dusty but intact.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("You find a newspaper dated 47 days ago:", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("'MIRACLE CURE PROMISES IMMORTALITY'", 20, self.game_font, self.magenta, self.mid_WIDTH, 190)            
               
            
            
            ### LEAVE BRANCH (2) ###
            if self.user_text == "12":
                self.render_text("You find a window in the same room you woke up in.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("The sky has a slight crimson tint.", 15, self.game_font, self.crimson, self.mid_WIDTH, 140)
                self.render_text("Your head is fuzzy and you don't know how you got here.", 15, self.game_font, self.white, self.mid_WIDTH, 170)
                self.render_text("After close inspection of the window, you find that it is locked by a padlock. ", 15, self.game_font, self.white, self.mid_WIDTH, 200)
                self.render_text("You feel confident in your ability in breaking the glass though.", 15, self.game_font, self.white, self.mid_WIDTH, 230)
                self.render_text("Break it? Press 1 for yes, press 2 for no.", 15, self.game_font, self.white, self.mid_WIDTH, 400)
            
            # Break window path
            if self.user_text == "121":
                self.render_text("The glass shatters easily - too easily.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("As you prepare to climb down, the floor beneath you creaks.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("Suddenly, the tiles give way and you fall into darkness...", 15, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("Press 1 to continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            if self.user_text == "1211":
                self.render_text("You wake up in an underground facility.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Emergency lights cast a red glow on sterile walls.", 15, self.game_font, self.crimson, self.mid_WIDTH, 130)
                self.render_text("Two tunnels stretch before you.", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("Press 1 for left tunnel, 2 for right tunnel", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            # Left tunnel - Medical bay
            if self.user_text == "12111":
                self.render_text("You find yourself in an abandoned medical bay.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Rows of empty tanks line the walls.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("A terminal flickers nearby, still operational.", 15, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("Subject Status Report: 47 iterations complete", 20, self.game_font, self.crimson, self.mid_WIDTH, 190)
                self.render_text("Press 1 to access subject records", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            # Right tunnel - Control room
            if self.user_text == "12112":
                self.render_text("The tunnel opens into a massive control room.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Dozens of monitors show hospital rooms identical to yours.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("Each screen shows a different version of you, making different choices.", 15, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("Some of you are already dead.", 20, self.game_font, self.crimson, self.mid_WIDTH, 190)
                self.render_text("Press 1 to check security feeds", 15, self.game_font, self.white, self.mid_WIDTH, 400)


            # Convergence point - True nature reveal
            if self.user_text == "121111" or self.user_text == "121121":
                self.render_text("Your memories flood back all at once.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("You're not a patient. You never were.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("You're the original researcher of Project OBLIQUE.", 15, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("The one who discovered that immortality had a price:", 20, self.game_font, self.crimson, self.mid_WIDTH, 190)
                self.render_text("The mind can't handle infinite existence.", 15, self.game_font, self.white, self.mid_WIDTH, 220)
                self.render_text("It creates loops. Safe spaces. Familiar scenarios.", 15, self.game_font, self.white, self.mid_WIDTH, 250)
                self.render_text("And now you're trapped in your own creation.", 20, self.game_font, self.crimson, self.mid_WIDTH, 280)
                self.render_text("Or are you? The answer lies in iteration 48...", 15, self.game_font, self.magenta, self.mid_WIDTH, 310)

            if self.user_text == "122":
                self.render_text("You decide against breaking the window - something feels off.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Looking closer at the padlock, you notice strange markings.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("They look like... dates? Each one crossed out.", 15, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("The most recent one is exactly 47 days ago.", 20, self.game_font, self.crimson, self.mid_WIDTH, 190)
                self.render_text("Press 1 to investigate the padlock, 2 to look for another exit", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            # Investigate padlock path
            if self.user_text == "1221":
                self.render_text("The padlock feels unusually warm to the touch.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("As you examine it, your finger catches on a hidden switch.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("Click.", 20, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("The wall beside the window begins to slide open...", 15, self.game_font, self.white, self.mid_WIDTH, 190)
                self.render_text("Press 1 to enter the hidden passage", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            if self.user_text == "12211":
                self.render_text("You step into what appears to be an observation room.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Through one-way glass, you can see your hospital room.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("But that's impossible - you just left that room.", 15, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("On the bed lies another you, still unconscious.", 20, self.game_font, self.crimson, self.mid_WIDTH, 190)
                self.render_text("A monitor beside the bed reads: 'Iteration 48 prepped'", 15, self.game_font, self.white, self.mid_WIDTH, 220)
                self.render_text("Press 1 to check the research terminal", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            if self.user_text == "122111":
                self.render_text("Project OBLIQUE - Memory Partition Test Results", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("Subject maintains consciousness across iterations", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("Success: Memory bleeding between partitions detected", 15, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("Warning: Subject showing signs of partition collapse", 20, self.game_font, self.crimson, self.mid_WIDTH, 190)
                self.render_text("All 47 memory partitions are becoming unstable", 15, self.game_font, self.white, self.mid_WIDTH, 220)
                self.render_text("Recommendation: Initiate Emergency Protocol WAKE", 15, self.game_font, self.white, self.mid_WIDTH, 250)
                self.render_text("Press 1 to initiate protocol", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            if self.user_text == "1221111":
                self.render_text("'WAKE protocol initiated'", 20, self.game_font, self.magenta, self.mid_WIDTH, 100)
                self.render_text("You hear alarms blaring throughout the facility.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("Through the glass, you watch as all 47 versions of you", 15, self.game_font, self.white, self.mid_WIDTH, 160)
                self.render_text("Begin to wake up simultaneously.", 15, self.game_font, self.white, self.mid_WIDTH, 190)
                self.render_text("'Memory partition collapse complete'", 20, self.game_font, self.crimson, self.mid_WIDTH, 220)
                self.render_text("'Congratulations, Doctor. The experiment was a success.'", 15, self.game_font, self.white, self.mid_WIDTH, 250)
                self.render_text("But which version of you are you really?", 20, self.game_font, self.magenta, self.mid_WIDTH, 280)
                self.render_text("Press 1 to continue", 15, self.game_font, self.white, self.mid_WIDTH, 400)

            # Look for another exit path
            if self.user_text == "1222":
                self.render_text("You turn away from the window to search elsewhere.", 15, self.game_font, self.white, self.mid_WIDTH, 100)
                self.render_text("The room suddenly feels different - older, abandoned.", 15, self.game_font, self.white, self.mid_WIDTH, 130)
                self.render_text("Dust covers everything, years worth of it.", 15, self.game_font, self.magenta, self.mid_WIDTH, 160)
                self.render_text("This isn't the same room you woke up in.", 20, self.game_font, self.crimson, self.mid_WIDTH, 190)
                self.render_text("Or rather - it is, but decades later.", 15, self.game_font, self.white, self.mid_WIDTH, 220)
                self.render_text("You've been here much longer than you thought.", 15, self.game_font, self.white, self.mid_WIDTH, 250)

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
    