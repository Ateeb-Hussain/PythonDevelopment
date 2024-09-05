# Snake Water Gun Python Game

This repository contains two Python implementations of the classic Snake Water Gun game:

* **Snake_Water_Gun_Game_NoGUI.py:** A console-based version of the game.
* **Snake_Water_Gun_Game_WithGUI.py:** A graphical user interface (GUI) version of the game using Kivy.

## Gameplay

The game is simple: you choose either Snake, Water, or Gun, and the computer randomly chooses one of the three options. The winner is determined by the following rules:

- **Snake beats Water**
- **Water beats Gun**
- **Gun beats Snake**

If you win, your score increases by 1. If you lose, your score decreases by 1. If it's a draw, your score remains the same.

## Features

* **Simple and easy-to-use interface**
* **Random computer choices**
* **Score tracking**
* **Both console and GUI versions available**

## Requirements

* **Python 3.x**
* **Kivy (for GUI version)**

## Running the Game

### Console Version

1. Execute `Snake_Water_Gun_Game_NoGUI.py` using Python.

### GUI Version

1. Install Kivy using pip: `pip install kivy`
2. Execute `Snake_Water_Gun_Game_WithGUI.py` using Python.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for bug fixes, feature enhancements, or new game modes.

## License

This project is licensed under the CC0 1.0 Universal - see the [LICENSE](LICENSE) file for details.
