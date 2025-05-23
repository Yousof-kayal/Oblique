# Oblique Architecture Improvements

## Story Tree Structure

The game has been refactored to use a tree data structure for story management, replacing the previous approach of using conditional statements based on input strings. This offers several advantages:

1. **Cleaner Code Structure**: Each story node is represented as an object with associated text, choices, and styling.
2. **Easier Modification**: Adding or changing story branches is simpler as it's all contained in the story creation function.
3. **Reusable Components**: The story tree system can be easily reused for other text-based games.
4. **Improved Navigation**: Players can now navigate choices using keyboard up/down arrows and select with Enter.

## Key Components

### StoryNode Class
- Represents a single point in the story
- Contains text to display, formatting options, and available choices
- Each choice links to another StoryNode, creating the branching structure

### StoryTree Class
- Manages the overall story structure
- Tracks the current node and selected choice
- Handles navigation through the story

### Game Rendering
- Text is now rendered more flexibly, handling multi-line text
- Choices are displayed with visual selection indicators
- The current selection is highlighted

## Input System

The input system has been improved to use keyboard navigation instead of typing numbers:

- **Up/Down Arrows**: Navigate between choices
- **Enter**: Select the current choice and advance the story
- **Escape**: Return to the title screen

This makes the game more intuitive and interactive while maintaining the narrative focus.

## Future Improvements

1. **State Management**: Add a proper game state system to track visited paths and enable more complex story conditions
2. **Save/Load**: Implement saving progress
3. **Visual Effects**: Add text animations or transitions between story nodes
4. **Sound Effects**: Add atmospheric sounds or effects at key story moments
5. **Resource Management**: Create a dedicated system for managing assets

## Testing

To test the new architecture, run the game and verify:
- The story progresses correctly through all branches
- Up/down navigation works properly
- Choices lead to the expected story nodes
- Formatting (colors, font sizes) is preserved
- The game can return to the title screen from any point