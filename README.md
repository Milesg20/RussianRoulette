# Russian Roulette (Python Game)

## Overview
This is a simple text-based Russian Roulette game implemented in Python. The game simulates a deadly game of chance where you and an AI opponent take turns pulling the trigger of a revolver with a single bullet.

## Features
- Alternating turns between you and an AI opponent.
- Randomized chamber with decreasing chances as the game progresses.
- Simple input system for your actions (yes/no).
- Win/lose/draw scenarios.

## How to Play
1. Run the Python script to start the game.
2. Each round, you and the AI opponent will take turns.
3. On your turn, you'll be asked: `Pull trigger? (y/n)`
   - Type `y` to pull the trigger.
   - Type `n` to forfeit and end the game.
4. The revolver has 6 chambers, and each round one chamber becomes unavailable.
5. The player who pulls the trigger on the chamber with the bullet loses.
6. If all chambers are empty, the game ends in a draw.

## Example
```
Welcome to Russian Roulette. Try to survive!

Your turn:
Pull trigger? (y/n) y
*click* You survived. 5 chambers left.

Opponent's turn:
Opponent pulls the trigger...
*click* Opponent survived. 4 chambers left.
```

## Requirements
- Python 3.x

## Running the Game
```bash
python russian_roulette.py
```

## License
This project is for educational purposes.

---
