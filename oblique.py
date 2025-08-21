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
                if self.story_tree.is_end_node():
                    # If at an ending, return to title screen
                    self.start = False
                    self.story_tree.reset()
                    self.current_menu = self.title_screen
                else:
                    # Otherwise just exit to title screen
                    self.start = False
                    self.story_tree.reset()

            self.display.fill(self.black)
            
            # Process user input for story navigation
            if self.up_KEY:
                self.story_tree.move_selection_up()
            elif self.down_KEY:
                self.story_tree.move_selection_down()
            elif self.start_KEY:
                if self.story_tree.is_end_node():
                    # If at an ending, return to title screen
                    self.start = False
                    self.story_tree.reset()
                    self.current_menu = self.title_screen
                else:
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
        Render the text of the current story node with line-based coloring
        """
        if not self.story_tree.current_node:
            return
        
        text = self.story_tree.get_current_text()
        font_size = self.story_tree.get_node_font_size() or 15
        
        # Split text by newline and render each line with appropriate color
        lines = text.split('\n')
        y_pos = 100
        for line in lines:
            if line:  # Only render non-empty lines
                # Determine color based on line content
                line_color = self.white  # Default neutral
                line_lower = line.lower()
                
                # Crimson for danger/shock content
                if any(word in line_lower for word in ['kill', 'death', 'die', 'blood', 'strike', 'vital organ', 'fall', 'creature', 'grab', 'decaying', 'crimson', 'shatter', 'darkness', 'evacuated', 'breach', 'alarms', 'warning', 'impossible', 'abandoned', 'frozen']):
                    line_color = self.crimson
                # Magenta for important information
                elif any(word in line_lower for word in ['project oblique', 'tubes', 'hospital', 'empty', 'circles', 'shadows', 'figures', 'police', 'report', 'containment', 'cure', 'immortality', 'researcher', 'memories', 'terminal', 'protocol', 'subject', 'partition', 'consciousness', 'versions', 'reflection', 'badges']):
                    line_color = self.magenta
                
                self.render_text(line, font_size, self.game_font, line_color, self.mid_WIDTH, y_pos)
                y_pos += 30
    
    def render_choices(self):
        """
        Render the available choices with keyboard selection using square cursor
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
            
            # Calculate text width to position cursor dynamically
            choice_font = pg.font.Font(self.game_font, 15)
            text_width = choice_font.size(choice)[0]
            cursor_x = self.mid_WIDTH - (text_width // 2) - 30  # 30 pixels to the left of text
            
            # Render choice text
            self.render_text(choice, 15, self.game_font, color, self.mid_WIDTH, y_pos)
            
            # Render square cursor for selected item
            if i == self.story_tree.selection_index:
                self.render_text('O', 20, self.menu_font, self.magenta, cursor_x, y_pos)
            
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
    if ob.start:  # Only run main game loop when game is started
        ob.main_loop()