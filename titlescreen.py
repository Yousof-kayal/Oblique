import pygame as pg

class TitleScreen():
    def __init__(self,oblique):
        """
        Initializing Title Screen Class

        Args:
            oblique (file): Contains "TheGame" Class, inheriting the contents
        """
        self.oblique = oblique

        #initializing run_display flag, and initializing selection to "Start"
        self.run_display = True
        self.selection = "Start"

        self.startx, self.starty = self.oblique.mid_WIDTH, self.oblique.mid_HEIGHT + 50
        self.creditsx, self.creditsy = self.oblique.mid_WIDTH, self.oblique.mid_HEIGHT + 95
        self.exitx, self.exity = self.oblique.mid_WIDTH, self.oblique.mid_HEIGHT + 135

        #initializing container for cursor, with offset 150 points to the left 
        self.cursor_rect = pg.Rect(0,0,45,45)
        self.offset = - 150
        #Calibrating cursor to selection -> "Start"
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        
    
    def blit_screen(self):
        self.oblique.window.blit(self.oblique.display,(0,0))
        pg.display.update()
        self.oblique.reset_key()

    def display(self):
        self.run_display = True
        while self.run_display:
            self.oblique.listen_event()
            self.listen_start()
            self.oblique.display.fill(self.oblique.black)

            self.oblique.render_text("Oblique", 200, self.oblique.menu_font, self.oblique.white, self.oblique.mid_WIDTH, self.oblique.mid_HEIGHT-100)
            self.oblique.render_text("Start Game", 60, self.oblique.menu_font, self.oblique.white, self.startx, self.starty)
            self.oblique.render_text("Credits", 60, self.oblique.menu_font, self.oblique.white, self.creditsx, self.creditsy)
            self.oblique.render_text("Exit", 60, self.oblique.menu_font, self.oblique.white, self.exitx, self.exity)

            #cursor creation using the create text method
            self.oblique.render_text('O', 40, self.oblique.menu_font, self.oblique.magenta, self.cursor_rect.x, self.cursor_rect.y)
            self.blit_screen()
    
    def move_cursor(self):
        """
        Funtion that moves cursor in accordance to 'up' and 'down' inputs
        """
        if self.oblique.down_KEY:
            if self.selection == "Start":
                self.cursor_rect.midtop = (self.creditsx + self.offset+50, self.creditsy)
                self.selection = "Credits"
            elif self.selection == "Credits":
                self.cursor_rect.midtop = (self.exitx + self.offset+90, self.exity)
                self.selection = "Exit"
            elif self.selection == "Exit":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.selection = "Start"

        if self.oblique.up_KEY:
            if self.selection == "Start":
                self.cursor_rect.midtop = (self.exitx + self.offset+90, self.exity)
                self.selection = "Exit"
            elif self.selection == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.selection = "Start"
            elif self.selection == "Exit":
                self.cursor_rect.midtop = (self.creditsx + self.offset+50, self.creditsy)
                self.selection = "Credits"
        
    
    def listen_start(self):
        """
        Listens for user input of "start" button. Depending on self.selection value, opens corresponding menu.
        """
        self.move_cursor()
        if self.oblique.start_KEY:
            if self.selection == "Start":
                self.oblique.start = True
            elif self.selection == "Credits":
                self.oblique.current_menu = self.oblique.credits
            elif self.selection == "Exit":
                self.oblique.running, self.oblique.start = False, False
            self.run_display= False
                
class Credits(TitleScreen):
    def __init__(self, oblique):
        self.oblique = oblique
        self.run_display = True

    def display(self):
        self.run_display = True
        while self.run_display:
            self.oblique.listen_event()
            if self.oblique.back_KEY or self.oblique.start_KEY:
                self.oblique.current_menu = self.oblique.title_screen
                self.run_display = False
            self.oblique.display.fill(self.oblique.black)
            self.oblique.render_text('Credits', 100, self.oblique.menu_font, self.oblique.white, self.oblique.mid_WIDTH, self.oblique.mid_HEIGHT - 20)
            self.oblique.render_text('By Yousof Kayal', 50, self.oblique.menu_font, self.oblique.magenta, self.oblique.mid_WIDTH, self.oblique.mid_HEIGHT +40)
            self.blit_screen()

