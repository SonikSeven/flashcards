# Flashcards

This project consists of a Python script designed to create, manage, and utilize flashcards for study purposes. Incorporating features like adding new flashcards, removing existing ones, importing/exporting cards, logging sessions, and statistics on learning efficacy, it's a versatile tool for anyone looking to improve their recall on various subjects. 

Below is the breakdown of how to get started and utilize the core features.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/flashcards.git
```

## Usage

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

The script accepts two optional arguments:

- `--import_from` to specify a file from which to import flashcards on start.
- `--export_to` to specify a file to which flashcards will be automatically exported upon exiting.

Example:
```
python flashcards.py --import_from myflashcards.txt --export_to myflashcards.txt
```

### Core Commands:
Upon starting the script, you're presented with several options:

- `add` to add a new flashcard.
- `remove` to remove an existing flashcard.
- `import` to import flashcards from a file.
- `export` to export flashcards to a file.
- `ask` to start a quiz on the flashcards.
- `exit` to exit the program (exports cards if `--export_to` is used).
- `log` to save a session log to a file.
- `hardest card` to display the card(s) with the most errors.
- `reset stats` to reset statistics for all cards.

### Adding a New Flashcard:
When adding a new flashcard, you'll be prompted to input both the term and definition.

### Removing a Flashcard:
To remove a flashcard, you'll need to specify the term you wish to delete.

### Importing and Exporting:
Flashcards can be imported from or exported to a file. The file format is straightforward:
```
term1|definition1|error_count
term2|definition2|error_count
...
```

### Debugging and Logs:
The program logs all actions in a session. To save this log, use the `log` command and specify a file name.

### Understanding the Hardest Cards:
The `hardest card` command helps to identify which flashcards need more attention based on your error count.

## License

This project is licensed under the [MIT License](LICENSE.txt).
