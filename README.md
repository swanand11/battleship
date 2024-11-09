# Battleship Game 🚢

A classic two-player naval strategy game implemented in Python where you play against an AI opponent. Place your ships strategically and try to sink the AI's fleet before it sinks yours!

## 🎮 Features

- Command-line interface with clear visual representation
- Intelligent AI opponent that:
  - Uses strategic targeting after successful hits
  - Never repeats moves
  - Properly tracks ship damage
- Complete ship placement system
- Real-time game status updates
- Input validation and error handling

## 🚀 Setup

### Prerequisites
- Python 3.x
- NumPy library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/battleship.git
cd battleship
```

2. Install required dependencies:
```bash
pip install numpy
```

3. Run the game:
```bash
python main.py
```

## 📝 How to Play

### Ship Types
- Carrier (5 spaces)
- Battleship (4 spaces)
- Destroyer (3 spaces)
- Submarine (3 spaces)
- Patrol Boat (2 spaces)

### Game Rules
1. Start by placing your ships on the 10x10 grid
   - Choose ship type (1-5)
   - Select orientation (1 for horizontal, 2 for vertical)
   - Enter x,y coordinates (0-9)

2. Taking Turns
   - Players alternate turns
   - Enter coordinates to attack (x,y)
   - The game shows if it's a hit or miss
   - Ships can't be hit twice in the same spot

### Board Symbols
- `.` : Empty space
- `S` : Your ship
- `H` : Hit
- `M` : Miss

## 📁 Project Structure

```
battleship/
├── main.py          # Game initialization and main loop
├── board.py         # Board class and display logic
├── ship.py          # Ship class and ship creation
├── player.py        # Human player logic
└── computer_player.py # AI opponent logic
```

## 🎯 Game Features

### AI Strategy
- Random targeting for initial attacks
- Smart targeting system that focuses on adjacent cells after a hit
- Tracks all previous moves to avoid repetition
- Maintains a queue of potential target coordinates

### Input Validation
- Ensures all coordinates are within bounds
- Prevents overlapping ship placement
- Validates user input format

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. You can also open issues for bugs or feature suggestions.

## 🎮 Future Improvements

Planned features:
- Multiple difficulty levels for AI
- Scoring system
- Game statistics tracking
- Save/Load game functionality
- Sound effects
- Graphical user interface

## 🙏 Acknowledgments

- Inspired by the classic Battleship board game
- Thanks to the Python and NumPy communities
