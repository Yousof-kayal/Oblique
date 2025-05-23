import pygame as pg

class StoryNode:
    def __init__(self, text, font_size=15, color=None):
        """
        Initialize a story node
        
        Args:
            text (str): The story text to display
            font_size (int): Size of the font for this node
            color (tuple): RGB color tuple for this text (default: None, will use game's default)
        """
        self.text = text
        self.font_size = font_size
        self.color = color
        self.choices = []
        
    def add_choice(self, text, node):
        """
        Add a choice that leads to another node
        
        Args:
            text (str): The choice text
            node (StoryNode): The node this choice leads to
        """
        self.choices.append({"text": text, "node": node})
        return self  # Enable method chaining
        
class StoryTree:
    def __init__(self, game, root_node):
        """
        Initialize the story tree
        
        Args:
            game: Reference to the main game object
            root_node (StoryNode): The starting node of the story
        """
        self.game = game
        self.root = root_node
        self.current_node = root_node
        self.selection_index = 0  # Track which choice is currently selected
        
    def reset(self):
        """Reset to the beginning of the story"""
        self.current_node = self.root
        self.selection_index = 0
        
    def make_choice(self):
        """Make the currently selected choice"""
        if self.has_choices() and 0 <= self.selection_index < len(self.current_node.choices):
            self.current_node = self.current_node.choices[self.selection_index]["node"]
            self.selection_index = 0  # Reset selection for the new node
            return True
        return False
        
    def move_selection_up(self):
        """Move the selection cursor up"""
        if self.has_choices():
            self.selection_index = (self.selection_index - 1) % len(self.current_node.choices)
            
    def move_selection_down(self):
        """Move the selection cursor down"""
        if self.has_choices():
            self.selection_index = (self.selection_index + 1) % len(self.current_node.choices)
            
    def get_current_text(self):
        """Get the text of the current node"""
        return self.current_node.text
        
    def get_current_choices(self):
        """Get the available choices from the current node"""
        return [choice["text"] for choice in self.current_node.choices]
        
    def has_choices(self):
        """Check if the current node has any choices"""
        return len(self.current_node.choices) > 0
        
    def get_node_color(self):
        """Get the color for the current node's text"""
        return self.current_node.color if self.current_node.color else self.game.white
        
    def get_node_font_size(self):
        """Get the font size for the current node's text"""
        return self.current_node.font_size
        
    def is_end_node(self):
        """Check if this is an end node (no more choices)"""
        return not self.has_choices()

def create_oblique_story(game):
    """
    Create the story tree for Oblique
    
    Args:
        game: Reference to the main game object
        
    Returns:
        StoryTree: The complete story tree
    """
    # Define colors for easy access
    white = game.white
    magenta = game.magenta
    crimson = game.crimson
    
    # Starting node
    start = StoryNode("You wake up in a hospital bed...\n\nLooking around to the left and right, you are all alone.")
    start.add_choice("Continue", None)  # Placeholder, will set properly below
    
    # First choice node
    first_choice = StoryNode("There are tubes connected into your skin.\n\nYou pull them out, and get out of the bed.\n\nThe hospital is empty... Do you find a way out, or explore?", color=magenta)
    first_choice.add_choice("Explore the hospital", None)  # Placeholder
    first_choice.add_choice("Try to leave", None)  # Placeholder
    
    # Link start to first choice
    start.choices[0]["node"] = first_choice
    
    #=============== EXPLORE BRANCH ===============#
    
    # Initial explore choice
    explore_initial = StoryNode("You follow the exit signs scattered all over.\n\nAs you continue to search for a way out, you notice something.\n\nYou've been going in circles", color=magenta)
    explore_initial.add_choice("Ignore the signs and explore", None)  # Placeholder
    explore_initial.add_choice("Find a window", None)  # Placeholder
    
    # Set first branch choice
    first_choice.choices[0]["node"] = explore_initial
    
    # Follow signs path
    explore_follow_signs = StoryNode("You wander aimlessly for hours, nothing seems to catch your attention.\n\nEverything looks the same.", color=magenta)
    explore_follow_signs.add_choice("Keep wandering", None)  # Placeholder
    explore_follow_signs.add_choice("Go back and rest", None)  # Placeholder
    
    # Link from initial explore
    explore_initial.choices[0]["node"] = explore_follow_signs
    
    # Keep wandering path
    keep_wandering = StoryNode("Your eyes are starting to fool you.\n\nThings that previously weren't there are appearing.\n\nShadowy figures zip around your surroundings.", color=magenta)
    keep_wandering.add_choice("Fight", None)  # Placeholder
    
    # Link from follow signs
    explore_follow_signs.choices[0]["node"] = keep_wandering
    
    # Fight path - death ending
    fight_ending = StoryNode("You are weak, and frail\n\nBut nonetheless, you try to fight back.\n\nThe shadowy figures zip left and right\n\nWith no effort, they strike a vital organ and watch you fall to the ground.", color=crimson, font_size=20)
    fight_ending.add_choice("Game Over", None)  # End node, no choices
    
    # Link fight ending
    keep_wandering.choices[0]["node"] = fight_ending
    
    # Rest path - same result as keep wandering
    go_rest = StoryNode("You decide to rest, but it doesn't help.\n\nYour eyes are starting to fool you.\n\nThings that previously weren't there are appearing.\n\nShadowy figures zip around your surroundings.", color=magenta)
    go_rest.add_choice("Fight", fight_ending)  # Same ending as keep wandering
    
    # Link from follow signs
    explore_follow_signs.choices[1]["node"] = go_rest
    
    # Find window path
    find_window = StoryNode("You remember there was a window in the room you woke up in and backtrack.\n\nYou find the room and casually walk towards it.\n\nYou look out the window and find yourself on a relatively low floor.\n\nA fall from here would still kill you.", color=crimson)
    find_window.add_choice("Continue", None)  # Placeholder
    
    # Link from initial explore
    explore_initial.choices[1]["node"] = find_window
    
    # Continue window path
    window_continue = StoryNode("Curious, you look behind you.\n\nYou are met with a creature with three arms and two legs with a decaying body.\n\nIt tries to grab you, but you jump onto a trash container.\n\nYou live for another day", color=magenta)
    window_continue.add_choice("Continue", None)  # Placeholder
    
    # Link from find window
    find_window.choices[0]["node"] = window_continue
    
    # Empty streets
    empty_streets = StoryNode("As you run through the empty streets, you notice there are no cars.\n\nNo people. No sounds. Just emptiness.\n\nYou find a police station and decide to investigate.")
    empty_streets.add_choice("Enter police station", None)  # Placeholder
    empty_streets.add_choice("Keep searching the city", None)  # Placeholder
    
    # Link from window continue
    window_continue.choices[0]["node"] = empty_streets
    
    # Police station
    police_station = StoryNode("Inside, you find a detailed report about a containment breach.\n\nProject OBLIQUE: A failed attempt to cure death itself.", color=magenta)
    police_station.add_choice("Continue", None)  # Placeholder
    
    # Link from empty streets
    empty_streets.choices[0]["node"] = police_station
    
    # Officer appears
    officer_appears = StoryNode("You hear footsteps approaching from behind...")
    officer_appears.add_choice("Turn around", None)  # Placeholder
    
    # Link from police station
    police_station.choices[0]["node"] = officer_appears
    
    # Meet officer
    meet_officer = StoryNode("It's a police officer! Finally, someone normal!\n\nHe explains that the city has been evacuated.\n\nYou're being taken to a safe zone.")
    meet_officer.add_choice("Go with the officer", None)  # Placeholder
    
    # Link from officer appears
    officer_appears.choices[0]["node"] = meet_officer
    
    # True climax
    true_climax = StoryNode("As you follow the officer, something catches your eye.\n\nHis reflection in a window shows no face.\n\nYou try to run, but more officers appear.\n\nTheir badges all read: PROJECT OBLIQUE", 20, crimson)
    true_climax.add_choice("End", None)  # End node
    
    # Link from meet officer
    meet_officer.choices[0]["node"] = true_climax
    
    # City exploration
    city_exploration = StoryNode("The city seems frozen in time.\n\nStore windows are dusty but intact.\n\nYou find a newspaper dated 47 days ago:\n\n'MIRACLE CURE PROMISES IMMORTALITY'", color=magenta)
    city_exploration.add_choice("End", None)  # End node
    
    # Link from empty streets
    empty_streets.choices[1]["node"] = city_exploration
    
    #=============== LEAVE BRANCH ===============#
    
    # Try to leave
    try_leave = StoryNode("You find a window in the same room you woke up in.\n\nThe sky has a slight crimson tint.\n\nYour head is fuzzy and you don't know how you got here.", color=crimson)
    try_leave.add_choice("Break the glass", None)  # Placeholder
    try_leave.add_choice("Look closer at the window", None)  # Placeholder
    
    # Link from first choice
    first_choice.choices[1]["node"] = try_leave
    
    # Break glass
    break_glass = StoryNode("The glass shatters easily - too easily.\n\nAs you prepare to climb down, the floor beneath you creaks.\n\nSuddenly, the tiles give way and you fall into darkness...", color=magenta)
    break_glass.add_choice("Continue", None)  # Placeholder
    
    # Link from try leave
    try_leave.choices[0]["node"] = break_glass
    
    # Underground facility
    underground = StoryNode("You wake up in an underground facility.\n\nEmergency lights cast a red glow on sterile walls.\n\nTwo tunnels stretch before you.", color=crimson)
    underground.add_choice("Take left tunnel", None)  # Placeholder
    underground.add_choice("Take right tunnel", None)  # Placeholder
    
    # Link from break glass
    break_glass.choices[0]["node"] = underground
    
    # Left tunnel - Medical bay
    medical_bay = StoryNode("You find yourself in an abandoned medical bay.\n\nRows of empty tanks line the walls.\n\nA terminal flickers nearby, still operational.", color=magenta)
    medical_bay.add_choice("Access subject records", None)  # Placeholder
    
    # Link from underground
    underground.choices[0]["node"] = medical_bay
    
    # Right tunnel - Control room
    control_room = StoryNode("The tunnel opens into a massive control room.\n\nDozens of monitors show hospital rooms identical to yours.\n\nEach screen shows a different version of you, making different choices.", color=magenta)
    control_room.add_choice("Check security feeds", None)  # Placeholder
    
    # Link from underground
    underground.choices[1]["node"] = control_room
    
    # Convergence point
    convergence = StoryNode("Your memories flood back all at once.\n\nYou're not a patient. You never were.\n\nYou're the original researcher of Project OBLIQUE.\n\nThe one who discovered that immortality had a price:", color=crimson)
    convergence.add_choice("End", None)  # End node
    
    # Link to convergence from both paths
    medical_bay.choices[0]["node"] = convergence
    control_room.choices[0]["node"] = convergence
    
    # Look at padlock
    examine_padlock = StoryNode("You decide against breaking the window - something feels off.\n\nLooking closer at the padlock, you notice strange markings.\n\nThey look like... dates? Each one crossed out.", color=magenta)
    examine_padlock.add_choice("Investigate the padlock", None)  # Placeholder
    examine_padlock.add_choice("Look for another exit", None)  # Placeholder
    
    # Link from try leave
    try_leave.choices[1]["node"] = examine_padlock
    
    # Investigate padlock
    padlock_investigation = StoryNode("The padlock feels unusually warm to the touch.\n\nAs you examine it, your finger catches on a hidden switch.\n\nClick.", color=magenta)
    padlock_investigation.add_choice("Enter the hidden passage", None)  # Placeholder
    
    # Link from examine padlock
    examine_padlock.choices[0]["node"] = padlock_investigation
    
    # Observation room
    observation_room = StoryNode("You step into what appears to be an observation room.\n\nThrough one-way glass, you can see your hospital room.\n\nBut that's impossible - you just left that room.\n\nOn the bed lies another you, still unconscious.", color=crimson)
    observation_room.add_choice("Check the research terminal", None)  # Placeholder
    
    # Link from padlock investigation
    padlock_investigation.choices[0]["node"] = observation_room
    
    # Research terminal
    research_terminal = StoryNode("Project OBLIQUE - Memory Partition Test Results\n\nSubject maintains consciousness across iterations\n\nSuccess: Memory bleeding between partitions detected\n\nWarning: Subject showing signs of partition collapse", color=crimson)
    research_terminal.add_choice("Initiate protocol", None)  # Placeholder
    
    # Link from observation room
    observation_room.choices[0]["node"] = research_terminal
    
    # Protocol initiation
    protocol_wake = StoryNode("'WAKE protocol initiated'\n\nYou hear alarms blaring throughout the facility.\n\nThrough the glass, you watch as all 47 versions of you\n\nBegin to wake up simultaneously.", color=crimson)
    protocol_wake.add_choice("End", None)  # End node
    
    # Link from research terminal
    research_terminal.choices[0]["node"] = protocol_wake
    
    # Look for another exit
    another_exit = StoryNode("You turn away from the window to search elsewhere.\n\nThe room suddenly feels different - older, abandoned.\n\nDust covers everything, years worth of it.\n\nThis isn't the same room you woke up in.", color=crimson)
    another_exit.add_choice("End", None)  # End node
    
    # Link from examine padlock
    examine_padlock.choices[1]["node"] = another_exit
    
    # Create and return the story tree
    return StoryTree(game, start)