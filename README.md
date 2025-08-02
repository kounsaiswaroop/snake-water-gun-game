# Snake Water Gun Game

A simple command-line implementation of the classic game "Snake, Water, Gun" (similar to Rock, Paper, Scissors) in Python.

## How to Play

- The computer randomly chooses one of three options: Snake, Water, or Gun.
- You enter your choice by typing:
  - `s` for Snake
  - `w` for Water
  - `g` for Gun
- The game will then show both choices and announce the result:
  - **Snake drinks Water** - Snake wins.
  - **Water drowns Gun** - Water wins.
  - **Gun kills Snake** - Gun wins.
- If both choose the same, it's a tie.

## How to Run

1. Make sure you have Python 3 installed on your system.
2. Run the script using the command:
python snake_water_gun.py
3. Follow the on-screen instructions to enter your choice.

## Code Explanation

- The computer choice is generated randomly from the list `[-1, 0, 1]`, mapping to Gun, Water, and Snake respectively.
- User inputs are mapped to these numbers using a dictionary.
- The result is then decided based on who wins according to the rules:
- Snake beats Water
- Water beats Gun
- Gun beats Snake
- If the user inputs an invalid option, the game prompts with an error message.


## License

This project is open source and available under the MIT License.


