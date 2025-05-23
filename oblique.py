import pygame as pg
from titlescreen import TitleScreen, Credits
from story import create_oblique_story

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
        
        self.menu_font = 'assets/PoppkornRegular-MzKY.ttf'
        self.game_font = 'assets/PressStart2P-vaV7.ttf'
        
        # Create the story tree
        self.story_tree = create_oblique_story(self)
        
        # Initialize title screen and credits
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
                self.story_tree.reset()  # Reset story when exiting game

            self.display.fill(self.black)
            
            # Process user input for story navigation
            if self.up_KEY:
                self.story_tree.move_selection_up()
            elif self.down_KEY:
                self.story_tree.move_selection_down()
            elif self.start_KEY:
                self.story_tree.make_choice()
            
            # Get current node text and render it
            self.render_story_node()
            
            # Render choices
            self.render_choices()
            
            self.window.blit(self.display,(0,0))
            pg.display.update()

            self.reset_key()
    
    def render_story_node(self):
        """
        Render the text of the current story node
        """
        text = self.story_tree.get_current_text()
        color = self.story_tree.get_node_color() or self.white
        font_size = self.story_tree.get_node_font_size() or 15
        
        # Split text by newline and render each line
        lines = text.split('\n')
        y_pos = 100
        for line in lines:
            if line:  # Only render non-empty lines
                self.render_text(line, font_size, self.game_font, color, self.mid_WIDTH, y_pos)
                y_pos += 30
    
    def render_choices(self):
        """
        Render the available choices with keyboard selection
        """
        choices = self.story_tree.get_current_choices()
        if not choices:
            # End node, show return option
            self.render_text("Press ESC to return to title screen", 15, self.game_font, 
                            self.white, self.mid_WIDTH, self.display_HEIGHT - 100)
            return
        
        y_pos = self.display_HEIGHT - 150
        for i, choice in enumerate(choices):
            # Determine color based on selection
            color = self.magenta if i == self.story_tree.selection_index else self.white
            
            # Render choice text with cursor for selected item
            prefix = "► " if i == self.story_tree.selection_index else "  "
            choice_text = f"{prefix}{choice}"
            self.render_text(choice_text, 15, self.game_font, color, self.mid_WIDTH, y_pos)
            y_pos += 30

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